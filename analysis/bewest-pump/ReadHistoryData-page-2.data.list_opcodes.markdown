## START logs/ReadHistoryData-page-2.data
#### RECORD 0 BolusWizard 2013-01-14T05:44:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 372,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-01-14T05:44:31)
    0000   0x1f 0x6c 0x05 0x0e 0x0d                   .l...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x36 0x00 0x00    .Q.-j6..
    0008   0x00 0x1a 0x00 0x1c 0x7d                   ....}
    decimal
              0   81   13   45  106   54    0    0
              0   26    0   28  125
    HOUR BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 3.6, 'curve': 4},
 {'age': 200, 'amount': 0.3, 'curve': 4},
 {'age': 210, 'amount': 0.3, 'curve': 5},
 {'age': 204, 'amount': 1.9, 'curve': 20},
 {'age': 214, 'amount': 2.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x90 0x6e 0x04 0x0c 0xc8 0x04    \..n....
    0008   0x0c 0xd2 0x05 0x4c 0xcc 0x14 0x54 0xd6    ...L..T.
    0010   0x14                                       .
    decimal
             92   17  144  110    4   12  200    4
             12  210    5   76  204   20   84  214
             20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-01-14T05:44:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-01-14T05:44:31)
    0000   0x1f 0x6c 0x45 0x0e 0x0d                   .lE..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-01-14T07:13:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 369}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-01-14T07:13:12)
    0000   0x0c 0x4d 0x27 0x0e 0x8d                   .M'..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 BolusWizard 2013-01-14T07:13:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 369,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-01-14T07:13:36)
    0000   0x24 0x4d 0x07 0x0e 0x0d                   $M...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x36 0x00 0x00    .Q.-j6..
    0008   0x00 0x18 0x00 0x1e 0x7d                   ....}
    decimal
              0   81   13   45  106   54    0    0
              0   24    0   30  125
    HOUR BITS: [0, 1, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 89, 'amount': 3.0, 'curve': 4},
 {'age': 199, 'amount': 3.6, 'curve': 4},
 {'age': 33, 'amount': 0.3, 'curve': 20},
 {'age': 43, 'amount': 0.3, 'curve': 21}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x59 0x04 0x90 0xc7 0x04    \.xY....
    0008   0x0c 0x21 0x14 0x0c 0x2b 0x15              .!..+.
    decimal
             92   14  120   89    4  144  199    4
             12   33   20   12   43   21
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-01-14T07:13:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-01-14T07:13:36)
    0000   0x24 0x4d 0x47 0x0e 0x0d                   $MG..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 TempBasal 2013-01-14T07:16:24 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.05}
```
    op hex (2)
    0000   0x33 0x2a                                  3*
    decimal
             51   42
    datetime (2013-01-14T07:16:24)
    0000   0x18 0x50 0x07 0x0e 0x0d                   .P...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 0]
#### RECORD 8 TempBasalDuration 2013-01-14T07:16:24 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-01-14T07:16:24)
    0000   0x18 0x50 0x07 0x0e 0x0d                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 CalBGForPH 2013-01-14T08:00:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 421}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2013-01-14T08:00:31)
    0000   0x1f 0x40 0x28 0x0e 0x8d                   .@(..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 BolusWizard 2013-01-14T08:00:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 65,
 '_byte[7]': 0,
 'bg': 421,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2013-01-14T08:00:41)
    0000   0x29 0x40 0x08 0x0e 0x0d                   )@...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x41 0x00 0x00    .Q.-jA..
    0008   0x00 0x26 0x00 0x1b 0x7d                   .&..}
    decimal
              0   81   13   45  106   65    0    0
              0   38    0   27  125
    HOUR BITS: [0, 1, 0]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 2.4, 'curve': 4},
 {'age': 56, 'amount': 0.6, 'curve': 4},
 {'age': 136, 'amount': 3.0, 'curve': 4},
 {'age': 246, 'amount': 3.6, 'curve': 4},
 {'age': 80, 'amount': 0.3, 'curve': 20},
 {'age': 90, 'amount': 0.3, 'curve': 21}]
```
    op hex (20)
    0000   0x5c 0x14 0x60 0x2e 0x04 0x18 0x38 0x04    \.`...8.
    0008   0x78 0x88 0x04 0x90 0xf6 0x04 0x0c 0x50    x......P
    0010   0x14 0x0c 0x5a 0x15                        ..Z.
    decimal
             92   20   96   46    4   24   56    4
            120  136    4  144  246    4   12   80
             20   12   90   21
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-01-14T08:00:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-01-14T08:00:41)
    0000   0x29 0x40 0x48 0x0e 0x0d                   )@H..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 13 TempBasal 2013-01-14T08:05:06 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.2}
```
    op hex (2)
    0000   0x33 0x30                                  30
    decimal
             51   48
    datetime (2013-01-14T08:05:06)
    0000   0x06 0x45 0x08 0x0e 0x0d                   .E...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 0]
