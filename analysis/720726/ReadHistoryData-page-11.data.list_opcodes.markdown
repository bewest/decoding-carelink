## START analysis/ianj/raw/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x11 0x94                                  ..
##### DEBUG DECIMAL
             17  148
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 2.7, 'curve': 4},
 {'age': 49, 'amount': 0.1, 'curve': 20},
 {'age': 59, 'amount': 3.2, 'curve': 20},
 {'age': 69, 'amount': 3.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0x9b 0x04 0x04 0x31 0x14    \.l...1.
    0008   0x80 0x3b 0x14 0x8c 0x45 0x14              .;..E.
    decimal
             92   14  108  155    4    4   49   20
            128   59   20  140   69   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-08-29T00:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x04 0x00 0x04 0x00 0x20 0x00    ...... .
    decimal
              1    0    4    0    4    0   32    0
    datetime (2012-08-29T00:19:46)
    0000   0xae 0x13 0x40 0x7d 0x0c                   ..@}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 2 Rewind 2012-08-29T00:36:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-29T00:36:04)
    0000   0x84 0x24 0x00 0x1d 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 Prime 2012-08-29T00:37:24 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2b                   ....+
    decimal
              3    0    0    0   43
    datetime (2012-08-29T00:37:24)
    0000   0x98 0x25 0x20 0x1d 0x0c                   .% ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BasalProfileStart 2012-08-29T00:37:39 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-29T00:37:39)
    0000   0xa7 0x25 0x00 0x1d 0x0c                   .%...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2012-08-29T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-29T04:00:00)
    0000   0x80 0x00 0x04 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 6 CalBGForPH 2012-08-29T07:55:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2012-08-29T07:55:42)
    0000   0xaa 0x37 0x27 0x7d 0x0c                   .7'}.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2012-08-29T07:55:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2012-08-29T07:55:42)
    0000   0xaa 0x37 0xa7 0x7d 0x0c                   .7.}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 LowBattery 2012-08-29T08:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-08-29T08:01:00)
    0000   0x80 0x01 0x08 0x1d 0x0c                   .....
    body (0)

#### RECORD 9 BasalProfileStart 2012-08-29T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-29T09:30:00)
    0000   0x80 0x1e 0x09 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 10 LowBattery 2012-08-29T10:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-08-29T10:01:00)
    0000   0x80 0x01 0x0a 0x1d 0x0c                   .....
    body (0)

#### RECORD 11 CalBGForPH 2012-08-29T10:13:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2012-08-29T10:13:23)
    0000   0x97 0x0d 0x2a 0x7d 0x0c                   ..*}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2012-08-29T10:13:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2012-08-29T10:13:23)
    0000   0x97 0x0d 0x2a 0x7d 0x0c                   ..*}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2012-08-29T10:13:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 98,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 7.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2012-08-29T10:13:27)
    0000   0x9b 0x0d 0x0a 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x4c 0x00    ...n.6L.
    0008   0x00 0x00 0x00 0x00 0x00 0x4c 0x36         .....L6
    decimal
              0  144    0  110   23   54   76    0
              0    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 14 Ian69 2012-08-29T10:13:27 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-29T10:13:27)
    0000   0x9b 0x0d 0x0a 0x1d 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 15 Bolus 2012-08-29T10:13:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x00 0x00    ..L.L...
    decimal
              1    0   76    0   76    0    0    0
    datetime (2012-08-29T10:13:27)
    0000   0x9b 0x0d 0x4a 0x7d 0x0c                   ..J}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 16 BasalProfileStart 2012-08-29T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-29T13:00:00)
    0000   0x80 0x00 0x0d 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 17 BolusWizard 2012-08-29T13:07:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 34,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-29T13:07:04)
    0000   0x84 0x07 0x0d 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x22 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    "..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             34  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 1.1, 'curve': 4},
 {'age': 183, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0xad 0x04 0x20 0xb7 0x04    \.,.. ..
    decimal
             92    8   44  173    4   32  183    4
    datetime (unknown)

    body (0)

#### RECORD 19 Ian69 2012-08-29T13:07:04 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-29T13:07:04)
    0000   0x84 0x07 0x0d 0x1d 0x0c                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 20 Bolus 2012-08-29T13:07:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x10 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   16    0
    datetime (2012-08-29T13:07:04)
    0000   0x84 0x07 0x4d 0x7d 0x0c                   ..M}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 21 CalBGForPH 2012-08-29T15:12:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 278}
