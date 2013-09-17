## START logs/ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 1004, found 18 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2b 0x78                                  +x
##### DEBUG DECIMAL
             43  120
#### RECORD 0 Ian69 2013-09-02T09:23:26 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-02T09:23:26)
    0000   0x9a 0x57 0x09 0x02 0x0d                   .W...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Bolus 2013-09-02T09:23:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-09-02T09:23:26)
    0000   0x9a 0x57 0x49 0x62 0x0d                   .WIb.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 BasalProfileStart 2013-09-02T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-02T09:30:00)
    0000   0x80 0x5e 0x09 0x02 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 3 BasalProfileStart 2013-09-02T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-02T13:00:00)
    0000   0x80 0x40 0x0d 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 4 Ian69 2013-09-02T14:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-02T14:30:00)
    0000   0x80 0x5e 0x0e 0x02 0x0d                   .^...
    body (2)
    hex
    0000   0x2e 0x1e                                  ..
    decimal
             46   30
    HOUR BITS: [0, 1, 0]
#### RECORD 5 BolusWizard 2013-09-02T15:00:28 head[2], body[15] op[0x5b]
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
    datetime (2013-09-02T15:00:28)
    0000   0x9c 0x40 0x0f 0x62 0x0d                   .@.b.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 2.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0x53 0x14                   \.`S.
    decimal
             92    5   96   83   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-09-02T15:00:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2013-09-02T15:00:28)
    0000   0x9c 0x40 0x4f 0x62 0x0d                   .@Ob.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2013-09-02T19:04:59 head[2], body[15] op[0x5b]
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
    datetime (2013-09-02T19:04:59)
    0000   0xbb 0x44 0x13 0x62 0x0d                   .D.b.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 243, 'amount': 2.2, 'curve': 4},
 {'age': 253, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x58 0xf3 0x04 0x20 0xfd 0x04    \.X.. ..
    decimal
             92    8   88  243    4   32  253    4
    datetime (unknown)

    body (0)

#### RECORD 10 Ian69 2013-09-02T19:04:59 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-02T19:04:59)
    0000   0xbb 0x44 0x73 0x02 0x0d                   .Ds..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 0]
#### RECORD 11 Bolus 2013-09-02T19:04:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2013-09-02T19:04:59)
    0000   0xbb 0x44 0x53 0x62 0x0d                   .DSb.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 BolusWizard 2013-09-02T19:09:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 9,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-09-02T19:09:02)
    0000   0x82 0x49 0x13 0x62 0x0d                   .I.b.
    body (15)
    hex
    0000   0x09 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x36          .... 6
    decimal
              9  144    0  110   23   54    0    0
             32    0    0    0    0   32   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 2.2, 'curve': 4},
 {'age': 248, 'amount': 2.2, 'curve': 4},
 {'age': 2, 'amount': 0.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x08 0x04 0x58 0xf8 0x04    \.X..X..
    0008   0x20 0x02 0x14                              ..
    decimal
             92   11   88    8    4   88  248    4
             32    2   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-09-02T19:09:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x58 0x00    .. . .X.
    decimal
              1    0   32    0   32    0   88    0
    datetime (2013-09-02T19:09:02)
    0000   0x82 0x49 0x53 0x62 0x0d                   .ISb.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 Bolus 2013-09-02T19:10:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x78 0x00    ......x.
    decimal
              1    0   16    0   16    0  120    0
    datetime (2013-09-02T19:10:19)
    0000   0x93 0x4a 0x53 0x62 0x0d                   .JSb.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2013-09-02T19:33:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-02T19:33:22)
    0000   0x96 0x61 0x13 0x62 0x0d                   .a.b.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 3.4, 'curve': 4},
 {'age': 16, 'amount': 2.2, 'curve': 20},
 {'age': 26, 'amount': 0.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x88 0x20 0x04 0x58 0x10 0x14    \.. .X..
    0008   0x20 0x1a 0x14                              ..
    decimal
             92   11  136   32    4   88   16   20
             32   26   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-09-02T19:33:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x80 0x00    ..L.L...
    decimal
              1    0   76    0   76    0  128    0
    datetime (2013-09-02T19:33:23)
    0000   0x97 0x61 0x53 0x62 0x0d                   .aSb.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2013-09-02T20:59:45 head[2], body[15] op[0x5b]
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
    datetime (2013-09-02T20:59:45)
    0000   0xad 0x7b 0x14 0x62 0x0d                   .{.b.
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x36         D....D6
    decimal
             19  144    0  110   23   54    0    0
             68    0    0    0    0   68   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.9, 'curve': 4},
 {'age': 118, 'amount': 3.4, 'curve': 4},
 {'age': 102, 'amount': 2.2, 'curve': 20},
 {'age': 112, 'amount': 0.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x4c 0x58 0x04 0x88 0x76 0x04    \.LX..v.
    0008   0x58 0x66 0x14 0x20 0x70 0x14              Xf. p.
    decimal
             92   14   76   88    4  136  118    4
             88  102   20   32  112   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-09-02T20:59:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x74 0x00    ..D.D.t.
    decimal
              1    0   68    0   68    0  116    0
    datetime (2013-09-02T20:59:46)
    0000   0xae 0x7b 0x54 0x62 0x0d                   .{Tb.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-09-02T21:49:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-02T21:49:17)
    0000   0x91 0x71 0x15 0x62 0x0d                   .q.b.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 58, 'amount': 1.7, 'curve': 4},
 {'age': 138, 'amount': 1.9, 'curve': 4},
 {'age': 168, 'amount': 3.4, 'curve': 4},
 {'age': 152, 'amount': 2.2, 'curve': 20},
 {'age': 162, 'amount': 0.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x3a 0x04 0x4c 0x8a 0x04    \.D:.L..
    0008   0x88 0xa8 0x04 0x58 0x98 0x14 0x20 0xa2    ...X.. .
    0010   0x14                                       .
    decimal
             92   17   68   58    4   76  138    4
            136  168    4   88  152   20   32  162
             20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-09-02T21:49:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x74 0x00    ......t.
    decimal
              1    0  156    0  156    0  116    0
    datetime (2013-09-02T21:49:17)
    0000   0x91 0x71 0x55 0x62 0x0d                   .qUb.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 BolusWizard 2013-09-02T22:28:19 head[2], body[15] op[0x5b]
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
    datetime (2013-09-02T22:28:19)
    0000   0x93 0x5c 0x16 0x62 0x0d                   .\.b.
    body (15)
    hex
    0000   0x10 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x36         8....86
    decimal
             16  144    0  110   23   54    0    0
             56    0    0    0    0   56   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.35, 'curve': 4},
 {'age': 47, 'amount': 2.55, 'curve': 4},
 {'age': 97, 'amount': 1.7, 'curve': 4},
 {'age': 177, 'amount': 1.9, 'curve': 4},
 {'age': 207, 'amount': 3.4, 'curve': 4},
 {'age': 191, 'amount': 2.2, 'curve': 20},
 {'age': 201, 'amount': 0.8, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x36 0x25 0x04 0x66 0x2f 0x04    \.6%.f/.
    0008   0x44 0x61 0x04 0x4c 0xb1 0x04 0x88 0xcf    Da.L....
    0010   0x04 0x58 0xbf 0x14 0x20 0xc9 0x14         .X.. ..
    decimal
             92   23   54   37    4  102   47    4
             68   97    4   76  177    4  136  207
              4   88  191   20   32  201   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-09-02T22:28:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0xd4 0x00    ..8.8...
    decimal
              1    0   56    0   56    0  212    0
    datetime (2013-09-02T22:28:19)
    0000   0x93 0x5c 0x56 0x62 0x0d                   .\Vb.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 BasalProfileStart 2013-09-03T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-03T00:00:00)
    0000   0x80 0x40 0x00 0x03 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 29 ResultTotals (2000, 10, 0, 0, 13, 2) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x4d                   ....M
    decimal
              7    0    0    6   77
    datetime ((2000, 10, 0, 0, 13, 2))
    0000   0x82 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x82 0x8d 0x06 0x00 0x00 0x00 0x00    n.......
    0008   0x00 0x00 0x00 0x06 0x4d 0x03 0x89 0x38    ....M..8
    0010   0x02 0xc4 0x2c 0x00 0xb3 0x02 0x18 0x00    ..,.....
    0018   0x00 0x00 0x9c 0x00 0x10 0x07 0x00 0x01    ........
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  130  141    6    0    0    0    0
              0    0    0    6   77    3  137   56
              2  196   44    0  179    2   24    0
              0    0  156    0   16    7    0    1
              1    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 31 BolusWizard 2013-09-03T01:23:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T01:23:47)
    0000   0xaf 0x57 0x01 0x63 0x0d                   .W.c.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 182, 'amount': 1.4, 'curve': 4},
 {'age': 212, 'amount': 1.35, 'curve': 4},
 {'age': 222, 'amount': 2.55, 'curve': 4},
 {'age': 16, 'amount': 1.7, 'curve': 20},
 {'age': 96, 'amount': 1.9, 'curve': 20},
 {'age': 126, 'amount': 3.4, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x38 0xb6 0x04 0x36 0xd4 0x04    \.8..6..
    0008   0x66 0xde 0x04 0x44 0x10 0x14 0x4c 0x60    f..D..L`
    0010   0x14 0x88 0x7e 0x14                        ..~.
    decimal
             92   20   56  182    4   54  212    4
            102  222    4   68   16   20   76   96
             20  136  126   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-09-03T01:23:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x18 0x00    ..T.T...
    decimal
              1    0   84    0   84    0   24    0
    datetime (2013-09-03T01:23:47)
    0000   0xaf 0x57 0x41 0x63 0x0d                   .WAc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 BasalProfileStart 2013-09-03T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-03T04:00:00)
    0000   0x80 0x40 0x04 0x03 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 35 BolusWizard 2013-09-03T09:03:59 head[2], body[15] op[0x5b]
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
    datetime (2013-09-03T09:03:59)
    0000   0xbb 0x43 0x09 0x63 0x0d                   .C.c.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 2.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x54 0xce 0x14                   \.T..
    decimal
             92    5   84  206   20
    datetime (unknown)

    body (0)