#### RECORD 14 TempBasalDuration 2013-01-14T08:05:06 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-01-14T08:05:06)
    0000   0x06 0x45 0x08 0x0e 0x0d                   .E...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 CalBGForPH 2013-01-14T08:16:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 418}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-01-14T08:16:51)
    0000   0x33 0x50 0x28 0x0e 0x8d                   3P(..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2013-01-14T08:17:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 65,
 '_byte[7]': 0,
 'bg': 418,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 6.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-01-14T08:17:01)
    0000   0x01 0x51 0x08 0x0e 0x0d                   .Q...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x41 0x00 0x00    .Q.-jA..
    0008   0x00 0x41 0x00 0x00 0x7d                   .A..}
    decimal
              0   81   13   45  106   65    0    0
              0   65    0    0  125
    HOUR BITS: [0, 1, 0]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 3.3, 'curve': 4},
 {'age': 63, 'amount': 2.4, 'curve': 4},
 {'age': 73, 'amount': 0.6, 'curve': 4},
 {'age': 153, 'amount': 3.0, 'curve': 4},
 {'age': 7, 'amount': 3.6, 'curve': 20},
 {'age': 97, 'amount': 0.3, 'curve': 20},
 {'age': 107, 'amount': 0.3, 'curve': 21}]
```
    op hex (23)
    0000   0x5c 0x17 0x84 0x17 0x04 0x60 0x3f 0x04    \....`?.
    0008   0x18 0x49 0x04 0x78 0x99 0x04 0x90 0x07    .I.x....
    0010   0x14 0x0c 0x61 0x14 0x0c 0x6b 0x15         ..a..k.
    decimal
             92   23  132   23    4   96   63    4
             24   73    4  120  153    4  144    7
             20   12   97   20   12  107   21
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-01-14T08:17:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-01-14T08:17:01)
    0000   0x01 0x51 0x48 0x0e 0x0d                   .QH..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 CalBGForPH 2013-01-14T08:33:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 365}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-01-14T08:33:32)
    0000   0x20 0x61 0x28 0x0e 0x8d                    a(..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 CalBGForPH 2013-01-14T08:43:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 365}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-01-14T08:43:09)
    0000   0x09 0x6b 0x28 0x0e 0x8d                   .k(..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 BolusWizard 2013-01-14T08:43:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 53,
 '_byte[7]': 0,
 'bg': 365,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 6.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-01-14T08:43:58)
    0000   0x3a 0x6b 0x08 0x0e 0x0d                   :k...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x35 0x00 0x00    .Q.-j5..
    0008   0x00 0x3d 0x00 0x00 0x7d                   .=..}
    decimal
              0   81   13   45  106   53    0    0
              0   61    0    0  125
    HOUR BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 0.7, 'curve': 4},
 {'age': 49, 'amount': 3.3, 'curve': 4},
 {'age': 89, 'amount': 2.4, 'curve': 4},
 {'age': 99, 'amount': 0.6, 'curve': 4},
 {'age': 179, 'amount': 3.0, 'curve': 4},
 {'age': 33, 'amount': 3.6, 'curve': 20},
 {'age': 123, 'amount': 0.3, 'curve': 20},
 {'age': 133, 'amount': 0.3, 'curve': 21}]
