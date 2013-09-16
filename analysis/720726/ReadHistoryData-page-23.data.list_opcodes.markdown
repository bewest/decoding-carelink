## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2f 0x50                                  /P
##### DEBUG DECIMAL
             47   80
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 2.1, 'curve': 4},
 {'age': 165, 'amount': 3.8, 'curve': 4},
 {'age': 89, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x54 0x41 0x04 0x98 0xa5 0x04    \.TA....
    0008   0x6c 0x59 0x14                             lY.
    decimal
             92   11   84   65    4  152  165    4
            108   89   20
    datetime (unknown)

    body (0)

#### RECORD 1 Ian69 2013-08-11T17:40:56 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-11T17:40:56)
    0000   0xb8 0x28 0x71 0x0b 0x0d                   .(q..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Bolus 2013-08-11T17:40:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 19.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0x68 0x00    ......h.
    decimal
              1    0  192    0  192    0  104    0
    datetime (2013-08-11T17:40:56)
    0000   0xb8 0x28 0x51 0x6b 0x0d                   .(Qk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2013-08-11T18:47:00 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T18:47:00)
    0000   0x80 0x2f 0x12 0x6b 0x0d                   ./.k.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 4.8, 'curve': 4},
 {'age': 132, 'amount': 2.1, 'curve': 4},
 {'age': 232, 'amount': 3.8, 'curve': 4},
 {'age': 156, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xc0 0x48 0x04 0x54 0x84 0x04    \..H.T..
    0008   0x98 0xe8 0x04 0x6c 0x9c 0x14              ...l..
    decimal
             92   14  192   72    4   84  132    4
            152  232    4  108  156   20
    datetime (unknown)

    body (0)

#### RECORD 5 BolusWizard 2013-08-11T18:47:03 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T18:47:03)
    0000   0x83 0x2f 0x12 0x6b 0x0d                   ./.k.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 4.8, 'curve': 4},
 {'age': 132, 'amount': 2.1, 'curve': 4},
 {'age': 232, 'amount': 3.8, 'curve': 4},
 {'age': 156, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xc0 0x48 0x04 0x54 0x84 0x04    \..H.T..
    0008   0x98 0xe8 0x04 0x6c 0x9c 0x14              ...l..
    decimal
             92   14  192   72    4   84  132    4
            152  232    4  108  156   20
    datetime (unknown)

    body (0)

#### RECORD 7 BolusWizard 2013-08-11T18:47:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-11T18:47:08)
    0000   0x88 0x2f 0x12 0x6b 0x0d                   ./.k.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 4.8, 'curve': 4},
 {'age': 132, 'amount': 2.1, 'curve': 4},
 {'age': 232, 'amount': 3.8, 'curve': 4},
 {'age': 156, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xc0 0x48 0x04 0x54 0x84 0x04    \..H.T..
    0008   0x98 0xe8 0x04 0x6c 0x9c 0x14              ...l..
    decimal
             92   14  192   72    4   84  132    4
            152  232    4  108  156   20
    datetime (unknown)

    body (0)

#### RECORD 9 LowReservoir 2013-08-11T18:47:08 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 3.2}
```
    op hex (2)
    0000   0x34 0x20                                  4 
    decimal
             52   32
    datetime (2013-08-11T18:47:08)
    0000   0x88 0x2f 0x12 0x0b 0x8d                   ./...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 Bolus 2013-08-11T18:47:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xbc 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  188    0
    datetime (2013-08-11T18:47:08)
    0000   0x88 0x2f 0x52 0x6b 0x0d                   ./Rk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 BolusWizard 2013-08-11T20:20:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-11T20:20:59)
    0000   0xbb 0x14 0x14 0x6b 0x0d                   ...k.
    body (15)
    hex
    0000   0x0d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x2c 0x00 0x00 0x00 0x00 0x2c 0x36         ,....,6
    decimal
             13  144    0  110   23   54    0    0
             44    0    0    0    0   44   54
    DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 2.5, 'curve': 4},
 {'age': 165, 'amount': 4.8, 'curve': 4},
 {'age': 225, 'amount': 2.1, 'curve': 4},
 {'age': 69, 'amount': 3.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x64 0x5f 0x04 0xc0 0xa5 0x04    \.d_....
    0008   0x54 0xe1 0x04 0x98 0x45 0x14              T...E.
    decimal
             92   14  100   95    4  192  165    4
             84  225    4  152   69   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-11T20:20:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x70 0x00    ..,.,.p.
    decimal
              1    0   44    0   44    0  112    0
    datetime (2013-08-11T20:20:59)
    0000   0xbb 0x14 0x54 0x6b 0x0d                   ..Tk.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 14 BolusWizard 2013-08-11T21:20:24 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T21:20:24)
    0000   0x98 0x14 0x15 0x6b 0x0d                   ...k.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 1.1, 'curve': 4},
 {'age': 155, 'amount': 2.5, 'curve': 4},
 {'age': 225, 'amount': 4.8, 'curve': 4},
 {'age': 29, 'amount': 2.1, 'curve': 20},
 {'age': 129, 'amount': 3.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0x41 0x04 0x64 0x9b 0x04    \.,A.d..
    0008   0xc0 0xe1 0x04 0x54 0x1d 0x14 0x98 0x81    ...T....
    0010   0x14                                       .
    decimal
             92   17   44   65    4  100  155    4
            192  225    4   84   29   20  152  129
             20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-08-11T21:20:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x4c 0x00    ..x.x.L.
    decimal
              1    0  120    0  120    0   76    0
    datetime (2013-08-11T21:20:25)
    0000   0x99 0x14 0x55 0x6b 0x0d                   ..Uk.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 17 Bolus 2013-08-11T22:27:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x74 0x00    ..(.(.t.
    decimal
              1    0   40    0   40    0  116    0
    datetime (2013-08-11T22:27:59)
    0000   0xbb 0x1b 0x56 0x6b 0x0d                   ..Vk.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 18 Rewind 2013-08-11T23:02:59 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-11T23:02:59)
    0000   0xbb 0x02 0x17 0x0b 0x0d                   .....
    body (0)

#### RECORD 19 Prime 2013-08-11T23:04:26 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 5.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x3a                   ....:
    decimal
              3    0    0    0   58
    datetime (2013-08-11T23:04:26)
    0000   0x9a 0x04 0x37 0x0b 0x0d                   ..7..
    body (0)

#### RECORD 20 BasalProfileStart 2013-08-11T23:04:43 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-11T23:04:43)
    0000   0xab 0x04 0x17 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 21 BolusWizard 2013-08-11T23:04:59 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T23:04:59)
    0000   0xbb 0x04 0x17 0x6b 0x0d                   ...k.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 1.0, 'curve': 4},
 {'age': 109, 'amount': 3.0, 'curve': 4},
 {'age': 169, 'amount': 1.1, 'curve': 4},
 {'age': 3, 'amount': 2.5, 'curve': 20},
 {'age': 73, 'amount': 4.8, 'curve': 20},
 {'age': 133, 'amount': 2.1, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x28 0x27 0x04 0x78 0x6d 0x04    \.('.xm.
    0008   0x2c 0xa9 0x04 0x64 0x03 0x14 0xc0 0x49    ,..d...I
    0010   0x14 0x54 0x85 0x14                        .T..
    decimal
             92   20   40   39    4  120  109    4
             44  169    4  100    3   20  192   73
             20   84  133   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-08-11T23:04:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x70 0x00    ..h.h.p.
    decimal
              1    0  104    0  104    0  112    0
    datetime (2013-08-11T23:04:59)
    0000   0xbb 0x04 0x57 0x6b 0x0d                   ..Wk.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-08-11T23:48:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-11T23:48:56)
    0000   0xb8 0x30 0x17 0x6b 0x0d                   .0.k.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 2.55, 'curve': 4},
 {'age': 53, 'amount': 0.05, 'curve': 4},
 {'age': 83, 'amount': 1.0, 'curve': 4},
 {'age': 153, 'amount': 3.0, 'curve': 4},
 {'age': 213, 'amount': 1.1, 'curve': 4},
 {'age': 47, 'amount': 2.5, 'curve': 20},
 {'age': 117, 'amount': 4.8, 'curve': 20},
 {'age': 177, 'amount': 2.1, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x66 0x2b 0x04 0x02 0x35 0x04    \.f+..5.
    0008   0x28 0x53 0x04 0x78 0x99 0x04 0x2c 0xd5    (S.x..,.
    0010   0x04 0x64 0x2f 0x14 0xc0 0x75 0x14 0x54    .d/..u.T
    0018   0xb1 0x14                                  ..
    decimal
             92   26  102   43    4    2   53    4
             40   83    4  120  153    4   44  213
              4  100   47   20  192  117   20   84
            177   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-08-11T23:48:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xa0 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  160    0
    datetime (2013-08-11T23:48:56)
    0000   0xb8 0x30 0x57 0x6b 0x0d                   .0Wk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 BasalProfileStart 2013-08-12T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-12T00:00:00)
    0000   0x80 0x00 0x00 0x0c 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 28 ResultTotals (2000, 8, 0, 0, 13, 11) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xd9                   .....
    decimal
              7    0    0    7  217
    datetime ((2000, 8, 0, 0, 13, 11))
    0000   0x8b 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 29 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x8b 0x0d 0x06 0x10 0xa9 0x3e 0x14    n.....>.
    0008   0x02 0x00 0x00 0x07 0xd9 0x03 0x85 0x2d    .......-
    0010   0x04 0x54 0x37 0x00 0xf5 0x02 0x6c 0x00    .T7...l.
    0018   0x98 0x01 0x28 0x00 0x28 0x08 0x01 0x02    ..(.(...
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  139   13    6   16  169   62   20
              2    0    0    7  217    3  133   45
              4   84   55    0  245    2  108    0
            152    1   40    0   40    8    1    2
              1    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 30 BolusWizard 2013-08-12T00:41:11 head[2], body[15] op[0x5b]
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
    datetime (2013-08-12T00:41:11)
    0000   0x8b 0x29 0x00 0x6c 0x0d                   .).l.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 1.0, 'curve': 4},
 {'age': 96, 'amount': 2.55, 'curve': 4},
 {'age': 106, 'amount': 0.05, 'curve': 4},
 {'age': 136, 'amount': 1.0, 'curve': 4},
 {'age': 206, 'amount': 3.0, 'curve': 4},
 {'age': 10, 'amount': 1.1, 'curve': 20},
 {'age': 100, 'amount': 2.5, 'curve': 20},
 {'age': 170, 'amount': 4.8, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x28 0x38 0x04 0x66 0x60 0x04    \.(8.f`.
    0008   0x02 0x6a 0x04 0x28 0x88 0x04 0x78 0xce    .j.(..x.
    0010   0x04 0x2c 0x0a 0x14 0x64 0x64 0x14 0xc0    .,..dd..
    0018   0xaa 0x14                                  ..
    decimal
             92   26   40   56    4  102   96    4
              2  106    4   40  136    4  120  206
              4   44   10   20  100  100   20  192
            170   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-08-12T00:41:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x80 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  128    0
    datetime (2013-08-12T00:41:11)
    0000   0x8b 0x29 0x40 0x6c 0x0d                   .)@l.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 33 BasalProfileStart 2013-08-12T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-12T04:00:00)
    0000   0x80 0x00 0x04 0x0c 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 34 BasalProfileStart 2013-08-12T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-12T09:30:00)
    0000   0x80 0x1e 0x09 0x0c 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 35 CalBGForPH 2013-08-12T10:29:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 207}
