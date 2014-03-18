## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 1005, found 17 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x5c 0xa5                                  \.
##### DEBUG DECIMAL
             92  165
#### RECORD 0 Bolus 2014-03-01T00:20:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x18 0x00    ........
    decimal
              1    0  144    0  144    0   24    0
    datetime (2014-03-01T00:20:06)
    0000   0x06 0xd4 0x40 0x61 0x0e                   ..@a.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 CalBGForPH 2014-03-01T00:53:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2014-03-01T00:53:06)
    0000   0x06 0xf5 0x20 0x61 0x0e                   .. a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2014-03-01T00:53:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-01T00:53:06)
    0000   0x06 0xf5 0x60 0x61 0x0e                   ..`a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BasalProfileStart 2014-03-01T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-01T02:00:00)
    0000   0x00 0xc0 0x02 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BasalProfileStart 2014-03-01T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-01T04:00:00)
    0000   0x00 0xc0 0x04 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BasalProfileStart 2014-03-01T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-01T06:00:00)
    0000   0x00 0xc0 0x06 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2014-03-01T08:36:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 342}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2014-03-01T08:36:51)
    0000   0x33 0xe4 0x28 0x61 0x8e                   3.(a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 Ian3F 2014-03-01T08:36:51 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2a                                  ?*
    decimal
             63   42
    datetime (2014-03-01T08:36:51)
    0000   0x33 0xe4 0xc8 0x61 0x0e                   3..a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2014-03-01T08:37:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 342,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 24.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2014-03-01T08:37:33)
    0000   0x21 0xe5 0x08 0x61 0x0e                   !..a.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x28 0x50 0xf0 0x00    .Q.n(P..
    0008   0x00 0x00 0x00 0x00 0x00 0xf0 0x64         ......d
    decimal
              0   81    0  110   40   80  240    0
              0    0    0    0    0  240  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2014-03-01T09:14:02 head[2], body[15] op[0x5b]
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
    datetime (2014-03-01T09:14:02)
    0000   0x02 0xce 0x09 0x61 0x0e                   ...a.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    -P.n(P..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x64         ......d
    decimal
             45   80    0  110   40   80    0    0
            160    0    0    0    0  160  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 Bolus 2014-03-01T09:14:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2014-03-01T09:14:02)
    0000   0x02 0xce 0x49 0x61 0x0e                   ..Ia.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 11 BolusWizard 2014-03-01T10:21:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T10:21:28)
    0000   0x1c 0xd5 0x0a 0x61 0x0e                   ...a.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    (P.n(P..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x64         ......d
    decimal
             40   80    0  110   40   80    0    0
            144    0    0    0    0  144  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 4.0, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0x45 0x80                   \..E.
    decimal
             92    5  160   69  128
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2014-03-01T10:21:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x3c 0x00    ......<.
    decimal
              1    0  144    0  144    0   60    0
    datetime (2014-03-01T10:21:28)
    0000   0x1c 0xd5 0x4a 0x61 0x0e                   ..Ja.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2014-03-01T10:24:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 307}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2014-03-01T10:24:37)
    0000   0x25 0xd8 0x2a 0x61 0x8e                   %.*a.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 Ian3F 2014-03-01T10:24:37 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x26                                  ?&
    decimal
             63   38
    datetime (2014-03-01T10:24:37)
    0000   0x25 0xd8 0x6a 0x61 0x0e                   %.ja.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 BasalProfileStart 2014-03-01T10:27:26 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-01T10:27:26)
    0000   0x1a 0xdb 0x0a 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 17 Prime 2014-03-01T10:27:16 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-03-01T10:27:16)
    0000   0x10 0xdb 0x0a 0x01 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 BasalProfileStart 2014-03-01T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-01T10:30:00)
    0000   0x00 0xde 0x0a 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 19 BasalProfileStart 2014-03-01T10:39:06 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-01T10:39:06)
    0000   0x06 0xe7 0x0a 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 20 Prime 2014-03-01T10:38:56 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-03-01T10:38:56)
    0000   0x38 0xe6 0x0a 0x01 0x0e                   8....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 LowBattery 2014-03-01T11:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2014-03-01T11:01:00)
    0000   0x00 0xc1 0x0b 0x01 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Battery 2014-03-01T11:25:48 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-01T11:25:48)
    0000   0x30 0xd9 0x0b 0x01 0x0e                   0....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 BasalProfileStart 2014-03-01T11:25:48 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-01T11:25:48)
    0000   0x30 0xd9 0x0b 0x01 0x0e                   0....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 24 Battery 2014-03-01T11:31:32 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-01T11:31:32)
    0000   0x20 0xdf 0x0b 0x01 0x0e                    ....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BasalProfileStart 2014-03-01T11:31:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-01T11:31:32)
    0000   0x20 0xdf 0x0b 0x01 0x0e                    ....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 TempBasal 2014-03-01T12:57:32 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-01T12:57:32)
    0000   0x20 0xf9 0x0c 0x01 0x0e                    ....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 27 TempBasalDuration 2014-03-01T12:57:32 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2014-03-01T12:57:32)
    0000   0x20 0xf9 0x0c 0x01 0x0e                    ....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 Battery 2014-03-01T13:27:58 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-01T13:27:58)
    0000   0x3a 0xdb 0x0d 0x01 0x0e                   :....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 Battery 2014-03-01T13:48:23 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2014-03-01T13:48:23)
    0000   0x17 0xf0 0x0d 0x01 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 Battery 2014-03-01T13:48:52 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-01T13:48:52)
    0000   0x34 0xf0 0x0d 0x01 0x0e                   4....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 NoDelivery 2014-03-01T13:48:23 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x37 0x06 0x87                        .7..
    decimal
              6   55    6  135
    datetime (2014-03-01T13:48:23)
    0000   0x17 0xf0 0x4d 0xa1 0x0e                   ..M..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 32 ClearAlarm 2014-03-01T13:54:17 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x37                                  .7
    decimal
             12   55
    datetime (2014-03-01T13:54:17)
    0000   0x11 0xf6 0x0d 0x01 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Battery 2014-03-01T16:34:37 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-01T16:34:37)
    0000   0x25 0xe2 0x10 0x01 0x0e                   %....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 Battery 2014-03-01T16:35:26 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2014-03-01T16:35:26)
    0000   0x1a 0xe3 0x10 0x01 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 Battery 2014-03-01T16:35:58 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-01T16:35:58)
    0000   0x3a 0xe3 0x10 0x01 0x0e                   :....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 BasalProfileStart 2014-03-01T16:35:58 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-01T16:35:58)
    0000   0x3a 0xe3 0x10 0x01 0x0e                   :....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 37 Bolus 2014-03-01T16:36:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x00 0x00    ........
    decimal
              1    0   20    0   20    0    0    0
    datetime (2014-03-01T16:36:56)
    0000   0x38 0xe4 0x50 0x01 0x0e                   8.P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BolusWizard 2014-03-01T17:15:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T17:15:43)
    0000   0x2b 0xcf 0x11 0x61 0x0e                   +..a.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x78 0x32 0x50 0x00 0x00    (P.x2P..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x64         ......d
    decimal
             40   80    0  120   50   80    0    0
            132    0    0    0    0  132  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 0.5, 'curve': 128},
 {'age': 157, 'amount': 2.85, 'curve': 144},
 {'age': 167, 'amount': 0.75, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x2b 0x80 0x72 0x9d 0x90    \..+.r..
    0008   0x1e 0xa7 0x90                             ...
    decimal
             92   11   20   43  128  114  157  144
             30  167  144
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2014-03-01T17:15:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x10 0x00    ........
    decimal
              1    0  132    0  132    0   16    0
    datetime (2014-03-01T17:15:43)
    0000   0x2b 0xcf 0x51 0x61 0x0e                   +.Qa.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2014-03-01T18:06:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T18:06:02)
    0000   0x02 0xc6 0x12 0x61 0x0e                   ...a.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80    0    0
            100    0    0    0    0  100  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 3.3, 'curve': 128},
 {'age': 94, 'amount': 0.5, 'curve': 128},
 {'age': 208, 'amount': 2.85, 'curve': 144},
 {'age': 218, 'amount': 0.75, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x36 0x80 0x14 0x5e 0x80    \..6..^.
    0008   0x72 0xd0 0x90 0x1e 0xda 0x90              r.....
    decimal
             92   14  132   54  128   20   94  128
            114  208  144   30  218  144
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2014-03-01T18:06:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x4c 0x00    ..d.d.L.
    decimal
              1    0  100    0  100    0   76    0
    datetime (2014-03-01T18:06:02)
    0000   0x02 0xc6 0x52 0x61 0x0e                   ..Ra.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 44 CalBGForPH 2014-03-01T18:35:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2014-03-01T18:35:25)
    0000   0x19 0xe3 0x32 0x61 0x0e                   ..2a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 Ian3F 2014-03-01T18:35:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2014-03-01T18:35:25)
    0000   0x19 0xe3 0xf2 0x61 0x0e                   ...a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2014-03-01T19:40:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T19:40:10)
    0000   0x0a 0xe8 0x13 0x61 0x0e                   ...a.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    #P.n2P..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x64         |....|d
    decimal
             35   80    0  110   50   80    0    0
            124    0    0    0    0  124  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 2.5, 'curve': 128},
 {'age': 148, 'amount': 3.3, 'curve': 128},
 {'age': 188, 'amount': 0.5, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x62 0x80 0x84 0x94 0x80    \.db....
    0008   0x14 0xbc 0x80                             ...
    decimal
             92   11  100   98  128  132  148  128
             20  188  128
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2014-03-01T19:40:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x10 0x00    ..|.|...
    decimal
              1    0  124    0  124    0   16    0
    datetime (2014-03-01T19:40:10)
    0000   0x0a 0xe8 0x53 0x61 0x0e                   ..Sa.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2014-03-01T19:48:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T19:48:04)
    0000   0x04 0xf0 0x13 0x61 0x0e                   ...a.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    #P.n2P..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x64         |....|d
    decimal
             35   80    0  110   50   80    0    0
            124    0    0    0    0  124  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.4, 'curve': 128},
 {'age': 16, 'amount': 2.7, 'curve': 128},
 {'age': 106, 'amount': 2.5, 'curve': 128},
 {'age': 156, 'amount': 3.3, 'curve': 128},
 {'age': 196, 'amount': 0.5, 'curve': 128}]
```
    op hex (17)
    0000   0x5c 0x11 0x10 0x06 0x80 0x6c 0x10 0x80    \....l..
    0008   0x64 0x6a 0x80 0x84 0x9c 0x80 0x14 0xc4    dj......
    0010   0x80                                       .
    decimal
             92   17   16    6  128  108   16  128
            100  106  128  132  156  128   20  196
            128
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2014-03-01T19:48:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x80 0x00    ..|.|...
    decimal
              1    0  124    0  124    0  128    0
    datetime (2014-03-01T19:48:05)
    0000   0x05 0xf0 0x53 0x61 0x0e                   ..Sa.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 BolusWizard 2014-03-01T21:00:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 0,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 80,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T21:00:29)
    0000   0x1d 0xc0 0x15 0x61 0x0e                   ...a.
    body (15)
    hex
    0000   0x50 0x50 0x00 0x6e 0x32 0x50 0x00 0x01    PP.n2P..
    0008   0x20 0x00 0x00 0x00 0x01 0x20 0x64          .... d
    decimal
             80   80    0  110   50   80    0    1
             32    0    0    0    1   32  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 3.5, 'curve': 128},
 {'age': 88, 'amount': 2.7, 'curve': 128},
 {'age': 178, 'amount': 2.5, 'curve': 128},
 {'age': 228, 'amount': 3.3, 'curve': 128},
 {'age': 12, 'amount': 0.5, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x8c 0x4e 0x80 0x6c 0x58 0x80    \..N.lX.
    0008   0x64 0xb2 0x80 0x84 0xe4 0x80 0x14 0x0c    d.......
    0010   0x90                                       .
    decimal
             92   17  140   78  128  108   88  128
            100  178  128  132  228  128   20   12
            144
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2014-03-01T21:03:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x3c 0x02    ..X.X.<.
    decimal
              1    0   88    0   88    0   60    2
    datetime (2014-03-01T21:03:49)
    0000   0x31 0xc3 0xb5 0x61 0x0e                   1..a.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 Bolus 2014-03-01T21:00:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 20.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x3c 0x00    ......<.
    decimal
              1    0  200    0  200    0   60    0
    datetime (2014-03-01T21:00:29)
    0000   0x1d 0xc0 0x95 0x61 0x0e                   ...a.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 BolusWizard 2014-03-01T21:42:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 50,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 180}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-01T21:42:49)
    0000   0x31 0xea 0x15 0x61 0x0e                   1..a.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    2P.n2P..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x64         ......d
    decimal
             50   80    0  110   50   80    0    0
            180    0    0    0    0  180  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 0.05, 'curve': 128},
 {'age': 10, 'amount': 0.35, 'curve': 128},
 {'age': 20, 'amount': 0.4, 'curve': 128},
 {'age': 30, 'amount': 0.35, 'curve': 128},
 {'age': 40, 'amount': 3.0, 'curve': 128},
 {'age': 50, 'amount': 2.3, 'curve': 128},
 {'age': 120, 'amount': 3.5, 'curve': 128},
 {'age': 130, 'amount': 2.7, 'curve': 128},
 {'age': 220, 'amount': 2.5, 'curve': 128},
 {'age': 14, 'amount': 3.3, 'curve': 144},
 {'age': 54, 'amount': 0.5, 'curve': 144}]