```
    op hex (26)
    0000   0x5c 0x1a 0x1c 0x1d 0x04 0x84 0x31 0x04    \.....1.
    0008   0x60 0x59 0x04 0x18 0x63 0x04 0x78 0xb3    `Y..c.x.
    0010   0x04 0x90 0x21 0x14 0x0c 0x7b 0x14 0x0c    ..!..{..
    0018   0x85 0x15                                  ..
    decimal
             92   26   28   29    4  132   49    4
             96   89    4   24   99    4  120  179
              4  144   33   20   12  123   20   12
            133   21
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-01-14T08:43:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-01-14T08:43:58)
    0000   0x3a 0x6b 0x48 0x0e 0x0d                   :kH..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 24 CalBGForPH 2013-01-14T09:47:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 343}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2013-01-14T09:47:14)
    0000   0x0e 0x6f 0x29 0x0e 0x8d                   .o)..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 BolusWizard 2013-01-14T09:47:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 48,
 '_byte[7]': 0,
 'bg': 343,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2013-01-14T09:47:46)
    0000   0x2e 0x6f 0x09 0x0e 0x0d                   .o...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x30 0x00 0x00    .Q.-j0..
    0008   0x00 0x26 0x00 0x0a 0x7d                   .&..}
    decimal
              0   81   13   45  106   48    0    0
              0   38    0   10  125
    HOUR BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 63, 'amount': 0.95, 'curve': 4},
 {'age': 73, 'amount': 0.05, 'curve': 4},
 {'age': 93, 'amount': 0.7, 'curve': 4},
 {'age': 113, 'amount': 3.3, 'curve': 4},
 {'age': 153, 'amount': 2.4, 'curve': 4},
 {'age': 163, 'amount': 0.6, 'curve': 4},
 {'age': 243, 'amount': 3.0, 'curve': 4},
 {'age': 97, 'amount': 3.6, 'curve': 20},
 {'age': 187, 'amount': 0.3, 'curve': 20},
 {'age': 197, 'amount': 0.3, 'curve': 21}]
```
    op hex (32)
    0000   0x5c 0x20 0x26 0x3f 0x04 0x02 0x49 0x04    \ &?..I.
    0008   0x1c 0x5d 0x04 0x84 0x71 0x04 0x60 0x99    .]..q.`.
    0010   0x04 0x18 0xa3 0x04 0x78 0xf3 0x04 0x90    ....x...
    0018   0x61 0x14 0x0c 0xbb 0x14 0x0c 0xc5 0x15    a.......
    decimal
             92   32   38   63    4    2   73    4
             28   93    4  132  113    4   96  153
              4   24  163    4  120  243    4  144
             97   20   12  187   20   12  197   21
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-01-14T09:47:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-01-14T09:47:46)
    0000   0x2e 0x6f 0x49 0x0e 0x0d                   .oI..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 28 TempBasal 2013-01-14T09:51:36 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2013-01-14T09:51:36)
    0000   0x24 0x73 0x09 0x0e 0x0d                   $s...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]