#### RECORD 37 Ian69 2013-09-03T09:03:59 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-03T09:03:59)
    0000   0xbb 0x43 0x09 0x03 0x0d                   .C...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 0]
#### RECORD 38 Bolus 2013-09-03T09:03:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-09-03T09:03:59)
    0000   0xbb 0x43 0x49 0x63 0x0d                   .CIc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 BasalProfileStart 2013-09-03T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-03T09:30:00)
    0000   0x80 0x5e 0x09 0x03 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 40 PumpSuspend 2013-09-03T10:52:08 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-09-03T10:52:08)
    0000   0x88 0x74 0x0a 0x03 0x0d                   .t...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 BasalProfileStart 2013-09-03T12:14:40 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-03T12:14:40)
    0000   0xa8 0x4e 0x0c 0x03 0x0d                   .N...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 42 PumpResume 2013-09-03T12:14:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-09-03T12:14:40)
    0000   0xa8 0x4e 0x0c 0x03 0x0d                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 43 BolusWizard 2013-09-03T12:14:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T12:14:47)
    0000   0xaf 0x4e 0x0c 0x63 0x0d                   .N.c.
    body (15)
    hex
    0000   0x20 0x90 0x00 0x6e 0x17 0x36 0x00 0x00     ..n.6..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x36         t....t6
    decimal
             32  144    0  110   23   54    0    0
            116    0    0    0    0  116   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 2.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0xc1 0x04                   \.l..
    decimal
             92    5  108  193    4
    datetime (unknown)

    body (0)