```
    op hex (35)
    0000   0x5c 0x23 0x02 0x00 0x80 0x0e 0x0a 0x80    \#......
    0008   0x10 0x14 0x80 0x0e 0x1e 0x80 0x78 0x28    ......x(
    0010   0x80 0x5c 0x32 0x80 0x8c 0x78 0x80 0x6c    .\2..x.l
    0018   0x82 0x80 0x64 0xdc 0x80 0x84 0x0e 0x90    ..d.....
    0020   0x14 0x36 0x90                             .6.
    decimal
             92   35    2    0  128   14   10  128
             16   20  128   14   30  128  120   40
            128   92   50  128  140  120  128  108
            130  128  100  220  128  132   14  144
             20   54  144
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2014-03-01T21:42:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0xbc 0x00    ........
    decimal
              1    0  180    0  180    0  188    0
    datetime (2014-03-01T21:42:49)
    0000   0x31 0xea 0x55 0x61 0x0e                   1.Ua.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 BasalProfileStart 2014-03-01T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-01T22:30:00)
    0000   0x00 0xde 0x16 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BasalProfileStart 2014-03-02T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-02T00:00:00)
    0000   0x00 0xc0 0x00 0x02 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 MResultTotals 2014-03-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x32                   ....2
    decimal
              7    0    0    7   50
    datetime (2014-03-02T00:00:00)
    0000   0x21 0x8e                                  !.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 62 Sara6E 2014-03-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-02T00:00:00)
    0000   0x21 0x8e                                  !.
    body (49)
    hex
    0000   0x05 0x10 0xeb 0x43 0x56 0x04 0x00 0x00    ...CV...
    0008   0x07 0x32 0x01 0xaa 0x17 0x05 0x88 0x4d    .2.....M
    0010   0x01 0x8b 0x05 0x74 0x00 0x00 0x00 0x00    ...t....
    0018   0x00 0x14 0x09 0x00 0x00 0x01 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  235   67   86    4    0    0
              7   50    1  170   23    5  136   77
              1  139    5  116    0    0    0    0
              0   20    9    0    0    1    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 63 BasalProfileStart 2014-03-02T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-02T02:00:00)
    0000   0x00 0xc0 0x02 0x02 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 64 BasalProfileStart 2014-03-02T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-02T04:00:00)
    0000   0x00 0xc0 0x04 0x02 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 65 CalBGForPH 2014-03-02T04:24:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 197}
```
    op hex (2)
    0000   0x0a 0xc5                                  ..
    decimal
             10  197
    datetime (2014-03-02T04:24:21)
    0000   0x15 0xd8 0x24 0x62 0x0e                   ..$b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 Ian3F 2014-03-02T04:24:21 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2014-03-02T04:24:21)
    0000   0x15 0xd8 0xa4 0x62 0x0e                   ...b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 67 BolusWizard 2014-03-02T04:24:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 197,
 'bg_target_high': 0,
 'bg_target_low': 30,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 12.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc5                                  [.
    decimal
             91  197
    datetime (2014-03-02T04:24:38)
    0000   0x26 0xd8 0x04 0x02 0x0e                   &....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x80 0x00    .P.n.P..
    0008   0x00 0x00 0x00 0x00 0x00 0x80 0x64         ......d
    decimal
              0   80    0  110   30   80  128    0
              0    0    0    0    0  128  100
    HOUR BITS: [1, 1, 0]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 0.15, 'curve': 144},
 {'age': 136, 'amount': 0.35, 'curve': 144},
 {'age': 146, 'amount': 4.8, 'curve': 144},
 {'age': 156, 'amount': 0.35, 'curve': 144},
 {'age': 166, 'amount': 0.4, 'curve': 144},
 {'age': 176, 'amount': 0.35, 'curve': 144},
 {'age': 186, 'amount': 3.0, 'curve': 144},
 {'age': 196, 'amount': 2.3, 'curve': 144}]