#### RECORD 29 TempBasalDuration 2013-01-14T09:51:36 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-01-14T09:51:36)
    0000   0x24 0x73 0x09 0x0e 0x0d                   $s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 30 Rewind 2013-01-14T10:10:55 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-01-14T10:10:55)
    0000   0x37 0x4a 0x0a 0x0e 0x0d                   7J...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 31 Prime 2013-01-14T10:16:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x21                   ....!
    decimal
              3    0    0    0   33
    datetime (2013-01-14T10:16:13)
    0000   0x0d 0x50 0x2a 0x0e 0x0d                   .P*..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 Prime 2013-01-14T10:16:38 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-14T10:16:38)
    0000   0x26 0x50 0x0a 0x0e 0x0d                   &P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 CalBGForPH 2013-01-14T10:18:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 347}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-01-14T10:18:22)
    0000   0x16 0x52 0x2a 0x0e 0x8d                   .R*..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 BolusWizard 2013-01-14T10:18:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 49,
 '_byte[7]': 0,
 'bg': 347,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 5.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2013-01-14T10:18:47)
    0000   0x2f 0x52 0x0a 0x0e 0x0d                   /R...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x31 0x00 0x00    .Q.-j1..
    0008   0x00 0x35 0x00 0x00 0x7d                   .5..}
    decimal
              0   81   13   45  106   49    0    0
              0   53    0    0  125
    HOUR BITS: [0, 1, 0]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 3.0, 'curve': 4},
 {'age': 94, 'amount': 0.95, 'curve': 4},
 {'age': 104, 'amount': 0.05, 'curve': 4},
 {'age': 124, 'amount': 0.7, 'curve': 4},
 {'age': 144, 'amount': 3.3, 'curve': 4},
 {'age': 184, 'amount': 2.4, 'curve': 4},
 {'age': 194, 'amount': 0.6, 'curve': 4},
 {'age': 18, 'amount': 3.0, 'curve': 20},
 {'age': 128, 'amount': 3.6, 'curve': 20},
 {'age': 218, 'amount': 0.3, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x78 0x22 0x04 0x26 0x5e 0x04    \ x".&^.
    0008   0x02 0x68 0x04 0x1c 0x7c 0x04 0x84 0x90    .h..|...
    0010   0x04 0x60 0xb8 0x04 0x18 0xc2 0x04 0x78    .`.....x
    0018   0x12 0x14 0x90 0x80 0x14 0x0c 0xda 0x14    ........
    decimal
             92   32  120   34    4   38   94    4
              2  104    4   28  124    4  132  144
              4   96  184    4   24  194    4  120
             18   20  144  128   20   12  218   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-01-14T10:18:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-01-14T10:18:47)
    0000   0x2f 0x52 0x4a 0x0e 0x0d                   /RJ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 TempBasal 2013-01-14T11:24:40 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2013-01-14T11:24:40)
    0000   0x28 0x58 0x0b 0x0e 0x0d                   (X...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 0]
#### RECORD 38 TempBasalDuration 2013-01-14T11:24:40 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-01-14T11:24:40)
    0000   0x28 0x58 0x0b 0x0e 0x0d                   (X...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 CalBGForPH 2013-01-14T11:25:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 352}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-01-14T11:25:04)
    0000   0x04 0x59 0x2b 0x0e 0x8d                   .Y+..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 40 BolusWizard 2013-01-14T11:25:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 50,
 '_byte[7]': 0,
 'bg': 352,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-01-14T11:25:33)
    0000   0x21 0x59 0x0b 0x0e 0x0d                   !Y...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x32 0x00 0x00    .Q.-j2..
    0008   0x00 0x20 0x00 0x12 0x7d                   . ..}
    decimal
              0   81   13   45  106   50    0    0
              0   32    0   18  125
    HOUR BITS: [0, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 1.0, 'curve': 4},
 {'age': 101, 'amount': 3.0, 'curve': 4},
 {'age': 161, 'amount': 0.95, 'curve': 4},
 {'age': 171, 'amount': 0.05, 'curve': 4},
 {'age': 191, 'amount': 0.7, 'curve': 4},
 {'age': 211, 'amount': 3.3, 'curve': 4},
 {'age': 251, 'amount': 2.4, 'curve': 4},
 {'age': 5, 'amount': 0.6, 'curve': 20},
 {'age': 85, 'amount': 3.0, 'curve': 20},
 {'age': 195, 'amount': 3.6, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x28 0x47 0x04 0x78 0x65 0x04    \ (G.xe.
    0008   0x26 0xa1 0x04 0x02 0xab 0x04 0x1c 0xbf    &.......
    0010   0x04 0x84 0xd3 0x04 0x60 0xfb 0x04 0x18    ....`...
    0018   0x05 0x14 0x78 0x55 0x14 0x90 0xc3 0x14    ..xU....
    decimal
             92   32   40   71    4  120  101    4
             38  161    4    2  171    4   28  191
              4  132  211    4   96  251    4   24
              5   20  120   85   20  144  195   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-01-14T11:25:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x23 0x1d 0x00                        .#..
    decimal
              1   35   29    0
    datetime (2013-01-14T11:25:33)
    0000   0x21 0x59 0x4b 0x0e 0x0d                   !YK..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 43 NoDelivery 2013-01-14T11:27:29 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xff                        ....
    decimal
              6    4   11  255
    datetime (2013-01-14T11:27:29)
    0000   0x1d 0x5b 0x4b 0x4e 0x0d                   .[KN.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 44 ClearAlarm 2013-01-14T11:32:07 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-01-14T11:32:07)
    0000   0x07 0x60 0x0b 0x0e 0x0d                   .`...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 45 Prime 2013-01-14T15:42:57 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-14T15:42:57)
    0000   0x39 0x6a 0x0f 0x0e 0x0d                   9j...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 CalBGForPH 2013-01-14T15:47:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2013-01-14T15:47:00)
    0000   0x00 0x6f 0x2f 0x0e 0x0d                   .o/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-01-14T15:47:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
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
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-01-14T15:47:39)
    0000   0x27 0x6f 0x0f 0x0e 0x0d                   'o...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    0    0   11  125
    HOUR BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 2.85, 'curve': 20},
 {'age': 77, 'amount': 1.0, 'curve': 20},
 {'age': 107, 'amount': 3.0, 'curve': 20},
 {'age': 167, 'amount': 0.95, 'curve': 20},
 {'age': 177, 'amount': 0.05, 'curve': 20},
 {'age': 197, 'amount': 0.7, 'curve': 20},
 {'age': 217, 'amount': 3.3, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x72 0x07 0x14 0x28 0x4d 0x14    \.r..(M.
    0008   0x78 0x6b 0x14 0x26 0xa7 0x14 0x02 0xb1    xk.&....
    0010   0x14 0x1c 0xc5 0x14 0x84 0xd9 0x14         .......
    decimal
             92   23  114    7   20   40   77   20
            120  107   20   38  167   20    2  177
             20   28  197   20  132  217   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-01-14T15:47:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-01-14T15:47:39)
    0000   0x27 0x6f 0x4f 0x0e 0x0d                   'oO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 50 CalBGForPH 2013-01-14T16:19:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-01-14T16:19:34)
    0000   0x22 0x53 0x30 0x0e 0x0d                   "S0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 51 BolusWizard 2013-01-14T16:21:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-01-14T16:21:43)
    0000   0x2b 0x55 0x10 0x0e 0x0d                   +U...
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x09 0x15 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    9   21    0
              0   11    0   21  125
    HOUR BITS: [0, 1, 0]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.1, 'curve': 4},
 {'age': 41, 'amount': 2.85, 'curve': 20},
 {'age': 111, 'amount': 1.0, 'curve': 20},
 {'age': 141, 'amount': 3.0, 'curve': 20},
 {'age': 201, 'amount': 0.95, 'curve': 20},
 {'age': 211, 'amount': 0.05, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x2c 0x25 0x04 0x72 0x29 0x14    \.,%.r).
    0008   0x28 0x6f 0x14 0x78 0x8d 0x14 0x26 0xc9    (o.x..&.
    0010   0x14 0x02 0xd3 0x14                        ....
    decimal
             92   20   44   37    4  114   41   20
             40  111   20  120  141   20   38  201
             20    2  211   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-01-14T16:21:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-01-14T16:21:44)
    0000   0x2c 0x55 0x50 0x0e 0x0d                   ,UP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 54 CalBGForPH 2013-01-14T17:44:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 322}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-01-14T17:44:12)
    0000   0x0c 0x6c 0x31 0x0e 0x8d                   .l1..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 55 BolusWizard 2013-01-14T17:44:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 43,
 '_byte[7]': 0,
 'bg': 322,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x42                                  [B
    decimal
             91   66
    datetime (2013-01-14T17:44:31)
    0000   0x1f 0x6c 0x11 0x0e 0x0d                   .l...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2b 0x00 0x00    .Q.-j+..
    0008   0x00 0x13 0x00 0x18 0x7d                   ....}
    decimal
              0   81   13   45  106   43    0    0
              0   19    0   24  125
    HOUR BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 2.1, 'curve': 4},
 {'age': 120, 'amount': 1.1, 'curve': 4},
 {'age': 124, 'amount': 2.85, 'curve': 20},
 {'age': 194, 'amount': 1.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x54 0x5a 0x04 0x2c 0x78 0x04    \.TZ.,x.
    0008   0x72 0x7c 0x14 0x28 0xc2 0x14              r|.(..
    decimal
             92   14   84   90    4   44  120    4
            114  124   20   40  194   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2013-01-14T17:44:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-01-14T17:44:31)
    0000   0x1f 0x6c 0x51 0x0e 0x0d                   .lQ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2013-01-14T19:11:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 288}
```
    op hex (2)
    0000   0x0a 0x20                                  . 
    decimal
             10   32
    datetime (2013-01-14T19:11:57)
    0000   0x39 0x4b 0x33 0x0e 0x8d                   9K3..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 59 BolusWizard 2013-01-14T19:12:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 288,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x20                                  [ 
    decimal
             91   32
    datetime (2013-01-14T19:12:17)
    0000   0x11 0x4c 0x13 0x0e 0x0d                   .L...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x15 0x00 0x0f 0x7d                   ....}
    decimal
              0   81   13   45  106   36    0    0
              0   21    0   15  125
    HOUR BITS: [0, 1, 0]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 2.4, 'curve': 4},
 {'age': 178, 'amount': 2.1, 'curve': 4},
 {'age': 208, 'amount': 1.1, 'curve': 4},
 {'age': 212, 'amount': 2.85, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x58 0x04 0x54 0xb2 0x04    \.`X.T..
    0008   0x2c 0xd0 0x04 0x72 0xd4 0x14              ,..r..
    decimal
             92   14   96   88    4   84  178    4
             44  208    4  114  212   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-01-14T19:12:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-01-14T19:12:17)
    0000   0x11 0x4c 0x53 0x0e 0x0d                   .LS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 CalBGForPH 2013-01-14T19:43:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 289}
```
    op hex (2)
    0000   0x0a 0x21                                  .!
    decimal
             10   33
    datetime (2013-01-14T19:43:28)
    0000   0x1c 0x6b 0x33 0x0e 0x8d                   .k3..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 63 BolusWizard 2013-01-14T19:43:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 289,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x21                                  [!
    decimal
             91   33
    datetime (2013-01-14T19:43:54)
    0000   0x36 0x6b 0x13 0x0e 0x0d                   6k...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x22 0x00 0x02 0x7d                   ."..}
    decimal
              0   81   13   45  106   36    0    0
              0   34    0    2  125
    HOUR BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 2.2, 'curve': 4},
 {'age': 119, 'amount': 2.4, 'curve': 4},
 {'age': 209, 'amount': 2.1, 'curve': 4},
 {'age': 239, 'amount': 1.1, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x58 0x27 0x04 0x60 0x77 0x04    \.X'.`w.
    0008   0x54 0xd1 0x04 0x2c 0xef 0x04              T..,..
    decimal
             92   14   88   39    4   96  119    4
             84  209    4   44  239    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-01-14T19:43:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-01-14T19:43:54)
    0000   0x36 0x6b 0x53 0x0e 0x0d                   6kS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 66 TempBasal 2013-01-14T19:44:44 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.15}
