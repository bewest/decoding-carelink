## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 337, found 99 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x04 0x72 0xcb 0x16 0x0d 0x0d 0x00    ..r.....
    0008   0x1d 0x00 0x08 0x1d 0x00 0x10 0x22 0x00    ......".
    0010   0x18 0x1d 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    4  114  203   22   13   13    0
             29    0    8   29    0   16   34    0
             24   29    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 136, 'amount': 4.45, 'curve': 192},
 {'age': 146, 'amount': 0.35, 'curve': 192},
 {'age': 236, 'amount': 1.85, 'curve': 192},
 {'age': 246, 'amount': 1.55, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0xb2 0x88 0xc0 0x0e 0x92 0xc0    \.......
    0008   0x4a 0xec 0xc0 0x3e 0xf6 0xc0              J..>..
    decimal
             92   14  178  136  192   14  146  192
             74  236  192   62  246  192
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-07-13T17:09:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x20 0x00    ..H.H. .
    decimal
              1    0   72    0   72    0   32    0
    datetime (2013-07-13T17:09:35)
    0000   0x63 0xc9 0x51 0x6d 0x0d                   c.Qm.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-07-13T18:41:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2013-07-13T18:41:42)
    0000   0x6a 0xe9 0x32 0x0d 0x0d                   j.2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2013-07-13T18:42:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 248,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0xf8                                  [.
    decimal
             91  248
    datetime (2013-07-13T18:42:21)
    0000   0x55 0xea 0x12 0x0d 0x0d                   U....
    body (15)
    hex
    0000   0x1d 0x50 0x00 0x64 0x3c 0x64 0x54 0x00    .P.d<dT.
    0008   0x74 0x00 0x00 0x1c 0x00 0xac 0x78         t.....x
    decimal
             29   80    0  100   60  100   84    0
            116    0    0   28    0  172  120
    HOUR BITS: [1, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 1.8, 'curve': 192},
 {'age': 229, 'amount': 4.45, 'curve': 192},
 {'age': 239, 'amount': 0.35, 'curve': 192},
 {'age': 73, 'amount': 1.85, 'curve': 208},
 {'age': 83, 'amount': 1.55, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x63 0xc0 0xb2 0xe5 0xc0    \.Hc....
    0008   0x0e 0xef 0xc0 0x4a 0x49 0xd0 0x3e 0x53    ...JI.>S
    0010   0xd0                                       .
    decimal
             92   17   72   99  192  178  229  192
             14  239  192   74   73  208   62   83
            208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-13T18:42:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 17.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x1c 0x00    ........
    decimal
              1    0  172    0  172    0   28    0
    datetime (2013-07-13T18:42:21)
    0000   0x55 0xea 0x52 0x0d 0x0d                   U.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 CalBGForPH 2013-07-13T19:11:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-07-13T19:11:00)
    0000   0x40 0xcb 0x33 0x0d 0x0d                   @.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 BolusWizard 2013-07-13T19:11:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 17.2,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-07-13T19:11:08)
    0000   0x48 0xcb 0x13 0x6d 0x0d                   H..m.
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x04 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0xac 0x00 0x38 0x78         8....8x
    decimal
             14   80    0  100   60  100    4    0
             56    0    0  172    0   56  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 3.35, 'curve': 192},
 {'age': 38, 'amount': 0.95, 'curve': 192},
 {'age': 128, 'amount': 1.8, 'curve': 192},
 {'age': 2, 'amount': 4.45, 'curve': 208},
 {'age': 12, 'amount': 0.35, 'curve': 208},
 {'age': 102, 'amount': 1.85, 'curve': 208},
 {'age': 112, 'amount': 1.55, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x86 0x1c 0xc0 0x26 0x26 0xc0    \....&&.
    0008   0x48 0x80 0xc0 0xb2 0x02 0xd0 0x0e 0x0c    H.......
    0010   0xd0 0x4a 0x66 0xd0 0x3e 0x70 0xd0         .Jf.>p.
    decimal
             92   23  134   28  192   38   38  192
             72  128  192  178    2  208   14   12
            208   74  102  208   62  112  208
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-07-13T19:11:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0xac 0x00    ..8.8...
    decimal
              1    0   56    0   56    0  172    0
    datetime (2013-07-13T19:11:08)
    0000   0x48 0xcb 0x53 0x6d 0x0d                   H.Sm.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 CalBGForPH 2013-07-13T20:00:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-07-13T20:00:18)
    0000   0x52 0xc0 0x34 0x0d 0x0d                   R.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BolusWizard 2013-07-13T20:00:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 14.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-07-13T20:00:26)
    0000   0x5a 0xc0 0x14 0x6d 0x0d                   Z..m.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x8c 0x00 0x58 0x78         X....Xx
    decimal
             22   80    0  100   60  100    0    0
             88    0    0  140    0   88  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 1.4, 'curve': 192},
 {'age': 77, 'amount': 3.35, 'curve': 192},
 {'age': 87, 'amount': 0.95, 'curve': 192},
 {'age': 177, 'amount': 1.8, 'curve': 192},
 {'age': 51, 'amount': 4.45, 'curve': 208},
 {'age': 61, 'amount': 0.35, 'curve': 208},
 {'age': 151, 'amount': 1.85, 'curve': 208},
 {'age': 161, 'amount': 1.55, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x38 0x39 0xc0 0x86 0x4d 0xc0    \.89..M.
    0008   0x26 0x57 0xc0 0x48 0xb1 0xc0 0xb2 0x33    &W.H...3
    0010   0xd0 0x0e 0x3d 0xd0 0x4a 0x97 0xd0 0x3e    ..=.J..>
    0018   0xa1 0xd0                                  ..
    decimal
             92   26   56   57  192  134   77  192
             38   87  192   72  177  192  178   51
            208   14   61  208   74  151  208   62
            161  208
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-07-13T20:00:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x8c 0x00    ..X.X...
    decimal
              1    0   88    0   88    0  140    0
    datetime (2013-07-13T20:00:26)
    0000   0x5a 0xc0 0x54 0x6d 0x0d                   Z.Tm.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2013-07-13T21:42:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-07-13T21:42:17)
    0000   0x51 0xea 0x35 0x0d 0x0d                   Q.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 15 BolusWizard 2013-07-13T21:42:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdd                                  [.
    decimal
             91  221
    datetime (2013-07-13T21:42:21)
    0000   0x55 0xea 0x15 0x6d 0x0d                   U..m.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x00 0x00 0x00 0x28 0x00 0x18 0x78         ...(..x
    decimal
              0   80    0  100   60  100   64    0
              0    0    0   40    0   24  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 2.2, 'curve': 192},
 {'age': 159, 'amount': 1.4, 'curve': 192},
 {'age': 179, 'amount': 3.35, 'curve': 192},
 {'age': 189, 'amount': 0.95, 'curve': 192},
 {'age': 23, 'amount': 1.8, 'curve': 208},
 {'age': 153, 'amount': 4.45, 'curve': 208},
 {'age': 163, 'amount': 0.35, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x58 0x6d 0xc0 0x38 0x9f 0xc0    \.Xm.8..
    0008   0x86 0xb3 0xc0 0x26 0xbd 0xc0 0x48 0x17    ...&..H.
    0010   0xd0 0xb2 0x99 0xd0 0x0e 0xa3 0xd0         .......
    decimal
             92   23   88  109  192   56  159  192
            134  179  192   38  189  192   72   23
            208  178  153  208   14  163  208
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-07-13T21:42:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x28 0x00    ......(.
    decimal
              1    0   24    0   24    0   40    0
    datetime (2013-07-13T21:42:21)
    0000   0x55 0xea 0x55 0x6d 0x0d                   U.Um.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 ChangeBasalProfile 2013-07-13T22:11:50 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x04                                  ..
    decimal
              8    4
    datetime (2013-07-13T22:11:50)
    0000   0x72 0xcb 0x16 0x0d 0x0d                   r....
    body (44)
    hex
    0000   0x00 0x1c 0x00 0x08 0x1c 0x00 0x10 0x23    .......#
    0008   0x00 0x18 0x1c 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
              0   28    0    8   28    0   16   35
              0   24   28    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-28.data: 19 records`