#### RECORD 45 Ian69 2013-09-03T12:14:47 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-03T12:14:47)
    0000   0xaf 0x4e 0x0c 0x03 0x0d                   .N...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 1, 0]
#### RECORD 46 Bolus 2013-09-03T12:14:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x10 0x00    ..t.t...
    decimal
              1    0  116    0  116    0   16    0
    datetime (2013-09-03T12:14:47)
    0000   0xaf 0x4e 0x4c 0x63 0x0d                   .NLc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 47 BasalProfileStart 2013-09-03T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-03T13:00:00)
    0000   0x80 0x40 0x0d 0x03 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 48 BolusWizard 2013-09-03T13:11:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 9,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-09-03T13:11:43)
    0000   0xab 0x4b 0x0d 0x63 0x0d                   .K.c.
    body (15)
    hex
    0000   0x09 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x36          .... 6
    decimal
              9  144    0  110   23   54    0    0
             32    0    0    0    0   32   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 2.9, 'curve': 4},
 {'age': 250, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0x3c 0x04 0x6c 0xfa 0x04    \.t<.l..
    decimal
             92    8  116   60    4  108  250    4
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-09-03T13:11:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x60 0x00    .. . .`.
    decimal
              1    0   32    0   32    0   96    0
    datetime (2013-09-03T13:11:43)
    0000   0xab 0x4b 0x4d 0x63 0x0d                   .KMc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 CalBGForPH 2013-09-03T13:50:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-09-03T13:50:46)
    0000   0xae 0x72 0x4d 0x03 0x0d                   .rM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 52 BolusWizard 2013-09-03T13:50:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 9.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-09-03T13:50:51)
    0000   0xb3 0x72 0x0d 0x63 0x0d                   .r.c.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x60 0x00    ...n.6`.
    0008   0x00 0x00 0x00 0x64 0x00 0x00 0x36         ...d..6
    decimal
              0  144    0  110   23   54   96    0
              0    0    0  100    0    0   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 0.8, 'curve': 4},
 {'age': 99, 'amount': 2.9, 'curve': 4},
 {'age': 33, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x20 0x27 0x04 0x74 0x63 0x04    \. '.tc.
    0008   0x6c 0x21 0x14                             l!.
    decimal
             92   11   32   39    4  116   99    4
            108   33   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-09-03T13:50:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x64 0x00    .. . .d.
    decimal
              1    0   32    0   32    0  100    0
    datetime (2013-09-03T13:50:51)
    0000   0xb3 0x72 0x4d 0x63 0x0d                   .rMc.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2013-09-03T14:52:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T14:52:08)
    0000   0x88 0x74 0x0e 0x63 0x0d                   .t.c.
    body (15)
    hex
    0000   0x20 0x90 0x00 0x6e 0x17 0x36 0x00 0x00     ..n.6..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x36         t....t6
    decimal
             32  144    0  110   23   54    0    0
            116    0    0    0    0  116   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 0.675, 'curve': 4},
 {'age': 71, 'amount': 0.125, 'curve': 4},
 {'age': 101, 'amount': 0.8, 'curve': 4},
 {'age': 161, 'amount': 2.9, 'curve': 4},
 {'age': 95, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x1b 0x3d 0x04 0x05 0x47 0x04    \..=..G.
    0008   0x20 0x65 0x04 0x74 0xa1 0x04 0x6c 0x5f     e.t..l_
    0010   0x14                                       .
    decimal
             92   17   27   61    4    5   71    4
             32  101    4  116  161    4  108   95
             20
    datetime (unknown)

    body (0)

#### RECORD 57 CalBGForPH 2013-09-03T15:40:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-09-03T15:40:51)
    0000   0xb3 0x68 0x4f 0x03 0x0d                   .hO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2013-09-03T15:40:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 157,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 17.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2013-09-03T15:40:56)
    0000   0xb8 0x68 0x0f 0x63 0x0d                   .h.c.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xb0 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x28 0x00 0x88 0x36         ...(..6
    decimal
              0  144    0  110   23   54  176    0
              0    0    0   40    0  136   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 0.675, 'curve': 4},
 {'age': 119, 'amount': 0.125, 'curve': 4},
 {'age': 149, 'amount': 0.8, 'curve': 4},
 {'age': 209, 'amount': 2.9, 'curve': 4},
 {'age': 143, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x1b 0x6d 0x04 0x05 0x77 0x04    \..m..w.
    0008   0x20 0x95 0x04 0x74 0xd1 0x04 0x6c 0x8f     ..t..l.
    0010   0x14                                       .
    decimal
             92   17   27  109    4    5  119    4
             32  149    4  116  209    4  108  143
             20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-09-03T15:40:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x28 0x00    ......(.
    decimal
              1    0  136    0  136    0   40    0
    datetime (2013-09-03T15:40:56)
    0000   0xb8 0x68 0x4f 0x63 0x0d                   .hOc.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 BolusWizard 2013-09-03T17:03:23 head[2], body[15] op[0x5b]
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
    datetime (2013-09-03T17:03:23)
    0000   0x97 0x43 0x11 0x63 0x0d                   .C.c.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 3.3, 'curve': 4},
 {'age': 92, 'amount': 0.1, 'curve': 4},
 {'age': 192, 'amount': 0.675, 'curve': 4},
 {'age': 202, 'amount': 0.125, 'curve': 4},
 {'age': 232, 'amount': 0.8, 'curve': 4},
 {'age': 36, 'amount': 2.9, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x84 0x52 0x04 0x04 0x5c 0x04    \..R..\.
    0008   0x1b 0xc0 0x04 0x05 0xca 0x04 0x20 0xe8    ...... .
    0010   0x04 0x74 0x24 0x14                        .t$.
    decimal
             92   20  132   82    4    4   92    4
             27  192    4    5  202    4   32  232
              4  116   36   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-09-03T17:03:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x68 0x00    ..H.H.h.
    decimal
              1    0   72    0   72    0  104    0
    datetime (2013-09-03T17:03:23)
    0000   0x97 0x43 0x51 0x63 0x0d                   .CQc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 BolusWizard 2013-09-03T17:53:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T17:53:17)
    0000   0x91 0x75 0x11 0x63 0x0d                   .u.c.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 1.8, 'curve': 4},
 {'age': 132, 'amount': 3.3, 'curve': 4},
 {'age': 142, 'amount': 0.1, 'curve': 4},
 {'age': 242, 'amount': 0.675, 'curve': 4},
 {'age': 252, 'amount': 0.125, 'curve': 4},
 {'age': 26, 'amount': 0.8, 'curve': 20},
 {'age': 86, 'amount': 2.9, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x48 0x34 0x04 0x84 0x84 0x04    \.H4....
    0008   0x04 0x8e 0x04 0x1b 0xf2 0x04 0x05 0xfc    ........
    0010   0x04 0x20 0x1a 0x14 0x74 0x56 0x14         . ..tV.
    decimal
             92   23   72   52    4  132  132    4
              4  142    4   27  242    4    5  252
              4   32   26   20  116   86   20
    datetime (unknown)

    body (0)

#### RECORD 66 Ian69 2013-09-03T17:53:17 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-03T17:53:17)
    0000   0x91 0x75 0x71 0x03 0x0d                   .uq..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 1]
#### RECORD 67 Bolus 2013-09-03T17:53:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x74 0x00    ..L.L.t.
    decimal
              1    0   76    0   76    0  116    0
    datetime (2013-09-03T17:53:17)
    0000   0x91 0x75 0x51 0x63 0x0d                   .uQc.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-8.data: 68 records`
