## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-8.data
ERROR day is out of range for month 0000   0x7e 0x0d 0x05 0x10 0xf7                   ~....
#### RECORD 0 BolusWizard 2013-06-28T13:33:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-06-28T13:33:58)
    0000   0x7a 0xa1 0x0d 0x1c 0x0d                   z....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0xff 0x2e 0xf0    <P.-j...
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             60   80   13   45  106  255   46  240
              0    0    0   45  125
    HOUR BITS: [1, 0, 1]
#### RECORD 1 Bolus 2013-06-28T13:33:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-06-28T13:33:58)
    0000   0x7a 0xa1 0x4d 0x1c 0x0d                   z.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2013-06-28T15:45:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-06-28T15:45:24)
    0000   0x58 0xad 0x2f 0x1c 0x0d                   X./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 CalBGForPH 2013-06-28T22:03:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-28T22:03:00)
    0000   0x40 0x83 0x36 0x1c 0x0d                   @.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 CalBGForPH 2013-06-28T22:11:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-28T22:11:40)
    0000   0x68 0x8b 0x36 0x1c 0x0d                   h.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 BolusWizard 2013-06-28T22:11:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-06-28T22:11:52)
    0000   0x74 0x8b 0x16 0x1c 0x0d                   t....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x02 0x21 0x00    +P.-j.!.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             43   80   13   45  106    2   33    0
              0    0    0   35  125
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Bolus 2013-06-28T22:11:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-06-28T22:11:52)
    0000   0x74 0x8b 0x56 0x1c 0x0d                   t.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 MResultTotals (2013, 0, 28, 20, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 28, 20, 4, 0))
    0000   0x00 0x04 0xb4 0x7c 0x0d                   ...|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 8 Model522ResultTotals 2013-06-29T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-29T00:00:00)
    0000   0x7c 0x0d 0x05 0x00 0x7a                   |...z
    body (38)
    hex
    0000   0x68 0x88 0x04 0x00 0x00 0x04 0xb4 0x03    h.......
    0008   0x74 0x49 0x01 0x40 0x1b 0x00 0x67 0x01    tI.@..g.
    0010   0x40 0x1b 0x01 0x38 0x61 0x00 0x08 0x03    @..8a...
    0018   0x00 0x00 0x00 0x02 0x01 0x00 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            104  136    4    0    0    4  180    3
            116   73    1   64   27    0  103    1
             64   27    1   56   97    0    8    3
              0    0    0    2    1    0    1    0
             12    0  232    0    0    0
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 CalBGForPH 2013-06-29T08:43:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-06-29T08:43:46)
    0000   0x6e 0xab 0x28 0x1d 0x8d                   n.(..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 BolusWizard 2013-06-29T08:43:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 269,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
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
    0000   0x5b 0x0d                                  [.
    decimal
             91   13
    datetime (2013-06-29T08:43:48)
    0000   0x70 0xab 0x08 0x1d 0x0d                   p....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   32    0    0
              0    0    0   32  125
    HOUR BITS: [1, 0, 1]
#### RECORD 11 LowReservoir 2013-06-29T08:45:53 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-29T08:45:53)
    0000   0x75 0xad 0x08 0x1d 0x0d                   u....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 Bolus 2013-06-29T08:43:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-06-29T08:43:48)
    0000   0x70 0xab 0x48 0x1d 0x0d                   p.H..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 BolusWizard 2013-06-29T12:55:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
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
    datetime (2013-06-29T12:55:44)
    0000   0x6c 0xb7 0x0c 0x1d 0x0d                   l....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 0, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 251, 'amount': 2.9, 'curve': 4},
 {'age': 5, 'amount': 0.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0xfb 0x04 0x0c 0x05 0x14    \.t.....
    decimal
             92    8  116  251    4   12    5   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-06-29T12:55:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-06-29T12:55:45)
    0000   0x6d 0xb7 0x4c 0x1d 0x0d                   m.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 LowReservoir 2013-06-29T17:03:09 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-29T17:03:09)
    0000   0x49 0x83 0x11 0x1d 0x0d                   I....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 CalBGForPH 2013-06-29T22:16:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-29T22:16:35)
    0000   0x63 0x90 0x36 0x1d 0x0d                   c.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 BolusWizard 2013-06-29T22:17:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-06-29T22:17:30)
    0000   0x5e 0x91 0x16 0x1d 0x0d                   ^....
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x02 0x2b 0x00    8P.-j.+.
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             56   80   13   45  106    2   43    0
              0    0    0   45  125
    HOUR BITS: [1, 0, 0]