```
    op hex (26)
    0000   0x5c 0x1a 0x06 0x7e 0x90 0x0e 0x88 0x90    \..~....
    0008   0xc0 0x92 0x90 0x0e 0x9c 0x90 0x10 0xa6    ........
    0010   0x90 0x0e 0xb0 0x90 0x78 0xba 0x90 0x5c    ....x..\
    0018   0xc4 0x90                                  ..
    decimal
             92   26    6  126  144   14  136  144
            192  146  144   14  156  144   16  166
            144   14  176  144  120  186  144   92
            196  144
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2014-03-02T04:24:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x00 0x00    ........
    decimal
              1    0  140    0  140    0    0    0
    datetime (2014-03-02T04:24:38)
    0000   0x26 0xd8 0x44 0x02 0x0e                   &.D..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 BasalProfileStart 2014-03-02T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-02T06:00:00)
    0000   0x00 0xc0 0x06 0x02 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 71 CalBGForPH 2014-03-02T09:08:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2014-03-02T09:08:09)
    0000   0x09 0xc8 0x29 0x02 0x0e                   ..)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 BolusWizard 2014-03-02T09:08:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 183,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 8.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb7                                  [.
    decimal
             91  183
    datetime (2014-03-02T09:08:16)
    0000   0x10 0xc8 0x09 0x62 0x0e                   ...b.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x50 0x00    .P.n(PP.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x64         .....Pd
    decimal
              0   80    0  110   40   80   80    0
              0    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 3.5, 'curve': 144}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x1e 0x90                   \....
    decimal
             92    5  140   30  144
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2014-03-02T09:08:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2014-03-02T09:08:16)
    0000   0x10 0xc8 0x49 0x62 0x0e                   ..Ib.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 75 BolusWizard 2014-03-02T09:57:51 head[2], body[15] op[0x5b]
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
    datetime (2014-03-02T09:57:51)
    0000   0x33 0xf9 0x09 0x62 0x0e                   3..b.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    -P.n(P..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x64         ......d
    decimal
             45   80    0  110   40   80    0    0
            160    0    0    0    0  160  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 2.0, 'curve': 128},
 {'age': 79, 'amount': 3.5, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x37 0x80 0x8c 0x4f 0x90    \.P7..O.
    decimal
             92    8   80   55  128  140   79  144
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2014-03-02T09:57:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x2c 0x00    ......,.
    decimal
              1    0  160    0  160    0   44    0
    datetime (2014-03-02T09:57:51)
    0000   0x33 0xf9 0x49 0x62 0x0e                   3.Ib.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-11.data: 78 records`
