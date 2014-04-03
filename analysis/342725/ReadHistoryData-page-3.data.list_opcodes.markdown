## START logs/ReadHistoryData-page-3.data
#### RECORD 0 Bolus 2014-03-12T00:36:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x08 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    8    0
    datetime (2014-03-12T00:36:50)
    0000   0x32 0xe4 0x40 0x0c 0x0e                   2.@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 BasalProfileStart 2014-03-12T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-12T02:00:00)
    0000   0x00 0xc0 0x02 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BasalProfileStart 2014-03-12T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-12T04:00:00)
    0000   0x00 0xc0 0x04 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2014-03-12T05:28:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 314}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2014-03-12T05:28:32)
    0000   0x20 0xdc 0x25 0x6c 0x8e                    .%l.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 Ian3F 2014-03-12T05:28:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2014-03-12T05:28:32)
    0000   0x20 0xdc 0x45 0x6c 0x0e                    .El.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2014-03-12T05:28:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 314,
 'bg_target_high': 1,
 'bg_target_low': 30,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3a                                  [:
    decimal
             91   58
    datetime (2014-03-12T05:28:55)
    0000   0x37 0xdc 0x05 0x0c 0x0e                   7....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x1e 0x50 0x1c 0x00    .Q.n.P..
    0008   0x00 0x08 0x00 0x00 0x01 0x1c 0x64         ......d
    decimal
              0   81    0  110   30   80   28    0
              0    8    0    0    1   28  100
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.7, 'curve': 144},
 {'age': 100, 'amount': 0.25, 'curve': 144},
 {'age': 110, 'amount': 0.05, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0x28 0x90 0x0a 0x64 0x90    \.D(..d.
    0008   0x02 0x6e 0x90                             .n.
    decimal
             92   11   68   40  144   10  100  144
              2  110  144
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2014-03-12T05:28:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x1c 0x01 0x1c 0x00 0x00 0x00    ........
    decimal
              1    1   28    1   28    0    0    0
    datetime (2014-03-12T05:28:55)
    0000   0x37 0xdc 0x45 0x0c 0x0e                   7.E..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 BasalProfileStart 2014-03-12T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-12T06:00:00)
    0000   0x00 0xc0 0x06 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 9 Rewind 2014-03-12T07:21:44 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-03-12T07:21:44)
    0000   0x2c 0xd5 0x07 0x0c 0x0e                   ,....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 Prime 2014-03-12T07:22:20 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 7.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x4c                   ....L
    decimal
              3    0    0    0   76
    datetime (2014-03-12T07:22:20)
    0000   0x14 0xd6 0x27 0x0c 0x0e                   ..'..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BasalProfileStart 2014-03-12T07:22:35 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-12T07:22:35)
    0000   0x23 0xd6 0x07 0x0c 0x0e                   #....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2014-03-12T08:05:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2014-03-12T08:05:26)
    0000   0x1a 0xc5 0x28 0x6c 0x0e                   ..(l.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian3F 2014-03-12T08:05:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-12T08:05:26)
    0000   0x1a 0xc5 0xa8 0x6c 0x0e                   ...l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 PumpSuspend 2014-03-12T08:05:45 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-12T08:05:45)
    0000   0x2d 0xc5 0x08 0x0c 0x0e                   -....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2014-03-12T08:36:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2014-03-12T08:36:20)
    0000   0x14 0xe4 0x28 0x6c 0x0e                   ..(l.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2014-03-12T08:36:20 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-12T08:36:20)
    0000   0x14 0xe4 0xa8 0x6c 0x0e                   ...l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 BasalProfileStart 2014-03-12T09:27:49 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-12T09:27:49)
    0000   0x31 0xdb 0x09 0x0c 0x0e                   1....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 18 PumpResume 2014-03-12T09:27:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-12T09:27:49)
    0000   0x31 0xdb 0x09 0x0c 0x0e                   1....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 BolusWizard 2014-03-12T09:28:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 45,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 160}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-12T09:28:00)
    0000   0x00 0xdc 0x09 0x6c 0x0e                   ...l.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    -P.n(P..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x64         ......d
    decimal
             45   80    0  110   40   80    0    0
            160    0    0    0    0  160  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 236, 'amount': 2.5, 'curve': 128},
 {'age': 246, 'amount': 4.6, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0xec 0x80 0xb8 0xf6 0x80    \.d.....
    decimal
             92    8  100  236  128  184  246  128
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2014-03-12T09:28:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2014-03-12T09:28:00)
    0000   0x00 0xdc 0x49 0x6c 0x0e                   ..Il.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 NoDelivery 2014-03-12T10:09:29 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x3b 0x01 0x08                        .;..
    decimal
              6   59    1    8
    datetime (2014-03-12T10:09:29)
    0000   0x1d 0xc9 0x6a 0xcc 0x0e                   ..j..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0]
