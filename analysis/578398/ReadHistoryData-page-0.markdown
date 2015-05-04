## START ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 181, found 841 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdf 0xe8                                  ..
##### DEBUG DECIMAL
            223  232
#### RECORD 0 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 204, 'amount': 0.15, 'curve': 4},
 {'age': 214, 'amount': 0.15, 'curve': 4},
 {'age': 224, 'amount': 0.15, 'curve': 4},
 {'age': 234, 'amount': 2.6, 'curve': 4},
 {'age': 244, 'amount': 0.15, 'curve': 4},
 {'age': 254, 'amount': 0.15, 'curve': 4},
 {'age': 8, 'amount': 0.2, 'curve': 20},
 {'age': 18, 'amount': 0.15, 'curve': 20},
 {'age': 28, 'amount': 0.15, 'curve': 20},
 {'age': 38, 'amount': 0.2, 'curve': 20},
 {'age': 48, 'amount': 0.15, 'curve': 20},
 {'age': 58, 'amount': 0.15, 'curve': 20},
 {'age': 68, 'amount': 4.05, 'curve': 20},
 {'age': 208, 'amount': 1.8, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x06 0xcc 0x04 0x06 0xd6 0x04    \,......
    0008   0x06 0xe0 0x04 0x68 0xea 0x04 0x06 0xf4    ...h....
    0010   0x04 0x06 0xfe 0x04 0x08 0x08 0x14 0x06    ........
    0018   0x12 0x14 0x06 0x1c 0x14 0x08 0x26 0x14    ......&.
    0020   0x06 0x30 0x14 0x06 0x3a 0x14 0xa2 0x44    .0..:..D
    0028   0x14 0x48 0xd0 0x14                        .H..
    decimal
             92   44    6  204    4    6  214    4
              6  224    4  104  234    4    6  244
              4    6  254    4    8    8   20    6
             18   20    6   28   20    8   38   20
              6   48   20    6   58   20  162   68
             20   72  208   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-04-29T17:03:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-29T17:03:32)
    0000   0x60 0x03 0x51 0x1d 0x0f                   `.Q..
    body (0)

#### RECORD 2 SensorAlert 2015-04-29T17:28:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 42}
```
    op hex (3)
    0000   0x0b 0x65 0x2a                             .e*
    decimal
             11  101   42
    datetime (2015-04-29T17:28:17)
    0000   0x51 0x1c 0x31 0xbd 0x8f                   Q.1..
    body (0)

#### RECORD 3 CalBGForPH 2015-04-29T17:40:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2015-04-29T17:40:56)
    0000   0x78 0x28 0x31 0x7d 0x0f                   x(1}.
    body (0)

#### RECORD 4 BGReceived 2015-04-29T17:40:56 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2015-04-29T17:40:56)
    0000   0x78 0x28 0x11 0x7d 0x0f                   x(.}.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 5 BolusWizard 2015-04-29T17:41:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2015-04-29T17:41:08)
    0000   0x48 0x29 0x11 0x1d 0x0f                   H)...
    body (13)
    hex
    0000   0x00 0x50 0x08 0x28 0x5a 0x18 0x00 0x00    .P.(Z...
    0008   0x00 0x1c 0x00 0x00 0x78                   ....x
    decimal
              0   80    8   40   90   24    0    0
              0   28    0    0  120

#### RECORD 6 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 3.0, 'curve': 4},
 {'age': 242, 'amount': 0.15, 'curve': 4},
 {'age': 252, 'amount': 0.15, 'curve': 4},
 {'age': 6, 'amount': 0.15, 'curve': 20},
 {'age': 16, 'amount': 2.6, 'curve': 20},
 {'age': 26, 'amount': 0.15, 'curve': 20},
 {'age': 36, 'amount': 0.15, 'curve': 20},
 {'age': 46, 'amount': 0.2, 'curve': 20},
 {'age': 56, 'amount': 0.15, 'curve': 20},
 {'age': 66, 'amount': 0.15, 'curve': 20},
 {'age': 76, 'amount': 0.2, 'curve': 20},
 {'age': 86, 'amount': 0.15, 'curve': 20},
 {'age': 96, 'amount': 0.15, 'curve': 20},
 {'age': 106, 'amount': 4.05, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x78 0x2a 0x04 0x06 0xf2 0x04    \,x*....
    0008   0x06 0xfc 0x04 0x06 0x06 0x14 0x68 0x10    ......h.
    0010   0x14 0x06 0x1a 0x14 0x06 0x24 0x14 0x08    .....$..
    0018   0x2e 0x14 0x06 0x38 0x14 0x06 0x42 0x14    ...8..B.
    0020   0x08 0x4c 0x14 0x06 0x56 0x14 0x06 0x60    .L..V..`
    0028   0x14 0xa2 0x6a 0x14                        ..j.
    decimal
             92   44  120   42    4    6  242    4
              6  252    4    6    6   20  104   16
             20    6   26   20    6   36   20    8
             46   20    6   56   20    6   66   20
              8   76   20    6   86   20    6   96
             20  162  106   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2015-04-29T17:41:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'duration': 0, 'programmed': 1.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2015-04-29T17:41:08)
    0000   0x48 0x29 0x51 0x1d 0x0f                   H)Q..
    body (0)

#### RECORD 8 PumpSuspend 2015-04-29T18:32:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-29T18:32:33)
    0000   0x61 0x20 0x12 0x5d 0x0f                   a .].
    body (0)

#### RECORD 9 PumpResume 2015-04-29T18:34:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-29T18:34:23)
    0000   0x57 0x22 0x12 0x5d 0x0f                   W".].
    body (0)

#### RECORD 10 PumpSuspend 2015-04-29T20:08:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-29T20:08:05)
    0000   0x45 0x08 0x14 0x5d 0x0f                   E..].
    body (0)

#### RECORD 11 PumpResume 2015-04-29T20:12:36 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-29T20:12:36)
    0000   0x64 0x0c 0x14 0x5d 0x0f                   d..].
    body (0)

`end ReadHistoryData-page-0.data: 12 records`