```
    op hex (2)
    0000   0x0a 0xcf                                  ..
    decimal
             10  207
    datetime (2013-08-12T10:29:39)
    0000   0xa7 0x1d 0x2a 0x6c 0x0d                   ..*l.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 36 Ian3F 2013-08-12T10:29:39 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2013-08-12T10:29:39)
    0000   0xa7 0x1d 0xea 0x6c 0x0d                   ...l.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 37 Ian69 2013-08-12T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-12T10:30:00)
    0000   0x80 0x1e 0x0a 0x0c 0x0d                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 38 BolusWizard 2013-08-12T10:30:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-08-12T10:30:00)
    0000   0x80 0x1e 0x0a 0x6c 0x0d                   ...l.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x68 0x00    ...n.6h.
    0008   0x00 0x00 0x00 0x00 0x00 0x68 0x36         .....h6
    decimal
              0  144    0  110   23   54  104    0
              0    0    0    0    0  104   54
    DAY BITS: [0, 1, 1]
#### RECORD 39 Bolus 2013-08-12T10:30:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2013-08-12T10:30:00)
    0000   0x80 0x1e 0x4a 0x6c 0x0d                   ..Jl.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 40 BasalProfileStart 2013-08-12T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-12T13:00:00)
    0000   0x80 0x00 0x0d 0x0c 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 41 CalBGForPH 2013-08-12T13:21:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 207}
```
    op hex (2)
    0000   0x0a 0xcf                                  ..
    decimal
             10  207
    datetime (2013-08-12T13:21:15)
    0000   0x8f 0x15 0x2d 0x6c 0x0d                   ..-l.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 42 Ian3F 2013-08-12T13:21:15 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2013-08-12T13:21:15)
    0000   0x8f 0x15 0xed 0x6c 0x0d                   ...l.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2013-08-12T13:21:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-08-12T13:21:25)
    0000   0x99 0x15 0x0d 0x6c 0x0d                   ...l.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x68 0x00    ...n.6h.
    0008   0x6c 0x00 0x00 0x14 0x00 0xc0 0x36         l.....6
    decimal
             30  144    0  110   23   54  104    0
            108    0    0   20    0  192   54
    DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 176, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0xb0 0x04                   \.h..
    decimal
             92    5  104  176    4
    datetime (unknown)

    body (0)

