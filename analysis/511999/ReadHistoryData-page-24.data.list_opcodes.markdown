## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 179, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x18 0x78 0x5c 0x08 0x0e 0xbd 0xd0 0x46    .x\....F
    0008   0xc7 0xd0 0x01 0x00 0x18 0x00 0x18 0x00    ........
    0010   0x00 0x00 0x46 0xf0 0x54 0x70 0x0d 0x0a    ..F.Tp..
    0018   0x74 0x41 0xd5 0x35 0x10 0x0d 0x5b 0x74    tA.5..[t
##### DEBUG DECIMAL
             24  120   92    8   14  189  208   70
            199  208    1    0   24    0   24    0
              0    0   70  240   84  112   13   10
            116   65  213   53   16   13   91  116
#### RECORD 0 BolusWizard 2013-07-16T11:44:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-07-16T11:44:50)
    0000   0x72 0xec 0x0b 0x10 0x0d                   r....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x24 0x00 0x00 0x78         ...$..x
    decimal
              0   80    0  120   60  100    8    0
              0    0    0   36    0    0  120
    HOUR BITS: [1, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 1.9, 'curve': 192},
 {'age': 201, 'amount': 2.7, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x5b 0xc0 0x6c 0xc9 0xc0    \.L[.l..
    decimal
             92    8   76   91  192  108  201  192
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus (2002, 4, 0, 4, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x40 0x00                        ..@.
    decimal
              1    0   64    0
    datetime ((2002, 4, 0, 4, 0, 0))
    0000   0x40 0x00 0x24 0x00 0x72                   @.$.r
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Base (2000, 0, 3, 27, 13, 16) head[2], body[0] op[0xec]

    op hex (2)
    0000   0xec 0x4b                                  .K
    decimal
            236   75
    datetime ((2000, 0, 3, 27, 13, 16))
    0000   0x10 0x0d 0x7b 0x03 0x40                   ..{.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2000, 0, 29, 24, 13, 16) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x0c                                  ..
    decimal
            192   12
    datetime ((2000, 0, 29, 24, 13, 16))
    0000   0x10 0x0d 0x18 0x1d 0x00                   .....
    body (0)

#### RECORD 5 CalBGForPH 2013-07-16T12:26:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-07-16T12:26:00)
    0000   0x40 0xda 0x2c 0x10 0x0d                   @.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 BolusWizard 2013-07-16T12:26:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 200,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc8                                  [.
    decimal
             91  200
    datetime (2013-07-16T12:26:03)
    0000   0x43 0xda 0x0c 0x10 0x0d                   C....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x34 0x00    .P.x<d4.
    0008   0x00 0x00 0x00 0x44 0x00 0x00 0x78         ...D..x
    decimal
              0   80    0  120   60  100   52    0
              0    0    0   68    0    0  120
    HOUR BITS: [1, 1, 0]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.6, 'curve': 192},
 {'age': 133, 'amount': 1.9, 'curve': 192},
 {'age': 243, 'amount': 2.7, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x2b 0xc0 0x4c 0x85 0xc0    \.@+.L..
    0008   0x6c 0xf3 0xc0                             l..
    decimal
             92   11   64   43  192   76  133  192
            108  243  192
    datetime (unknown)

    body (0)

#### RECORD 8 CalBGForPH 2013-07-16T13:21:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-07-16T13:21:30)
    0000   0x5e 0xd5 0x2d 0x10 0x0d                   ^.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 BolusWizard 2013-07-16T13:21:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-07-16T13:21:47)
    0000   0x6f 0xd5 0x0d 0x70 0x0d                   o..p.
    body (15)
    hex
    0000   0x1a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x54 0x00 0x00 0x1c 0x00 0x54 0x78         T....Tx
    decimal
             26   80    0  120   60  100    0    0
             84    0    0   28    0   84  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 1.6, 'curve': 192},
 {'age': 188, 'amount': 1.9, 'curve': 192},
 {'age': 42, 'amount': 2.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x62 0xc0 0x4c 0xbc 0xc0    \.@b.L..
    0008   0x6c 0x2a 0xd0                             l*.
    decimal
             92   11   64   98  192   76  188  192
            108   42  208
    datetime (unknown)

    body (0)

#### RECORD 11 LowReservoir 2013-07-16T13:22:02 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-16T13:22:02)
    0000   0x42 0xd6 0x0d 0x10 0x0d                   B....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 Bolus (2015, 4, 0, 28, 0, 20) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x54 0x00                        ..T.
    decimal
              1    0   84    0
    datetime ((2015, 4, 0, 28, 0, 20))
    0000   0x54 0x00 0x1c 0x00 0x6f                   T...o
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2003, 4, 29, 10, 13, 48) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x4d                                  .M
    decimal
            213   77
    datetime ((2003, 4, 29, 10, 13, 48))
    0000   0x70 0x0d 0x0a 0x9d 0x43                   p...C
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 14 Base (2005, 0, 29, 27, 13, 16) head[2], body[0] op[0xf0]

    op hex (2)
    0000   0xf0 0x34                                  .4
    decimal
            240   52
    datetime ((2005, 0, 29, 27, 13, 16))
    0000   0x10 0x0d 0x5b 0x9d 0x45                   ..[.E
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 15 Base (2000, 4, 16, 0, 13, 48) head[2], body[0] op[0xf0]

    op hex (2)
    0000   0xf0 0x14                                  ..
    decimal
            240   20
    datetime ((2000, 4, 16, 0, 13, 48))
    0000   0x70 0x0d 0x00 0x50 0x00                   p..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 16 ChangeTimeDisplay (2000, 4, 0, 0, 24, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 4, 0, 0, 24, 36))
    0000   0x64 0x18 0x00 0x00 0x00                   d....
    body (0)

`end logs/ReadHistoryData-page-24.data: 17 records`