```
    op hex (2)
    0000   0x0a 0x16                                  ..
    decimal
             10   22
    datetime (2012-08-29T15:12:03)
    0000   0x83 0x0c 0x2f 0x7d 0x8c                   ../}.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 22 Ian3F 2012-08-29T15:12:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2012-08-29T15:12:03)
    0000   0x83 0x0c 0xcf 0x7d 0x0c                   ...}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 23 CalBGForPH 2012-08-29T15:12:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2012-08-29T15:12:06)
    0000   0x86 0x0c 0x4f 0xdd 0x0c                   ..O..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 24 BolusWizard 2012-08-29T15:12:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 155,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 17.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2012-08-29T15:12:08)
    0000   0x88 0x0c 0x0f 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xac 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x34 0x00 0x78 0x36         ...4.x6
    decimal
              0  144    0  110   23   54  172    0
              0    0    0   52    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 128, 'amount': 3.0, 'curve': 4},
 {'age': 42, 'amount': 1.1, 'curve': 20},
 {'age': 52, 'amount': 0.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x78 0x80 0x04 0x2c 0x2a 0x14    \.x..,*.
    0008   0x20 0x34 0x14                              4.
    decimal
             92   11  120  128    4   44   42   20
             32   52   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2012-08-29T15:12:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x34 0x00    ..x.x.4.
    decimal
              1    0  120    0  120    0   52    0
    datetime (2012-08-29T15:12:08)
    0000   0x88 0x0c 0x4f 0x7d 0x0c                   ..O}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 27 BolusWizard 2012-08-29T19:22:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 38,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 136}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-29T19:22:06)
    0000   0x86 0x16 0x13 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x26 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    &..n.6..
    0008   0x88 0x00 0x00 0x00 0x00 0x88 0x36         ......6
    decimal
             38  144    0  110   23   54    0    0
            136    0    0    0    0  136   54
    DAY BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 248, 'amount': 0.25, 'curve': 4},
 {'age': 2, 'amount': 2.75, 'curve': 20},
 {'age': 122, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0a 0xf8 0x04 0x6e 0x02 0x14    \....n..
    0008   0x78 0x7a 0x14                             xz.
    decimal
             92   11   10  248    4  110    2   20
            120  122   20
    datetime (unknown)

    body (0)

#### RECORD 29 Ian69 2012-08-29T19:22:06 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-29T19:22:06)
    0000   0x86 0x16 0x73 0x1d 0x0c                   ..s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 30 Bolus 2012-08-29T19:22:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x00 0x00    ........
    decimal
              1    0  136    0  136    0    0    0
    datetime (2012-08-29T19:22:06)
    0000   0x86 0x16 0x53 0x7d 0x0c                   ..S}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2012-08-29T20:56:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-29T20:56:25)
    0000   0x99 0x38 0x14 0x7d 0x0c                   .8.}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 0.65, 'curve': 4},
 {'age': 102, 'amount': 2.75, 'curve': 4},
 {'age': 86, 'amount': 0.25, 'curve': 20},
 {'age': 96, 'amount': 2.75, 'curve': 20},
 {'age': 216, 'amount': 3.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x1a 0x5c 0x04 0x6e 0x66 0x04    \..\.nf.
    0008   0x0a 0x56 0x14 0x6e 0x60 0x14 0x78 0xd8    .V.n`.x.
    0010   0x14                                       .
    decimal
             92   17   26   92    4  110  102    4
             10   86   20  110   96   20  120  216
             20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2012-08-29T20:56:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x50 0x00    ..H.H.P.
    decimal
              1    0   72    0   72    0   80    0
    datetime (2012-08-29T20:56:26)
    0000   0x9a 0x38 0x54 0x7d 0x0c                   .8T}.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2012-08-29T22:06:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-29T22:06:07)
    0000   0x87 0x06 0x16 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x0c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x36         (....(6
    decimal
             12  144    0  110   23   54    0    0
             40    0    0    0    0   40   54
    DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 1.8, 'curve': 4},
 {'age': 162, 'amount': 0.65, 'curve': 4},
 {'age': 172, 'amount': 2.75, 'curve': 4},
 {'age': 156, 'amount': 0.25, 'curve': 20},
 {'age': 166, 'amount': 2.75, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x48 0x04 0x1a 0xa2 0x04    \.HH....
    0008   0x6e 0xac 0x04 0x0a 0x9c 0x14 0x6e 0xa6    n.....n.
    0010   0x14                                       .
    decimal
             92   17   72   72    4   26  162    4
            110  172    4   10  156   20  110  166
             20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2012-08-29T22:06:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x54 0x00    ..(.(.T.
    decimal
              1    0   40    0   40    0   84    0
    datetime (2012-08-29T22:06:08)
    0000   0x88 0x06 0x56 0x7d 0x0c                   ..V}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2012-08-30T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-30T00:00:00)
    0000   0x80 0x00 0x00 0x1e 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 38 MResultTotals 2012-08-30T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xc0                   .....
    decimal
              7    0    0    5  192
    datetime (2012-08-30T00:00:00)
    0000   0x9d 0x0c                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 39 Sara6E 2012-08-30T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2012-08-30T00:00:00)
    0000   0x9d 0x0c                                  ..
    body (49)
    hex
    0000   0x06 0x50 0xb8 0x35 0x16 0x05 0x00 0x00    .P.5....
    0008   0x05 0xc0 0x03 0x88 0x3d 0x02 0x38 0x27    ....=.8'
    0010   0x00 0x68 0x01 0x70 0x00 0xc8 0x00 0x00    .h.p....
    0018   0x00 0x00 0x04 0x03 0x00 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x17    ........
    0028   0x17 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6   80  184   53   22    5    0    0
              5  192    3  136   61    2   56   39
              0  104    1  112    0  200    0    0
              0    0    4    3    0    0    4    0
              0    0    0    0    0    0    0   23
             23    0    0    0    0    0    0    0
              0

#### RECORD 40 BasalProfileStart 2012-08-30T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-30T04:00:00)
    0000   0x80 0x00 0x04 0x1e 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 41 Bolus 2012-08-30T04:45:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2012-08-30T04:45:37)
    0000   0xa5 0x2d 0x44 0x7e 0x0c                   .-D~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BasalProfileStart 2012-08-30T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-30T09:30:00)
    0000   0x80 0x1e 0x09 0x1e 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 43 LowBattery 2012-08-30T10:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-08-30T10:01:00)
    0000   0x80 0x01 0x0a 0x1e 0x0c                   .....
    body (0)

