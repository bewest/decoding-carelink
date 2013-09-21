## START analysis/ianj/raw/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc3 0xfd                                  ..
##### DEBUG DECIMAL
            195  253
#### RECORD 0 CalBGForPH 2013-08-01T08:32:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-01T08:32:07)
    0000   0x87 0x20 0x28 0x61 0x0d                   . (a.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Ian3F 2013-08-01T08:32:07 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2013-08-01T08:32:07)
    0000   0x87 0x20 0x88 0x61 0x0d                   . .a.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-08-01T08:32:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2013-08-01T08:32:23)
    0000   0x97 0x20 0x08 0x61 0x0d                   . .a.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 Ian69 2013-08-01T08:32:23 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-01T08:32:23)
    0000   0x97 0x20 0x08 0x01 0x0d                   . ...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 4 Bolus 2013-08-01T08:32:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2013-08-01T08:32:23)
    0000   0x97 0x20 0x48 0x61 0x0d                   . Ha.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 BasalProfileStart 2013-08-01T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-01T09:30:00)
    0000   0x80 0x1e 0x09 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 6 CalBGForPH 2013-08-01T11:07:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-08-01T11:07:50)
    0000   0xb2 0x07 0x2b 0x61 0x0d                   ..+a.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2013-08-01T11:07:50 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-08-01T11:07:50)
    0000   0xb2 0x07 0x8b 0x61 0x0d                   ...a.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2013-08-01T11:22:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 48}