#### RECORD 23 ClearAlarm 2014-03-12T10:11:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x3b                                  .;
    decimal
             12   59
    datetime (2014-03-12T10:11:06)
    0000   0x06 0xcb 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 BasalProfileStart 2014-03-12T10:11:06 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-12T10:11:06)
    0000   0x06 0xcb 0x0a 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BasalProfileStart 2014-03-12T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-12T10:30:00)
    0000   0x00 0xde 0x0a 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 CalBGForPH 2014-03-12T10:30:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2014-03-12T10:30:12)
    0000   0x0c 0xde 0x2a 0x6c 0x0e                   ..*l.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2014-03-12T10:30:12 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-03-12T10:30:12)
    0000   0x0c 0xde 0x2a 0x6c 0x0e                   ..*l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 TempBasal 2014-03-12T10:31:09 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-12T10:31:09)
    0000   0x09 0xdf 0x0a 0x0c 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 29 TempBasalDuration 2014-03-12T10:31:09 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-12T10:31:09)
    0000   0x09 0xdf 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 TempBasal 2014-03-12T10:31:59 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-12T10:31:59)
    0000   0x3b 0xdf 0x0a 0x0c 0x0e                   ;....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 31 TempBasalDuration 2014-03-12T10:31:59 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2014-03-12T10:31:59)
    0000   0x3b 0xdf 0x0a 0x0c 0x0e                   ;....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BasalProfileStart 2014-03-12T10:31:59 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-12T10:31:59)
    0000   0x3b 0xdf 0x0a 0x0c 0x0e                   ;....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 33 ChangeTimeDisplay 2014-03-12T10:32:14 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2014-03-12T10:32:14)
    0000   0x0e 0xe0 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 ChangeTime 2014-03-12T10:32:19 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2014-03-12T10:32:19)
    0000   0x13 0xe0 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 NewTimeSet 2014-03-12T12:32:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2014-03-12T12:32:00)
    0000   0x00 0xe0 0x0c 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 TempBasal 2014-03-12T12:32:15 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-12T12:32:15)
    0000   0x0f 0xe0 0x0c 0x0c 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 37 TempBasalDuration 2014-03-12T12:32:15 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-12T12:32:15)
    0000   0x0f 0xe0 0x0c 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BasalProfileStart 2014-03-12T13:32:15 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-12T13:32:15)
    0000   0x0f 0xe0 0x0d 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2014-03-12T14:13:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-12T14:13:20)
    0000   0x14 0xcd 0x0e 0x6c 0x0e                   ...l.
    body (15)
    hex
    0000   0x20 0x50 0x00 0x78 0x32 0x50 0x00 0x00     P.x2P..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x64         h....hd
    decimal
             32   80    0  120   50   80    0    0
            104    0    0    0    0  104  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 4.0, 'curve': 128},
 {'age': 145, 'amount': 2.5, 'curve': 144},
 {'age': 155, 'amount': 4.6, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa0 0xab 0x80 0x64 0x91 0x90    \....d..
    0008   0xb8 0x9b 0x90                             ...
    decimal
             92   11  160  171  128  100  145  144
            184  155  144
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2014-03-12T14:13:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2014-03-12T14:13:20)
    0000   0x14 0xcd 0x4e 0x6c 0x0e                   ..Nl.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 BolusWizard 2014-03-12T14:40:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-12T14:40:15)
    0000   0x0f 0xe8 0x0e 0x6c 0x0e                   ...l.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x64         0....0d
    decimal
             15   80    0  120   50   80    0    0
             48    0    0    0    0   48  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 2.6, 'curve': 128},
 {'age': 198, 'amount': 4.0, 'curve': 128},
 {'age': 172, 'amount': 2.5, 'curve': 144},
 {'age': 182, 'amount': 4.6, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0x1c 0x80 0xa0 0xc6 0x80    \.h.....
    0008   0x64 0xac 0x90 0xb8 0xb6 0x90              d.....
    decimal
             92   14  104   28  128  160  198  128
            100  172  144  184  182  144
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2014-03-12T14:40:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x58 0x00    ..0.0.X.
    decimal
              1    0   48    0   48    0   88    0
    datetime (2014-03-12T14:40:15)
    0000   0x0f 0xe8 0x4e 0x6c 0x0e                   ..Nl.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 CalBGForPH 2014-03-12T19:35:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2014-03-12T19:35:13)
    0000   0x0d 0xe3 0x33 0x6c 0x0e                   ..3l.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2014-03-12T19:35:13 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2014-03-12T19:35:13)
    0000   0x0d 0xe3 0x93 0x6c 0x0e                   ...l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 PumpSuspend 2014-03-12T19:36:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-12T19:36:19)
    0000   0x13 0xe4 0x13 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 CalBGForPH 2014-03-12T21:58:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2014-03-12T21:58:17)
    0000   0x11 0xfa 0x35 0x6c 0x0e                   ..5l.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 Ian3F 2014-03-12T21:58:17 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-03-12T21:58:17)
    0000   0x11 0xfa 0x55 0x6c 0x0e                   ..Ul.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 BasalProfileStart 2014-03-12T21:58:18 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-12T21:58:18)
    0000   0x12 0xfa 0x15 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 51 PumpResume 2014-03-12T21:58:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-12T21:58:19)
    0000   0x13 0xfa 0x15 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 BolusWizard 2014-03-12T21:58:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 146,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2014-03-12T21:58:27)
    0000   0x1b 0xfa 0x15 0x0c 0x0e                   .....
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x32 0x50 0x24 0x00    #P.n2P$.
    0008   0x7c 0x00 0x00 0x00 0x00 0xa0 0x64         |.....d
    decimal
             35   80    0  110   50   80   36    0
            124    0    0    0    0  160  100
    HOUR BITS: [1, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 190, 'amount': 1.2, 'curve': 144},
 {'age': 210, 'amount': 2.6, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0xbe 0x90 0x68 0xd2 0x90    \.0..h..
    decimal
             92    8   48  190  144  104  210  144
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2014-03-12T21:58:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2014-03-12T21:58:27)
    0000   0x1b 0xfa 0x55 0x0c 0x0e                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 55 BasalProfileStart 2014-03-12T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-12T22:30:00)
    0000   0x00 0xde 0x16 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 56 BasalProfileStart 2014-03-13T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-13T00:00:00)
    0000   0x00 0xc0 0x00 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 57 MResultTotals 2014-03-13T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xa3                   .....
    decimal
              7    0    0    4  163
    datetime (2014-03-13T00:00:00)
    0000   0x2c 0x8e                                  ,.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 58 Sara6E 2014-03-13T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-13T00:00:00)
    0000   0x2c 0x8e                                  ,.
    body (49)
    hex
    0000   0x05 0x10 0x93 0x45 0x3a 0x08 0x00 0x00    ...E:...
    0008   0x04 0xa3 0x01 0x6b 0x1f 0x03 0x38 0x45    ...k..8E
    0010   0x00 0x7f 0x01 0x38 0x01 0x60 0x00 0xa0    ...8.`..
    0018   0x00 0x00 0x03 0x02 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  147   69   58    8    0    0
              4  163    1  107   31    3   56   69
              0  127    1   56    1   96    0  160
              0    0    3    2    1    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 59 BasalProfileStart 2014-03-13T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-13T02:00:00)
    0000   0x00 0xc0 0x02 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BasalProfileStart 2014-03-13T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-13T04:00:00)
    0000   0x00 0xc0 0x04 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 BasalProfileStart 2014-03-13T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-13T06:00:00)
    0000   0x00 0xc0 0x06 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 62 CalBGForPH 2014-03-13T07:34:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2014-03-13T07:34:51)
    0000   0x33 0xe2 0x27 0x6d 0x0e                   3.'m.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2014-03-13T07:34:51 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-03-13T07:34:51)
    0000   0x33 0xe2 0x67 0x6d 0x0e                   3.gm.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2014-03-13T09:04:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2014-03-13T09:04:18)
    0000   0x12 0xc4 0x29 0x0d 0x0e                   ..)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 BolusWizard 2014-03-13T09:04:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 2,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 4}
```
    op hex (2)
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2014-03-13T09:04:21)
    0000   0x15 0xc4 0x09 0x0d 0x0e                   .....
    body (15)
    hex
    0000   0x02 0x50 0x00 0x6e 0x28 0x50 0x08 0x00    .P.n(P..
    0008   0x04 0x00 0x00 0x00 0x00 0x0c 0x64         ......d
    decimal
              2   80    0  110   40   80    8    0
              4    0    0    0    0   12  100
    HOUR BITS: [1, 1, 0]
#### RECORD 66 Bolus 2014-03-13T09:04:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x00 0x00    ........
    decimal
              1    0   12    0   12    0    0    0
    datetime (2014-03-13T09:04:21)
    0000   0x15 0xc4 0x49 0x0d 0x0e                   ..I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 BasalProfileStart 2014-03-13T09:26:02 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-13T09:26:02)
    0000   0x02 0xda 0x09 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 68 Prime 2014-03-13T09:25:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-03-13T09:25:52)
    0000   0x34 0xd9 0x09 0x0d 0x0e                   4....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BolusWizard 2014-03-13T09:34:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-13T09:34:45)
    0000   0x2d 0xe2 0x09 0x6d 0x0e                   -..m.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    .P.n(P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   40   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 0.3, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x0c 0x20 0x80                   \.. .
    decimal
             92    5   12   32  128
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2014-03-13T09:34:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x0c 0x00    ..4.4...
    decimal
              1    0   52    0   52    0   12    0
    datetime (2014-03-13T09:34:46)
    0000   0x2e 0xe2 0x49 0x6d 0x0e                   ..Im.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 BolusWizard 2014-03-13T09:45:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-13T09:45:26)
    0000   0x1a 0xed 0x09 0x6d 0x0e                   ...m.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    .P.n(P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   40   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 1.3, 'curve': 128},
 {'age': 43, 'amount': 0.3, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x0d 0x80 0x0c 0x2b 0x80    \.4...+.
    decimal
             92    8   52   13  128   12   43  128
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2014-03-13T09:45:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x3c 0x00    ..4.4.<.
    decimal
              1    0   52    0   52    0   60    0
    datetime (2014-03-13T09:45:26)
    0000   0x1a 0xed 0x49 0x6d 0x0e                   ..Im.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 BasalProfileStart 2014-03-13T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-13T10:30:00)
    0000   0x00 0xde 0x0a 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 76 CalBGForPH 2014-03-13T11:40:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2014-03-13T11:40:07)
    0000   0x07 0xe8 0x2b 0x6d 0x0e                   ..+m.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 77 Ian3F 2014-03-13T11:40:07 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-13T11:40:07)
    0000   0x07 0xe8 0x2b 0x6d 0x0e                   ..+m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 78 CalBGForPH 2014-03-13T11:40:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2014-03-13T11:40:41)
    0000   0x29 0xe8 0x2b 0x6d 0x0e                   ).+m.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 79 Ian3F 2014-03-13T11:40:41 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-03-13T11:40:41)
    0000   0x29 0xe8 0x8b 0x6d 0x0e                   )..m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 80 BolusWizard 2014-03-13T11:41:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 148,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x94                                  [.
    decimal
             91  148
    datetime (2014-03-13T11:41:04)
    0000   0x04 0xe9 0x0b 0x0d 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x24 0x00    .P.x2P$.
    0008   0x00 0x00 0x00 0x04 0x00 0x20 0x64         ..... d
    decimal
              0   80    0  120   50   80   36    0
              0    0    0    4    0   32  100
    HOUR BITS: [1, 1, 1]
#### RECORD 81 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 119, 'amount': 1.3, 'curve': 128},
 {'age': 129, 'amount': 1.3, 'curve': 128},
 {'age': 159, 'amount': 0.3, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x77 0x80 0x34 0x81 0x80    \.4w.4..
    0008   0x0c 0x9f 0x80                             ...
    decimal
             92   11   52  119  128   52  129  128
             12  159  128
    datetime (unknown)

    body (0)

#### RECORD 82 Bolus 2014-03-13T11:41:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x04 0x00    ........
    decimal
              1    0   16    0   16    0    4    0
    datetime (2014-03-13T11:41:04)
    0000   0x04 0xe9 0x4b 0x0d 0x0e                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 BolusWizard 2014-03-13T13:04:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-13T13:04:17)
    0000   0x11 0xc4 0x0d 0x0d 0x0e                   .....
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x64          .... d
    decimal
             10   80    0  120   50   80    0    0
             32    0    0    0    0   32  100
    HOUR BITS: [1, 1, 0]
#### RECORD 84 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 0.4, 'curve': 128},
 {'age': 202, 'amount': 1.3, 'curve': 128},
 {'age': 212, 'amount': 1.3, 'curve': 128},
 {'age': 242, 'amount': 0.3, 'curve': 128}]