#### RECORD 44 Ian69 2012-08-30T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-30T10:30:00)
    0000   0x80 0x1e 0x0a 0x1e 0x0c                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 45 CalBGForPH 2012-08-30T11:25:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 59}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2012-08-30T11:25:08)
    0000   0x88 0x19 0x2b 0x7e 0x0c                   ..+~.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2012-08-30T11:25:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2012-08-30T11:25:08)
    0000   0x88 0x19 0x6b 0x7e 0x0c                   ..k~.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2012-08-30T11:43:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-30T11:43:42)
    0000   0xaa 0x2b 0x0b 0x7e 0x0c                   .+.~.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 163, 'amount': 1.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0xa3 0x14                   \.@..
    decimal
             92    5   64  163   20
    datetime (unknown)

    body (0)

#### RECORD 49 Ian69 2012-08-30T11:43:42 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-30T11:43:42)
    0000   0xaa 0x2b 0x0b 0x1e 0x0c                   .+...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 50 Bolus 2012-08-30T11:43:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2012-08-30T11:43:42)
    0000   0xaa 0x2b 0x4b 0x7e 0x0c                   .+K~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2012-08-30T11:55:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-30T11:55:15)
    0000   0x8f 0x37 0x0b 0x7e 0x0c                   .7.~.
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x36         D....D6
    decimal
             19  144    0  110   23   54    0    0
             68    0    0    0    0   68   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.75, 'curve': 4},
 {'age': 21, 'amount': 0.45, 'curve': 4},
 {'age': 175, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x46 0x0b 0x04 0x12 0x15 0x04    \.F.....
    0008   0x40 0xaf 0x14                             @..
    decimal
             92   11   70   11    4   18   21    4
             64  175   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2012-08-30T11:55:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x58 0x00    ..D.D.X.
    decimal
              1    0   68    0   68    0   88    0
    datetime (2012-08-30T11:55:15)
    0000   0x8f 0x37 0x4b 0x7e 0x0c                   .7K~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 BasalProfileStart 2012-08-30T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-30T13:00:00)
    0000   0x80 0x00 0x0d 0x1e 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 55 CalBGForPH 2012-08-30T14:52:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2012-08-30T14:52:12)
    0000   0x8c 0x34 0x4e 0x1e 0x0c                   .4N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 BolusWizard 2012-08-30T14:52:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 85,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.8,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2012-08-30T14:52:18)
    0000   0x92 0x34 0x0e 0x7e 0x0c                   .4.~.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    ...n.64.
    0008   0x6c 0x00 0x00 0x1c 0x00 0x84 0x36         l.....6
    decimal
             30  144    0  110   23   54   52    0
            108    0    0   28    0  132   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 178, 'amount': 1.7, 'curve': 4},
 {'age': 188, 'amount': 1.75, 'curve': 4},
 {'age': 198, 'amount': 0.45, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0xb2 0x04 0x46 0xbc 0x04    \.D..F..
    0008   0x12 0xc6 0x04                             ...
    decimal
             92   11   68  178    4   70  188    4
             18  198    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2012-08-30T14:52:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x1c 0x00    ........
    decimal
              1    0  132    0  132    0   28    0
    datetime (2012-08-30T14:52:18)
    0000   0x92 0x34 0x4e 0x7e 0x0c                   .4N~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 CalBGForPH 2012-08-30T15:33:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2012-08-30T15:33:55)
    0000   0xb7 0x21 0x4f 0x1e 0x0c                   .!O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 Battery 2012-08-30T15:58:40 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2012-08-30T15:58:40)
    0000   0xa8 0x3a 0x0f 0x1e 0x0c                   .:...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x15 0x03 0x62                        ...b
    decimal
              6   21    3   98
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x60 0x01 0x08                   .@`..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x11 0x04 0x08                        ....
    decimal
              6   17    4    8
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x08                   .@@..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 63 ClearAlarm 2008-01-01T00:04:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x15                                  ..
    decimal
             12   21
    datetime (2008-01-01T00:04:06)
    0000   0x06 0x44 0x00 0x01 0x08                   .D...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 64 ChangeTimeDisplay 2008-01-01T00:00:10 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x01                                  d.
    decimal
            100    1
    datetime (2008-01-01T00:00:10)
    0000   0x0a 0x40 0x00 0x01 0x08                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 65 ChangeTime 2008-01-01T00:00:38 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2008-01-01T00:00:38)
    0000   0x26 0x40 0x00 0x01 0x08                   &@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 66 NewTimeSet 2013-08-30T16:05:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-08-30T16:05:00)
    0000   0x80 0x05 0x10 0x1e 0x0d                   .....
    body (0)

#### RECORD 67 MResultTotals 2008-01-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2008-01-02T00:00:00)
    0000   0x01 0x88                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 68 Sara6E 2008-01-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2008-01-02T00:00:00)
    0000   0x01 0x88                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 69 Rewind 2013-08-30T16:05:02 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-30T16:05:02)
    0000   0x82 0x05 0x10 0x1e 0x0d                   .....
    body (0)

#### RECORD 70 Prime 2013-08-30T16:05:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2013-08-30T16:05:18)
    0000   0x92 0x05 0x30 0x1e 0x0d                   ..0..
    body (0)

#### RECORD 71 BasalProfileStart 2013-08-30T16:05:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-30T16:05:32)
    0000   0xa0 0x05 0x10 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 72 BolusWizard 2013-08-30T18:50:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-30T18:50:07)
    0000   0x87 0x32 0x12 0x7e 0x0d                   .2.~.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 Ian69 2013-08-30T18:50:07 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-30T18:50:07)
    0000   0x87 0x32 0x72 0x1e 0x0d                   .2r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 74 Bolus 2013-08-30T18:50:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2013-08-30T18:50:07)
    0000   0x87 0x32 0x52 0x7e 0x0d                   .2R~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 BolusWizard 2013-08-30T18:54:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-08-30T18:54:51)
    0000   0xb3 0x36 0x12 0x7e 0x0d                   .6.~.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 0.5, 'curve': 4}, {'age': 13, 'amount': 1.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x03 0x04 0x34 0x0d 0x04    \....4..
    decimal
             92    8   20    3    4   52   13    4
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-08-30T18:54:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x48 0x00    ......H.
    decimal
              1    0  168    0  168    0   72    0
    datetime (2013-08-30T18:54:51)
    0000   0xb3 0x36 0x52 0x7e 0x0d                   .6R~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 78 BolusWizard 2013-08-30T21:05:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-08-30T21:05:53)
    0000   0xb5 0x05 0x15 0x7e 0x0d                   ...~.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    DAY BITS: [0, 1, 1]
#### RECORD 79 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 134, 'amount': 4.7, 'curve': 4},
 {'age': 144, 'amount': 1.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xbc 0x86 0x04 0x34 0x90 0x04    \....4..
    decimal
             92    8  188  134    4   52  144    4
    datetime (unknown)

    body (0)

`end analysis/ianj/raw/ReadHistoryData-page-11.data: 80 records`