```
    op hex (2)
    0000   0x0a 0x30                                  .0
    decimal
             10   48
    datetime (2013-08-01T11:22:35)
    0000   0xa3 0x16 0x4b 0x01 0x0d                   ..K..
    body (0)

#### RECORD 9 BolusWizard 2013-08-01T11:22:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 48,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 24.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x30                                  [0
    decimal
             91   48
    datetime (2013-08-01T11:22:39)
    0000   0xa7 0x16 0x0b 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0xf4 0x00    ...n.6..
    0008   0x44 0xf8 0x00 0x10 0x00 0x38 0x36         D....86
    decimal
             19  144    0  110   23   54  244    0
             68  248    0   16    0   56   54
    DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 2.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x54 0xb1 0x04                   \.T..
    decimal
             92    5   84  177    4
    datetime (unknown)

    body (0)

#### RECORD 11 Ian69 2013-08-01T11:22:39 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-01T11:22:39)
    0000   0xa7 0x16 0x0b 0x01 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 12 Bolus 2013-08-01T11:22:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x10 0x00    ..8.8...
    decimal
              1    0   56    0   56    0   16    0
    datetime (2013-08-01T11:22:39)
    0000   0xa7 0x16 0x4b 0x61 0x0d                   ..Ka.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-08-01T12:04:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-01T12:04:30)
    0000   0x9e 0x04 0x0c 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 1.4, 'curve': 4},
 {'age': 219, 'amount': 2.1, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x38 0x31 0x04 0x54 0xdb 0x04    \.81.T..
    decimal
             92    8   56   49    4   84  219    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-08-01T12:04:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x38 0x00    ..l.l.8.
    decimal
              1    0  108    0  108    0   56    0
    datetime (2013-08-01T12:04:30)
    0000   0x9e 0x04 0x4c 0x61 0x0d                   ..La.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 16 BasalProfileStart 2013-08-01T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-01T13:00:00)
    0000   0x80 0x00 0x0d 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 17 CalBGForPH 2013-08-01T13:16:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2013-08-01T13:16:14)
    0000   0x8e 0x10 0x2d 0x61 0x0d                   ..-a.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 18 Ian3F 2013-08-01T13:16:14 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-08-01T13:16:14)
    0000   0x8e 0x10 0xad 0x61 0x0d                   ...a.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 19 CalBGForPH 2013-08-01T18:00:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-08-01T18:00:16)
    0000   0x90 0x00 0x32 0x61 0x0d                   ..2a.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 20 Ian3F 2013-08-01T18:00:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-08-01T18:00:16)
    0000   0x90 0x00 0xf2 0x61 0x0d                   ...a.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 21 BolusWizard 2013-08-01T18:01:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 66,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x42                                  [B
    decimal
             91   66
    datetime (2013-08-01T18:01:01)
    0000   0x81 0x01 0x12 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x14 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x38 0x36         $....86
    decimal
             10  144    0  110   23   54   20    0
             36    0    0    0    0   56   54
    DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 1.95, 'curve': 20},
 {'age': 110, 'amount': 0.75, 'curve': 20},
 {'age': 150, 'amount': 1.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4e 0x64 0x14 0x1e 0x6e 0x14    \.Nd..n.
    0008   0x38 0x96 0x14                             8..
    decimal
             92   11   78  100   20   30  110   20
             56  150   20
    datetime (unknown)

    body (0)

#### RECORD 23 Ian69 2013-08-01T18:01:02 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-01T18:01:02)
    0000   0x82 0x01 0x72 0x01 0x0d                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 24 Bolus 2013-08-01T18:01:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-01T18:01:01)
    0000   0x81 0x01 0x52 0x61 0x0d                   ..Ra.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 25 BolusWizard 2013-08-01T18:59:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 33,
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
    datetime (2013-08-01T18:59:50)
    0000   0xb2 0x3b 0x12 0x61 0x0d                   .;.a.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 1.4, 'curve': 4},
 {'age': 158, 'amount': 1.95, 'curve': 20},
 {'age': 168, 'amount': 0.75, 'curve': 20},
 {'age': 208, 'amount': 1.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x40 0x04 0x4e 0x9e 0x14    \.8@.N..
    0008   0x1e 0xa8 0x14 0x38 0xd0 0x14              ...8..
    decimal
             92   14   56   64    4   78  158   20
             30  168   20   56  208   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-08-01T18:59:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x30 0x00    ..x.x.0.
    decimal
              1    0  120    0  120    0   48    0
    datetime (2013-08-01T18:59:50)
    0000   0xb2 0x3b 0x52 0x61 0x0d                   .;Ra.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 BolusWizard 2013-08-01T19:28:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-01T19:28:27)
    0000   0x9b 0x1c 0x13 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    DAY BITS: [0, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 3.0, 'curve': 4},
 {'age': 93, 'amount': 1.4, 'curve': 4},
 {'age': 187, 'amount': 1.95, 'curve': 20},
 {'age': 197, 'amount': 0.75, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x21 0x04 0x38 0x5d 0x04    \.x!.8].
    0008   0x4e 0xbb 0x14 0x1e 0xc5 0x14              N.....
    decimal
             92   14  120   33    4   56   93    4
             78  187   20   30  197   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-08-01T19:28:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x94 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  148    0
    datetime (2013-08-01T19:28:28)
    0000   0x9c 0x1c 0x53 0x61 0x0d                   ..Sa.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-08-01T22:43:33 head[2], body[15] op[0x5b]
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
    datetime (2013-08-01T22:43:33)
    0000   0xa1 0x2b 0x16 0x61 0x0d                   .+.a.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 198, 'amount': 1.2, 'curve': 4},
 {'age': 228, 'amount': 3.0, 'curve': 4},
 {'age': 32, 'amount': 1.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0xc6 0x04 0x78 0xe4 0x04    \.0..x..
    0008   0x38 0x20 0x14                             8 .
    decimal
             92   11   48  198    4  120  228    4
             56   32   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-08-01T22:43:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x10 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   16    0
    datetime (2013-08-01T22:43:33)
    0000   0xa1 0x2b 0x56 0x61 0x0d                   .+Va.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2013-08-01T22:56:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-01T22:56:00)
    0000   0x80 0x38 0x16 0x61 0x0d                   .8.a.
    body (15)
    hex
    0000   0x10 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x36         8....86
    decimal
             16  144    0  110   23   54    0    0
             56    0    0    0    0   56   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 0.05, 'curve': 4},
 {'age': 21, 'amount': 2.15, 'curve': 4},
 {'age': 211, 'amount': 1.2, 'curve': 4},
 {'age': 241, 'amount': 3.0, 'curve': 4},
 {'age': 45, 'amount': 1.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x02 0x0b 0x04 0x56 0x15 0x04    \....V..
    0008   0x30 0xd3 0x04 0x78 0xf1 0x04 0x38 0x2d    0..x..8-
    0010   0x14                                       .
    decimal
             92   17    2   11    4   86   21    4
             48  211    4  120  241    4   56   45
             20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-08-01T22:56:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x64 0x00    ..8.8.d.
    decimal
              1    0   56    0   56    0  100    0
    datetime (2013-08-01T22:56:00)
    0000   0x80 0x38 0x56 0x61 0x0d                   .8Va.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 BolusWizard 2013-08-01T23:24:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 33,
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
    datetime (2013-08-01T23:24:20)
    0000   0x94 0x18 0x17 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.4, 'curve': 4},
 {'age': 39, 'amount': 0.05, 'curve': 4},
 {'age': 49, 'amount': 2.15, 'curve': 4},
 {'age': 239, 'amount': 1.2, 'curve': 4},
 {'age': 13, 'amount': 3.0, 'curve': 20},
 {'age': 73, 'amount': 1.4, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x38 0x1d 0x04 0x02 0x27 0x04    \.8...'.
    0008   0x56 0x31 0x04 0x30 0xef 0x04 0x78 0x0d    V1.0..x.
    0010   0x14 0x38 0x49 0x14                        .8I.
    decimal
             92   20   56   29    4    2   39    4
             86   49    4   48  239    4  120   13
             20   56   73   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-08-01T23:24:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x88 0x00    ........
    decimal
              1    0  136    0  136    0  136    0
    datetime (2013-08-01T23:24:20)
    0000   0x94 0x18 0x57 0x61 0x0d                   ..Wa.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 40 BasalProfileStart 2013-08-02T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-02T00:00:00)
    0000   0x80 0x00 0x00 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 41 MResultTotals 2013-08-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xcd                   .....
    decimal
              7    0    0    6  205
    datetime (2013-08-02T00:00:00)
    0000   0x81 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 42 Sara6E 2013-08-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-02T00:00:00)
    0000   0x81 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x5c 0x4c 0x77 0x06 0x00 0x00    ..\Lw...
    0008   0x06 0xcd 0x03 0x89 0x34 0x03 0x44 0x30    ....4.D0
    0010   0x00 0xe4 0x02 0x84 0x00 0x00 0x00 0xc0    ........
    0018   0x00 0x00 0x08 0x00 0x02 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x56    .......V
    0028   0x56 0x00 0x00 0x00 0x00 0x00 0x00 0x00    V.......
    0030   0x00                                       .
    decimal
              6    0   92   76  119    6    0    0
              6  205    3  137   52    3   68   48
              0  228    2  132    0    0    0  192
              0    0    8    0    2    0    0    0
              0    0    0    0    0    0    0   86
             86    0    0    0    0    0    0    0
              0

#### RECORD 43 BasalProfileStart 2013-08-02T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-02T04:00:00)
    0000   0x80 0x00 0x04 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 44 CalBGForPH 2013-08-02T08:07:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-08-02T08:07:50)
    0000   0xb2 0x07 0x28 0x62 0x0d                   ..(b.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 45 Ian3F 2013-08-02T08:07:50 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2013-08-02T08:07:50)
    0000   0xb2 0x07 0xe8 0x62 0x0d                   ...b.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2013-08-02T08:07:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 93,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2013-08-02T08:07:54)
    0000   0xb6 0x07 0x08 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x36         .....@6
    decimal
              0  144    0  110   23   54   64    0
              0    0    0    0    0   64   54
    DAY BITS: [0, 1, 1]
#### RECORD 47 Ian69 2013-08-02T08:07:55 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-02T08:07:55)
    0000   0xb7 0x07 0x08 0x02 0x0d                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 48 Bolus 2013-08-02T08:07:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-02T08:07:54)
    0000   0xb6 0x07 0x48 0x62 0x0d                   ..Hb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-08-02T09:23:57 head[2], body[15] op[0x5b]
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
    datetime (2013-08-02T09:23:57)
    0000   0xb9 0x17 0x09 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x4e 0x04                   \.@N.
    decimal
             92    5   64   78    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-02T09:23:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x30 0x00    ..H.H.0.
    decimal
              1    0   72    0   72    0   48    0
    datetime (2013-08-02T09:23:57)
    0000   0xb9 0x17 0x49 0x62 0x0d                   ..Ib.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2013-08-02T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-02T09:30:00)
    0000   0x80 0x1e 0x09 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 53 BolusWizard 2013-08-02T11:18:54 head[2], body[15] op[0x5b]
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
    datetime (2013-08-02T11:18:54)
    0000   0xb6 0x12 0x0b 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 0.2, 'curve': 4},
 {'age': 123, 'amount': 1.6, 'curve': 4},
 {'age': 193, 'amount': 1.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x08 0x71 0x04 0x40 0x7b 0x04    \..q.@{.
    0008   0x40 0xc1 0x04                             @..
    decimal
             92   11    8  113    4   64  123    4
             64  193    4
    datetime (unknown)

    body (0)

#### RECORD 55 Ian69 2013-08-02T11:18:54 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-02T11:18:54)
    0000   0xb6 0x12 0x0b 0x02 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 56 Bolus 2013-08-02T11:18:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x2c 0x00    ..H.H.,.
    decimal
              1    0   72    0   72    0   44    0
    datetime (2013-08-02T11:18:54)
    0000   0xb6 0x12 0x4b 0x62 0x0d                   ..Kb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 57 CalBGForPH 2013-08-02T11:52:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-08-02T11:52:34)
    0000   0xa2 0x34 0x2b 0x62 0x0d                   .4+b.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 Ian3F 2013-08-02T11:52:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2013-08-02T11:52:34)
    0000   0xa2 0x34 0x4b 0x62 0x0d                   .4Kb.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 BolusWizard 2013-08-02T12:27:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-02T12:27:08)
    0000   0x88 0x1b 0x0c 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 1.8, 'curve': 4},
 {'age': 182, 'amount': 0.2, 'curve': 4},
 {'age': 192, 'amount': 1.6, 'curve': 4},
 {'age': 6, 'amount': 1.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x48 0x04 0x08 0xb6 0x04    \.HH....
    0008   0x40 0xc0 0x04 0x40 0x06 0x14              @..@..
    decimal
             92   14   72   72    4    8  182    4
             64  192    4   64    6   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-08-02T12:27:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x44 0x00    ..l.l.D.
    decimal
              1    0  108    0  108    0   68    0
    datetime (2013-08-02T12:27:08)
    0000   0x88 0x1b 0x4c 0x62 0x0d                   ..Lb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 62 BasalProfileStart 2013-08-02T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-02T13:00:00)
    0000   0x80 0x00 0x0d 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 63 BolusWizard 2013-08-02T14:07:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-02T14:07:57)
    0000   0xb9 0x07 0x0e 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 2.7, 'curve': 4},
 {'age': 172, 'amount': 1.8, 'curve': 4},
 {'age': 26, 'amount': 0.2, 'curve': 20},
 {'age': 36, 'amount': 1.6, 'curve': 20},
 {'age': 106, 'amount': 1.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x6c 0x66 0x04 0x48 0xac 0x04    \.lf.H..
    0008   0x08 0x1a 0x14 0x40 0x24 0x14 0x40 0x6a    ...@$.@j
    0010   0x14                                       .
    decimal
             92   17  108  102    4   72  172    4
              8   26   20   64   36   20   64  106
             20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-08-02T14:07:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x50 0x00    ..0.0.P.
    decimal
              1    0   48    0   48    0   80    0
    datetime (2013-08-02T14:07:57)
    0000   0xb9 0x07 0x4e 0x62 0x0d                   ..Nb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 BolusWizard 2013-08-02T18:25:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-02T18:25:38)
    0000   0xa6 0x19 0x12 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 1.2, 'curve': 20},
 {'age': 104, 'amount': 2.7, 'curve': 20},
 {'age': 174, 'amount': 1.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x04 0x14 0x6c 0x68 0x14    \.0..lh.
    0008   0x48 0xae 0x14                             H..
    decimal
             92   11   48    4   20  108  104   20
             72  174   20
    datetime (unknown)

    body (0)

#### RECORD 68 Ian69 2013-08-02T18:25:38 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-02T18:25:38)
    0000   0xa6 0x19 0x72 0x02 0x0d                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 69 Bolus 2013-08-02T18:25:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-08-02T18:25:38)
    0000   0xa6 0x19 0x52 0x62 0x0d                   ..Rb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 70 BolusWizard 2013-08-02T18:59:15 head[2], body[15] op[0x5b]
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
    datetime (2013-08-02T18:59:15)
    0000   0x8f 0x3b 0x12 0x62 0x0d                   .;.b.
    body (15)
    hex
    0000   0x0c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x36         (....(6
    decimal
             12  144    0  110   23   54    0    0
             40    0    0    0    0   40   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 2.7, 'curve': 4},
 {'age': 38, 'amount': 1.2, 'curve': 20},
 {'age': 138, 'amount': 2.7, 'curve': 20},
 {'age': 208, 'amount': 1.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0x22 0x04 0x30 0x26 0x14    \.l".0&.
    0008   0x6c 0x8a 0x14 0x48 0xd0 0x14              l..H..
    decimal
             92   14  108   34    4   48   38   20
            108  138   20   72  208   20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-08-02T18:59:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x68 0x00    ..(.(.h.
    decimal
              1    0   40    0   40    0  104    0
    datetime (2013-08-02T18:59:15)
    0000   0x8f 0x3b 0x52 0x62 0x0d                   .;Rb.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
`end analysis/ianj/raw/ReadHistoryData-page-30.data: 73 records`
