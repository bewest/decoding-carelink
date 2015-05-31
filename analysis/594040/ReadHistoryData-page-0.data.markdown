## START analysis/594040/logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 185, found 837 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4f 0xd2                                  O.
##### DEBUG DECIMAL
             79  210
#### RECORD 0 SensorAlert 2015-05-30T15:26:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-05-30T15:26:10)
    0000   0x4a 0x5a 0x2f 0xbe 0x0f                   JZ/..
    body (0)

#### RECORD 1 BolusWizard 2015-05-30T15:26:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-30T15:26:26)
    0000   0x5a 0x5a 0x0f 0x7e 0x0f                   ZZ.~.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0   80   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 2 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 168, 'amount': 3.8},
 {'age': 258, 'amount': 1.95},
 {'age': 268, 'amount': 2.45},
 {'age': 278, 'amount': 1.9}]
```
    op hex (14)
    0000   0x5c 0x0e 0x98 0xa8 0x04 0x4e 0x02 0x14    \....N..
    0008   0x62 0x0c 0x14 0x4c 0x16 0x14              b..L..
    decimal
             92   14  152  168    4   78    2   20
             98   12   20   76   22   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2015-05-30T15:26:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x24 0x00    ..(.(.$.
    decimal
              1    0   40    0   40    0   36    0
    datetime (2015-05-30T15:26:26)
    0000   0x5a 0x5a 0x4f 0x7e 0x0f                   ZZO~.
    body (0)

#### RECORD 4 BolusWizard 2015-05-30T16:29:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.6,
 'carb_input': 21,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-30T16:29:11)
    0000   0x4b 0x5d 0x10 0x7e 0x0f                   K].~.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x78         h....hx
    decimal
             21   80    0   80   40   90    0    0
            104    0    0    0    0  104  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 1.0},
 {'age': 231, 'amount': 3.8},
 {'age': 321, 'amount': 1.95},
 {'age': 331, 'amount': 2.45},
 {'age': 341, 'amount': 1.9}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x47 0x04 0x98 0xe7 0x04    \.(G....
    0008   0x4e 0x41 0x14 0x62 0x4b 0x14 0x4c 0x55    NA.bK.LU
    0010   0x14                                       .
    decimal
             92   17   40   71    4  152  231    4
             78   65   20   98   75   20   76   85
             20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-05-30T16:29:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6,
 'duration': 0,
 'programmed': 2.6,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x28 0x00    ..h.h.(.
    decimal
              1    0  104    0  104    0   40    0
    datetime (2015-05-30T16:29:11)
    0000   0x4b 0x5d 0x50 0x7e 0x0f                   K]P~.
    body (0)

#### RECORD 7 SensorAlert 2015-05-30T16:55:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 190}
```
    op hex (3)
    0000   0x0b 0x65 0xbe                             .e.
    decimal
             11  101  190
    datetime (2015-05-30T16:55:51)
    0000   0x73 0x77 0x30 0xbe 0x0f                   sw0..
    body (0)

#### RECORD 8 JournalEntryMealMarker 2015-05-30T17:24:12 head[2], body[2] op[0x40]
###### DECODED
```python
{'carb_input': 1}
```
    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime (2015-05-30T17:24:12)
    0000   0x4c 0x58 0x11 0x1e 0x0f                   LX...
    body (2)
    hex
    0000   0x01 0x01                                  ..
    decimal
              1    1

#### RECORD 9 BolusWizard 2015-05-30T17:25:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-30T17:25:33)
    0000   0x61 0x59 0x11 0x7e 0x0f                   aY.~.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0   80   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 10 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 2.6},
 {'age': 127, 'amount': 1.0},
 {'age': 287, 'amount': 3.8},
 {'age': 377, 'amount': 1.95},
 {'age': 387, 'amount': 2.45},
 {'age': 397, 'amount': 1.9}]
```
    op hex (20)
    0000   0x5c 0x14 0x68 0x39 0x04 0x28 0x7f 0x04    \.h9.(..
    0008   0x98 0x1f 0x14 0x4e 0x79 0x14 0x62 0x83    ...Ny.b.
    0010   0x14 0x4c 0x8d 0x14                        .L..
    decimal
             92   20  104   57    4   40  127    4
            152   31   20   78  121   20   98  131
             20   76  141   20
    datetime (unknown)

    body (0)

#### RECORD 11 TempBasal 2015-05-30T17:40:59 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 90, 'temp': 'percent'}
```
    op hex (2)
    0000   0x33 0x5a                                  3Z
    decimal
             51   90
    datetime (2015-05-30T17:40:59)
    0000   0x7b 0x68 0x11 0x1e 0x0f                   {h...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 12 TempBasalDuration 2015-05-30T17:40:59 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 30}
```
    op hex (2)
    0000   0x16 0x01                                  ..
    decimal
             22    1
    datetime (2015-05-30T17:40:59)
    0000   0x7b 0x68 0x11 0x1e 0x0f                   {h...
    body (0)

`end analysis/594040/logs/ReadHistoryData-page-0.data: 13 records`