```
    op hex (2)
    0000   0x33 0x2e                                  3.
    decimal
             51   46
    datetime (2013-01-14T19:44:44)
    0000   0x2c 0x6c 0x13 0x0e 0x0d                   ,l...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]
#### RECORD 67 TempBasalDuration 2013-01-14T19:44:44 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2013-01-14T19:44:44)
    0000   0x2c 0x6c 0x13 0x0e 0x0d                   ,l...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2013-01-14T20:28:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-01-14T20:28:41)
    0000   0x29 0x5c 0x34 0x0e 0x0d                   )\4..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 69 BolusWizard 2013-01-14T20:29:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-01-14T20:29:17)
    0000   0x11 0x5d 0x14 0x0e 0x0d                   .]...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x19 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0   25    0    0  125
    HOUR BITS: [0, 1, 0]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 0.35, 'curve': 4},
 {'age': 55, 'amount': 0.15, 'curve': 4},
 {'age': 85, 'amount': 2.2, 'curve': 4},
 {'age': 165, 'amount': 2.4, 'curve': 4},
 {'age': 255, 'amount': 2.1, 'curve': 4},
 {'age': 29, 'amount': 1.1, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0e 0x2d 0x04 0x06 0x37 0x04    \..-..7.
    0008   0x58 0x55 0x04 0x60 0xa5 0x04 0x54 0xff    XU.`..T.
    0010   0x04 0x2c 0x1d 0x14                        .,..
    decimal
             92   20   14   45    4    6   55    4
             88   85    4   96  165    4   84  255
              4   44   29   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-01-14T20:29:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-01-14T20:29:17)
    0000   0x11 0x5d 0x54 0x0e 0x0d                   .]T..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 72 CalBGForPH 2013-01-14T20:48:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2013-01-14T20:48:12)
    0000   0x0c 0x70 0x34 0x0e 0x0d                   .p4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 73 TempBasal 2013-01-14T20:48:53 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.2}