#### RECORD 45 Ian69 2013-08-12T13:21:25 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-12T13:21:25)
    0000   0x99 0x15 0x0d 0x0c 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 46 Bolus 2013-08-12T13:21:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 19.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0x14 0x00    ........
    decimal
              1    0  192    0  192    0   20    0
    datetime (2013-08-12T13:21:25)
    0000   0x99 0x15 0x4d 0x6c 0x0d                   ..Ml.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-08-12T14:02:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-12T14:02:20)
    0000   0x94 0x02 0x0e 0x6c 0x0d                   ...l.
    body (15)
    hex
    0000   0x0d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x2c 0x00 0x00 0x00 0x00 0x2c 0x36         ,....,6
    decimal
             13  144    0  110   23   54    0    0
             44    0    0    0    0   44   54
    DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 4.8, 'curve': 4},
 {'age': 217, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x2f 0x04 0x68 0xd9 0x04    \../.h..
    decimal
             92    8  192   47    4  104  217    4
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-08-12T14:02:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0xb4 0x00    ..,.,...
    decimal
              1    0   44    0   44    0  180    0
    datetime (2013-08-12T14:02:20)
    0000   0x94 0x02 0x4e 0x6c 0x0d                   ..Nl.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 50 CalBGForPH 2013-08-12T16:37:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-08-12T16:37:35)
    0000   0xa3 0x25 0x30 0x6c 0x0d                   .%0l.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 Ian3F 2013-08-12T16:37:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2013-08-12T16:37:35)
    0000   0xa3 0x25 0x10 0x6c 0x0d                   .%.l.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 Ian69 2013-08-12T21:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-12T21:30:00)
    0000   0x80 0x1e 0x75 0x0c 0x0d                   ..u..
    body (2)
    hex
    0000   0x35 0x1e                                  5.
    decimal
             53   30

