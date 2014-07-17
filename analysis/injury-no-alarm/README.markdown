

## Injury, despite dosing large amounts of insulin, the NoDelivery alarm was absent

The following history comes straight from the pump where we can veryify the
absence of these alarms.

Here is a picture of the canula, it was completely bent over itself when I pull
it out.

![kinked canula profile](http://i.imgur.com/gvICsXM.png)
![kinked canula birds eye](http://i.imgur.com/lk0oBcc.png)

The insulin is not the problem because I dosed 6 units via syringe and
immediately observed the glucose levels dropping.

I wonder if Medtronic can explain under what circumstances the NoDelivery alarm
is designed to work.

#### RECORD 25 Rewind 2014-07-16T00:01:24 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-07-16T00:01:24)
    0000   0x58 0xc1 0x00 0x10 0x0e                   X....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 Prime 2014-07-16T00:03:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x18                   .....
    decimal
              3    0    0    0   24
    datetime (2014-07-16T00:03:30)
    0000   0x5e 0xc3 0x20 0x10 0x0e                   ^. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 Prime 2014-07-16T00:03:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2014-07-16T00:03:52)
    0000   0x74 0xc3 0x00 0x10 0x0e                   t....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 CalBGForPH 2014-07-16T00:10:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2014-07-16T00:10:24)
    0000   0x58 0xca 0x20 0x70 0x0e                   X. p.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 Ian3F 2014-07-16T00:10:24 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-07-16T00:10:24)
    0000   0x58 0xca 0x60 0x70 0x0e                   X.`p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 BolusWizard 2014-07-16T00:10:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2014-07-16T00:10:33)
    0000   0x61 0xca 0x00 0x10 0x0e                   a....
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x08 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             10   80   13   45  106    8    7    0
              0    0    0   15  125
    HOUR BITS: [1, 1, 0]
#### RECORD 31 Bolus 2014-07-16T00:10:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 0, 'programmed': 1.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2014-07-16T00:10:33)
    0000   0x61 0xca 0x40 0x10 0x0e                   a.@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BolusWizard 2014-07-16T01:26:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.8,
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
    datetime (2014-07-16T01:26:01)
    0000   0x41 0xda 0x01 0x10 0x0e                   A....
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0x00 0x30 0x00    ?P.-j.0.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             63   80   13   45  106    0   48    0
              0    0    0   48  125
    HOUR BITS: [1, 1, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x52 0x04                   \.<R.
    decimal
             92    5   60   82    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2014-07-16T01:26:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'duration': 0, 'programmed': 4.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2014-07-16T01:26:02)
    0000   0x42 0xda 0x41 0x10 0x0e                   B.A..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 Ian3F 2014-07-16T04:56:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x32                                  ?2
    decimal
             63   50
    datetime (2014-07-16T04:56:32)
    0000   0x60 0xf8 0xa4 0x70 0x0e                   `..p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2014-07-16T04:56:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 62,
 '_byte[7]': 0,
 'bg': 405,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x95                                  [.
    decimal
             91  149
    datetime (2014-07-16T04:56:43)
    0000   0x6b 0xf8 0x04 0x10 0x0e                   k....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3e 0x00 0x00    .Q.-j>..
    0008   0x00 0x05 0x00 0x39 0x7d                   ...9}
    decimal
              0   81   13   45  106   62    0    0
              0    5    0   57  125
    HOUR BITS: [1, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 212, 'amount': 4.8, 'curve': 4},
 {'age': 36, 'amount': 1.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0xd4 0x04 0x3c 0x24 0x14    \....<$.
    decimal
             92    8  192  212    4   60   36   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2014-07-16T04:56:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7, 'duration': 0, 'programmed': 5.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x39 0x39 0x00                        .99.
    decimal
              1   57   57    0
    datetime (2014-07-16T04:56:43)
    0000   0x6b 0xf8 0x44 0x10 0x0e                   k.D..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Ian3F 2014-07-16T09:06:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x37                                  ?7
    decimal
             63   55
    datetime (2014-07-16T09:06:04)
    0000   0x44 0xc6 0x89 0x70 0x0e                   D..p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 BolusWizard 2014-07-16T09:06:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 70,
 '_byte[7]': 0,
 'bg': 444,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.0,
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
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2014-07-16T09:06:16)
    0000   0x50 0xc6 0x09 0x10 0x0e                   P....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x46 0x00 0x00    .Q.-jF..
    0008   0x00 0x00 0x00 0x46 0x7d                   ...F}
    decimal
              0   81   13   45  106   70    0    0
              0    0    0   70  125
    HOUR BITS: [1, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 252, 'amount': 5.7, 'curve': 4},
 {'age': 206, 'amount': 4.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xe4 0xfc 0x04 0xc0 0xce 0x14    \.......
    decimal
             92    8  228  252    4  192  206   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2014-07-16T09:06:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.2, 'duration': 0, 'programmed': 7.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x48 0x48 0x00                        .HH.
    decimal
              1   72   72    0
    datetime (2014-07-16T09:06:17)
    0000   0x51 0xc6 0x49 0x10 0x0e                   Q.I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 TempBasal 2014-07-16T09:11:33 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2014-07-16T09:11:33)
    0000   0x61 0xcb 0x09 0x10 0x0e                   a....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 44 TempBasalDuration 2014-07-16T09:11:33 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2014-07-16T09:11:33)
    0000   0x61 0xcb 0x09 0x10 0x0e                   a....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BolusWizard 2014-07-16T09:45:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-16T09:45:27)
    0000   0x5b 0xed 0x09 0x10 0x0e                   [....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x00 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106    0    0    0
              0    0    0    0  125
    HOUR BITS: [1, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 0.8, 'curve': 5},
 {'age': 35, 'amount': 5.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x29 0x05 0xe4 0x23 0x14    \. )..#.
    decimal
             92    8   32   41    5  228   35   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2014-07-16T09:45:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'duration': 0, 'programmed': 0.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2014-07-16T09:45:27)
    0000   0x5b 0xed 0x49 0x10 0x0e                   [.I..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 Ian3F 2014-07-16T10:40:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x33                                  ?3
    decimal
             63   51
    datetime (2014-07-16T10:40:46)
    0000   0x6e 0xe8 0xea 0x70 0x0e                   n..p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2014-07-16T10:40:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 64,
 '_byte[7]': 0,
 'bg': 415,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 4.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2014-07-16T10:40:59)
    0000   0x7b 0xe8 0x0a 0x10 0x0e                   {....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x40 0x00 0x00    .Q.-j@..
    0008   0x00 0x31 0x00 0x0f 0x7d                   .1..}
    decimal
              0   81   13   45  106   64    0    0
              0   49    0   15  125
    HOUR BITS: [1, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.6, 'curve': 4},
 {'age': 96, 'amount': 0.8, 'curve': 5},
 {'age': 90, 'amount': 5.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0x38 0x04 0x20 0x60 0x05    \..8. `.
    0008   0xe4 0x5a 0x14                             .Z.
    decimal
             92   11   24   56    4   32   96    5
            228   90   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2014-07-16T10:40:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-16T10:40:59)
    0000   0x7b 0xe8 0x4a 0x10 0x0e                   {.J..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 BolusWizard 2014-07-16T10:42:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 64,
 '_byte[7]': 0,
 'bg': 415,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 7.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2014-07-16T10:42:58)
    0000   0x7a 0xea 0x0a 0x10 0x0e                   z....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x40 0x00 0x00    .Q.-j@..
    0008   0x00 0x4a 0x00 0x00 0x7d                   .J..}
    decimal
              0   81   13   45  106   64    0    0
              0   74    0    0  125
    HOUR BITS: [1, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 2.6, 'curve': 4},
 {'age': 58, 'amount': 0.6, 'curve': 4},
 {'age': 98, 'amount': 0.8, 'curve': 5},
 {'age': 92, 'amount': 5.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0x08 0x04 0x18 0x3a 0x04    \.h...:.
    0008   0x20 0x62 0x05 0xe4 0x5c 0x14               b..\.
    decimal
             92   14  104    8    4   24   58    4
             32   98    5  228   92   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2014-07-16T10:42:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-16T10:42:58)
    0000   0x7a 0xea 0x4a 0x10 0x0e                   z.J..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 55 Ian3F 2014-07-16T12:45:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x35                                  ?5
    decimal
             63   53
    datetime (2014-07-16T12:45:10)
    0000   0x4a 0xed 0x2c 0x70 0x0e                   J.,p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
`end m522-ReadHistoryData-page-0.data: 56 records`
## START m522-ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0xff                                  ..
##### DEBUG DECIMAL
              5  255