```
    op hex (2)
    0000   0x33 0x30                                  30
    decimal
             51   48
    datetime (2013-01-14T20:48:53)
    0000   0x35 0x70 0x14 0x0e 0x0d                   5p...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]
#### RECORD 74 TempBasalDuration 2013-01-14T20:48:53 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-01-14T20:48:53)
    0000   0x35 0x70 0x14 0x0e 0x0d                   5p...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 75 CalBGForPH 2013-01-14T20:49:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2013-01-14T20:49:43)
    0000   0x2b 0x71 0x34 0x0e 0x0d                   +q4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 76 BolusWizard 2013-01-14T20:50:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 202,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xca                                  [.
    decimal
             91  202
    datetime (2013-01-14T20:50:11)
    0000   0x0b 0x72 0x14 0x0e 0x0d                   .r...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x11 0x00 0x00    .P.-j...
    0008   0x00 0x19 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   17    0    0
              0   25    0    0  125
    HOUR BITS: [0, 1, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 0.5, 'curve': 4},
 {'age': 66, 'amount': 0.35, 'curve': 4},
 {'age': 76, 'amount': 0.15, 'curve': 4},
 {'age': 106, 'amount': 2.2, 'curve': 4},
 {'age': 186, 'amount': 2.4, 'curve': 4},
 {'age': 20, 'amount': 2.1, 'curve': 20},
 {'age': 50, 'amount': 1.1, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x14 0x1a 0x04 0x0e 0x42 0x04    \.....B.
    0008   0x06 0x4c 0x04 0x58 0x6a 0x04 0x60 0xba    .L.Xj.`.
    0010   0x04 0x54 0x14 0x14 0x2c 0x32 0x14         .T..,2.
    decimal
             92   23   20   26    4   14   66    4
              6   76    4   88  106    4   96  186
              4   84   20   20   44   50   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-01-14T20:50:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'programmed': 0.9}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-01-14T20:50:11)
    0000   0x0b 0x72 0x54 0x0e 0x0d                   .rT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 79 CalBGForPH 2013-01-14T21:17:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2013-01-14T21:17:41)
    0000   0x29 0x51 0x35 0x0e 0x0d                   )Q5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xf4                                  ..
    decimal
              0  244
    datetime (unknown)
    0000   0x59                                       Y
    body (0)

`end logs/ReadHistoryData-page-2.data: 81 records`