#### RECORD 53 BolusWizard 2013-08-12T23:04:03 head[2], body[15] op[0x5b]
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
    datetime (2013-08-12T23:04:03)
    0000   0x83 0x04 0x17 0x6c 0x0d                   ...l.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 54 Bolus 2013-08-12T23:04:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x00 0x00    ........
    decimal
              1    0  148    0  148    0    0    0
    datetime (2013-08-12T23:04:03)
    0000   0x83 0x04 0x57 0x6c 0x0d                   ..Wl.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 55 CalBGForPH 2013-08-12T23:12:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 152}
```
    op hex (2)
    0000   0x0a 0x98                                  ..
    decimal
             10  152
    datetime (2013-08-12T23:12:43)
    0000   0xab 0x0c 0x37 0x6c 0x0d                   ..7l.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 56 Ian3F 2013-08-12T23:12:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-08-12T23:12:43)
    0000   0xab 0x0c 0x17 0x6c 0x0d                   ...l.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 57 BasalProfileStart 2013-08-13T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-13T00:00:00)
    0000   0x80 0x00 0x00 0x0d 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 58 ResultTotals (2000, 8, 0, 0, 13, 12) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa1                   .....
    decimal
              7    0    0    5  161
    datetime ((2000, 8, 0, 0, 13, 12))
    0000   0x8c 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 59 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x8c 0x0d 0x06 0x00 0xb0 0x88 0xcf    n.......
    0008   0x04 0x00 0x00 0x05 0xa1 0x03 0x89 0x3f    .......?
    0010   0x02 0x18 0x25 0x00 0x5a 0x00 0x5c 0x00    ..%.Z.\.
    0018   0x68 0x01 0x54 0x00 0x00 0x02 0x01 0x02    h.T.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  140   13    6    0  176  136  207
              4    0    0    5  161    3  137   63
              2   24   37    0   90    0   92    0
            104    1   84    0    0    2    1    2
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 60 BolusWizard 2013-08-13T00:54:58 head[2], body[15] op[0x5b]
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
    datetime (2013-08-13T00:54:58)
    0000   0xba 0x36 0x00 0x6d 0x0d                   .6.m.
    body (15)
    hex
    0000   0x22 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    "..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             34  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 2.3, 'curve': 4},
 {'age': 119, 'amount': 1.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x5c 0x6d 0x04 0x38 0x77 0x04    \.\m.8w.
    decimal
             92    8   92  109    4   56  119    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-08-13T00:54:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x4c 0x00    ..x.x.L.
    decimal
              1    0  120    0  120    0   76    0
    datetime (2013-08-13T00:54:58)
    0000   0xba 0x36 0x40 0x6d 0x0d                   .6@m.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 BolusWizard 2013-08-13T01:24:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-13T01:24:58)
    0000   0xba 0x18 0x01 0x6d 0x0d                   ...m.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 2.95, 'curve': 4},
 {'age': 39, 'amount': 0.05, 'curve': 4},
 {'age': 139, 'amount': 2.3, 'curve': 4},
 {'age': 149, 'amount': 1.4, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x76 0x1d 0x04 0x02 0x27 0x04    \.v...'.
    0008   0x5c 0x8b 0x04 0x38 0x95 0x04              \..8..
    decimal
             92   14  118   29    4    2   39    4
             92  139    4   56  149    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-08-13T01:24:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0xa4 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  164    0
    datetime (2013-08-13T01:24:59)
    0000   0xbb 0x18 0x41 0x6d 0x0d                   ..Am.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-08-13T02:11:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-08-13T02:11:11)
    0000   0x8b 0x0b 0x22 0x6d 0x0d                   .."m.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2013-08-13T02:11:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2013-08-13T02:11:11)
    0000   0x8b 0x0b 0xc2 0x6d 0x0d                   ...m.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2013-08-13T02:16:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-08-13T02:16:41)
    0000   0xa9 0x10 0x22 0x6d 0x0d                   .."m.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-23.data: 69 records`