#### RECORD 19 Bolus 2013-06-29T22:17:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-06-29T22:17:30)
    0000   0x5e 0x91 0x56 0x1d 0x0d                   ^.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 BolusWizard 2013-06-29T23:02:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
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
    datetime (2013-06-29T23:02:42)
    0000   0x6a 0x82 0x17 0x1d 0x0d                   j....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 0, 0]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 4.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0x30 0x04                   \..0.
    decimal
             92    5  180   48    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-06-29T23:02:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-06-29T23:02:42)
    0000   0x6a 0x82 0x57 0x1d 0x0d                   j.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 MResultTotals (2013, 0, 29, 28, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 29, 28, 5, 0))
    0000   0x00 0x05 0x1c 0x7d 0x0d                   ...}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 24 Model522ResultTotals 2013-06-30T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-30T00:00:00)
    0000   0x7d 0x0d 0x05 0x10 0xcb                   }....
    body (38)
    hex
    0000   0x88 0x0d 0x02 0x00 0x00 0x05 0x1c 0x03    ........
    0008   0x84 0x45 0x01 0x98 0x1f 0x00 0x5a 0x01    .E....Z.
    0010   0x98 0x1f 0x01 0x10 0x43 0x00 0x88 0x21    ....C..!
    0018   0x00 0x00 0x00 0x04 0x02 0x01 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            136   13    2    0    0    5   28    3
            132   69    1  152   31    0   90    1
            152   31    1   16   67    0  136   33
              0    0    0    4    2    1    1    0
             12    0  232    0    0    0
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 25 CalBGForPH 2013-06-30T03:22:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 299}
```
    op hex (2)
    0000   0x0a 0x2b                                  .+
    decimal
             10   43
    datetime (2013-06-30T03:22:22)
    0000   0x56 0x96 0x23 0x1e 0x8d                   V.#..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 BolusWizard 2013-06-30T03:22:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 38,
 '_byte[7]': 0,
 'bg': 299,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2b                                  [+
    decimal
             91   43
    datetime (2013-06-30T03:22:26)
    0000   0x5a 0x96 0x03 0x1e 0x0d                   Z....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x26 0x00 0x00    .Q.-j&..
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
              0   81   13   45  106   38    0    0
              0    0    0   38  125
    HOUR BITS: [1, 0, 0]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 1.2, 'curve': 20},
 {'age': 52, 'amount': 4.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x0c 0x14 0xb4 0x34 0x14    \.0...4.
    decimal
             92    8   48   12   20  180   52   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-06-30T03:22:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-06-30T03:22:26)
    0000   0x5a 0x96 0x43 0x1e 0x0d                   Z.C..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 PumpSuspend 2013-06-30T09:05:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-30T09:05:49)
    0000   0x71 0x85 0x09 0x1e 0x0d                   q....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 PumpResume 2013-06-30T09:29:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-30T09:29:59)
    0000   0x7b 0x9d 0x09 0x1e 0x0d                   {....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 Rewind 2013-06-30T09:30:13 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-30T09:30:13)
    0000   0x4d 0x9e 0x09 0x1e 0x0d                   M....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 Prime 2013-06-30T09:32:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2013-06-30T09:32:13)
    0000   0x4d 0xa0 0x29 0x1e 0x0d                   M.)..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 Prime 2013-06-30T09:32:33 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-30T09:32:33)
    0000   0x61 0xa0 0x09 0x1e 0x0d                   a....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 34 CalBGForPH 2013-06-30T10:09:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 290}
```
    op hex (2)
    0000   0x0a 0x22                                  ."
    decimal
             10   34
    datetime (2013-06-30T10:09:29)
    0000   0x5d 0x89 0x2a 0x1e 0x8d                   ].*..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 BolusWizard 2013-06-30T10:09:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 290,
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
    0000   0x5b 0x22                                  ["
    decimal
             91   34
    datetime (2013-06-30T10:09:32)
    0000   0x60 0x89 0x0a 0x1e 0x0d                   `....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [1, 0, 0]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 149, 'amount': 1.5, 'curve': 20},
 {'age': 159, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x95 0x14 0x5c 0x9f 0x14    \.<..\..
    decimal
             92    8   60  149   20   92  159   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-06-30T10:09:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-30T10:09:32)
    0000   0x60 0x89 0x4a 0x1e 0x0d                   `.J..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 CalBGForPH 2013-06-30T11:22:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-06-30T11:22:41)
    0000   0x69 0x96 0x2b 0x1e 0x0d                   i.+..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 BolusWizard 2013-06-30T12:09:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-06-30T12:09:30)
    0000   0x5e 0x89 0x0c 0x1e 0x0d                   ^....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 3.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x7d 0x04                   \..}.
    decimal
             92    5  144  125    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-06-30T12:09:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-06-30T12:09:30)
    0000   0x5e 0x89 0x4c 0x1e 0x0d                   ^.L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 BolusWizard 2013-06-30T12:52:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
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
    datetime (2013-06-30T12:52:49)
    0000   0x71 0xb4 0x0c 0x1e 0x0d                   q....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 4.6, 'curve': 4},
 {'age': 168, 'amount': 3.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb8 0x30 0x04 0x90 0xa8 0x04    \..0....
    decimal
             92    8  184   48    4  144  168    4
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-06-30T12:52:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-06-30T12:52:49)
    0000   0x71 0xb4 0x4c 0x1e 0x0d                   q.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 CalBGForPH 2013-06-30T18:34:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 329}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-06-30T18:34:35)
    0000   0x63 0xa2 0x32 0x1e 0x8d                   c.2..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 46 BolusWizard 2013-06-30T18:34:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 45,
 '_byte[7]': 0,
 'bg': 329,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x49                                  [I
    decimal
             91   73
    datetime (2013-06-30T18:34:37)
    0000   0x65 0xa2 0x12 0x1e 0x0d                   e....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2d 0x00 0x00    .Q.-j-..
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
              0   81   13   45  106   45    0    0
              0    0    0   45  125
    HOUR BITS: [1, 0, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 1.0, 'curve': 20},
 {'age': 134, 'amount': 4.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x5e 0x14 0xb8 0x86 0x14    \.(^....
    decimal
             92    8   40   94   20  184  134   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-06-30T18:34:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-06-30T18:34:37)
    0000   0x65 0xa2 0x52 0x1e 0x0d                   e.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 CalBGForPH 2013-06-30T21:37:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 207}
```
    op hex (2)
    0000   0x0a 0xcf                                  ..
    decimal
             10  207
    datetime (2013-06-30T21:37:43)
    0000   0x6b 0xa5 0x35 0x1e 0x0d                   k.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 50 BolusWizard 2013-06-30T21:37:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 207,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcf                                  [.
    decimal
             91  207
    datetime (2013-06-30T21:37:55)
    0000   0x77 0xa5 0x15 0x1e 0x0d                   w....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x08 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    8    0   10  125
    HOUR BITS: [1, 0, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 4.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0xb7 0x04                   \....
    decimal
             92    5  180  183    4
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-06-30T21:37:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-06-30T21:37:55)
    0000   0x77 0xa5 0x55 0x1e 0x0d                   w.U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 53 CalBGForPH 2013-06-30T21:57:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2013-06-30T21:57:50)
    0000   0x72 0xb9 0x35 0x1e 0x0d                   r.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 BolusWizard 2013-06-30T21:58:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 159,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.6,
 'carb_input': 73,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 5.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2013-06-30T21:58:12)
    0000   0x4c 0xba 0x15 0x1e 0x0d                   L....
    body (13)
    hex
    0000   0x49 0x50 0x0d 0x2d 0x6a 0x07 0x38 0x00    IP.-j.8.
    0008   0x00 0x10 0x00 0x38 0x7d                   ...8}
    decimal
             73   80   13   45  106    7   56    0
              0   16    0   56  125
    HOUR BITS: [1, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 1.1, 'curve': 4},
 {'age': 204, 'amount': 4.5, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x18 0x04 0xb4 0xcc 0x04    \.,.....
    decimal
             92    8   44   24    4  180  204    4
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-06-30T21:58:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2013-06-30T21:58:12)
    0000   0x4c 0xba 0x55 0x1e 0x0d                   L.U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 57 MResultTotals (2013, 0, 30, 26, 7, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 30, 26, 7, 0))
    0000   0x00 0x07 0x3a 0x7e 0x0d                   ..:~.
    body (0)
    DAY BITS: [0, 1, 1]
ERROR day is out of range for month 0000   0x7e 0x0d 0x05 0x10 0xf7                   ~....
#### RECORD 58 Model522ResultTotals (2013, 6, 31, 0, 0, 0) head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime ((2013, 6, 31, 0, 0, 0))
    0000   0x7e 0x0d 0x05 0x10 0xf7                   ~....
    body (38)
    hex
    0000   0x9f 0x49 0x06 0x00 0x00 0x07 0x3a 0x03    .I....:.
    0008   0x72 0x30 0x03 0xc8 0x34 0x00 0x93 0x03    r0..4...
    0010   0xc8 0x34 0x01 0xc0 0x2e 0x02 0x08 0x36    .4.....6
    0018   0x00 0x00 0x00 0x07 0x03 0x04 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            159   73    6    0    0    7   58    3
            114   48    3  200   52    0  147    3
            200   52    1  192   46    2    8   54
              0    0    0    7    3    4    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 1, 1, 1]
#### RECORD 59 CalBGForPH 2013-07-01T02:15:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 322}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-07-01T02:15:06)
    0000   0x46 0xcf 0x22 0x01 0x8d                   F."..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 BolusWizard 2013-07-01T02:15:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 43,
 '_byte[7]': 0,
 'bg': 322,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x42                                  [B
    decimal
             91   66
    datetime (2013-07-01T02:15:12)
    0000   0x4c 0xcf 0x02 0x01 0x0d                   L....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2b 0x00 0x00    .Q.-j+..
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
              0   81   13   45  106   43    0    0
              0    0    0   43  125
    HOUR BITS: [1, 1, 0]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 5.6, 'curve': 20},
 {'age': 25, 'amount': 1.1, 'curve': 20},
 {'age': 205, 'amount': 4.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xe0 0x05 0x14 0x2c 0x19 0x14    \....,..
    0008   0xb4 0xcd 0x14                             ...
    decimal
             92   11  224    5   20   44   25   20
            180  205   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-07-01T02:15:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-07-01T02:15:12)
    0000   0x4c 0xcf 0x42 0x01 0x0d                   L.B..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 PumpSuspend 2013-07-01T12:05:47 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-01T12:05:47)
    0000   0x6f 0xc5 0x0c 0x01 0x0d                   o....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 PumpResume 2013-07-01T12:23:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-01T12:23:30)
    0000   0x5e 0xd7 0x0c 0x01 0x0d                   ^....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 CalBGForPH 2013-07-01T12:37:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2013-07-01T12:37:29)
    0000   0x5d 0xe5 0x2c 0x01 0x0d                   ].,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 BolusWizard 2013-07-01T12:37:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 226,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe2                                  [.
    decimal
             91  226
    datetime (2013-07-01T12:37:34)
    0000   0x62 0xe5 0x0c 0x01 0x0d                   b....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [1, 1, 1]
#### RECORD 67 Bolus 2013-07-01T12:37:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-07-01T12:37:34)
    0000   0x62 0xe5 0x4c 0x01 0x0d                   b.L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 CalBGForPH 2013-07-01T13:40:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-07-01T13:40:34)
    0000   0x62 0xe8 0x2d 0x01 0x0d                   b.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 BolusWizard 2013-07-01T13:41:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 19,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 1.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-07-01T13:41:47)
    0000   0x6f 0xe9 0x0d 0x01 0x0d                   o....
    body (13)
    hex
    0000   0x13 0x50 0x0d 0x2d 0x6a 0x07 0x0e 0x00    .P.-j...
    0008   0x00 0x12 0x00 0x0e 0x7d                   ....}
    decimal
             19   80   13   45  106    7   14    0
              0   18    0   14  125
    HOUR BITS: [1, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x43 0x04                   \.\C.
    decimal
             92    5   92   67    4
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-07-01T13:41:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-07-01T13:41:48)
    0000   0x70 0xe9 0x4d 0x01 0x0d                   p.M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 CalBGForPH 2013-07-01T14:56:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2013-07-01T14:56:26)
    0000   0x5a 0xf8 0x2e 0x01 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 CalBGForPH 2013-07-01T18:49:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-07-01T18:49:35)
    0000   0x63 0xf1 0x32 0x01 0x0d                   c.2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 BolusWizard 2013-07-01T18:49:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 90,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5a                                  [Z
    decimal
             91   90
    datetime (2013-07-01T18:49:46)
    0000   0x6e 0xf1 0x12 0x01 0x0d                   n....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfc 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             55   80   13   45  106  252   42  240
              0    0    0   38  125
    HOUR BITS: [1, 1, 1]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 1.4, 'curve': 20},
 {'age': 119, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x38 0x3b 0x14 0x5c 0x77 0x14    \.8;.\w.
    decimal
             92    8   56   59   20   92  119   20
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-07-01T18:49:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-07-01T18:49:46)
    0000   0x6e 0xf1 0x52 0x01 0x0d                   n.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 77 MResultTotals (2013, 0, 1, 16, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 1, 16, 5, 0))
    0000   0x00 0x05 0x50 0x61 0x8d                   ..Pa.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 78 Model522ResultTotals 2013-07-02T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-02T00:00:00)
    0000   0x61 0x8d 0x05 0x10 0xc7                   a....
    body (38)
    hex
    0000   0x5a 0x42 0x05 0x00 0x00 0x05 0x50 0x03    ZB....P.
    0008   0x78 0x41 0x01 0xd8 0x23 0x00 0x4a 0x01    xA..#.J.
    0010   0xd8 0x23 0x00 0xd0 0x2c 0x01 0x08 0x38    .#..,..8
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             90   66    5    0    0    5   80    3
            120   65    1  216   35    0   74    1
            216   35    0  208   44    1    8   56
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 79 PumpSuspend 2013-07-02T13:25:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-02T13:25:09)
    0000   0x49 0xd9 0x0d 0x02 0x0d                   I....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 80 PumpResume 2013-07-02T13:48:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-02T13:48:37)
    0000   0x65 0xf0 0x0d 0x02 0x0d                   e....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 81 CalBGForPH 2013-07-02T15:36:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 168}
```
    op hex (2)
    0000   0x0a 0xa8                                  ..
    decimal
             10  168
    datetime (2013-07-02T15:36:53)
    0000   0x75 0xe4 0x2f 0x02 0x0d                   u./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 82 CalBGForPH 2013-07-02T15:38:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-07-02T15:38:41)
    0000   0x69 0xe6 0x2f 0x02 0x0d                   i./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 BolusWizard 2013-07-02T15:38:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.5,
 'carb_input': 76,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 5.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-07-02T15:38:51)
    0000   0x73 0xe6 0x0f 0x02 0x0d                   s....
    body (13)
    hex
    0000   0x4c 0x50 0x0d 0x2d 0x6a 0x07 0x3a 0x00    LP.-j.:.
    0008   0x00 0x00 0x00 0x41 0x7d                   ...A}
    decimal
             76   80   13   45  106    7   58    0
              0    0    0   65  125
    HOUR BITS: [1, 1, 1]
#### RECORD 84 Bolus 2013-07-02T15:38:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.5, 'dual_component': '??', 'programmed': 6.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x41 0x41 0x00                        .AA.
    decimal
              1   65   65    0
    datetime (2013-07-02T15:38:51)
    0000   0x73 0xe6 0x4f 0x02 0x0d                   s.O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 85 Base unknown head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0x81                                  N.
    decimal
             78  129
    datetime (unknown)

    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-8.data: 86 records`