```
    op hex (14)
    0000   0x5c 0x0e 0x10 0x5c 0x80 0x34 0xca 0x80    \..\.4..
    0008   0x34 0xd4 0x80 0x0c 0xf2 0x80              4.....
    decimal
             92   14   16   92  128   52  202  128
             52  212  128   12  242  128
    datetime (unknown)

    body (0)

#### RECORD 85 Bolus 2014-03-13T13:04:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x04 0x00    .. . ...
    decimal
              1    0   32    0   32    0    4    0
    datetime (2014-03-13T13:04:17)
    0000   0x11 0xc4 0x4d 0x0d 0x0e                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 86 BolusWizard 2014-03-13T14:51:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-13T14:51:18)
    0000   0x12 0xf3 0x0e 0x6d 0x0e                   ...m.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             25   80    0  120   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 87 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 0.8, 'curve': 128},
 {'age': 199, 'amount': 0.4, 'curve': 128},
 {'age': 53, 'amount': 1.3, 'curve': 144},
 {'age': 63, 'amount': 1.3, 'curve': 144},
 {'age': 93, 'amount': 0.3, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x6d 0x80 0x10 0xc7 0x80    \. m....
    0008   0x34 0x35 0x90 0x34 0x3f 0x90 0x0c 0x5d    45.4?..]
    0010   0x90                                       .
    decimal
             92   17   32  109  128   16  199  128
             52   53  144   52   63  144   12   93
            144
    datetime (unknown)

    body (0)

#### RECORD 88 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x72                                  .r
    decimal
              0  114
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-3.data: 89 records`
