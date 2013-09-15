## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 104, found 918 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x74 0x42                                  tB
##### DEBUG DECIMAL
            116   66
#### RECORD 0 BolusWizard 2013-09-04T14:17:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-09-04T14:17:33)
    0000   0xa1 0x51 0x0e 0x04 0x0d                   .Q...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x14 0x00 0x28 0x78         (....(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   20    0   40  120
    HOUR BITS: [0, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.7, 'curve': 192},
 {'age': 75, 'amount': 1.5, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x79 0xc0 0x3c 0x4b 0xd0    \.Dy.<K.
    decimal
             92    8   68  121  192   60   75  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus (2001, 0, 0, 20, 0, 40) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x28 0x00                        ..(.
    decimal
              1    0   40    0
    datetime ((2001, 0, 0, 20, 0, 40))
    0000   0x28 0x00 0x14 0x00 0xa1                   (....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 3 Base (2004, 0, 28, 10, 13, 4) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0x4e                                  QN
    decimal
             81   78
    datetime ((2004, 0, 28, 10, 13, 4))
    0000   0x04 0x0d 0x0a 0xfc 0xb4                   .....
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 4 Base (2007, 0, 28, 27, 13, 4) head[2], body[0] op[0x54]

    op hex (2)
    0000   0x54 0x2f                                  T/
    decimal
             84   47
    datetime ((2007, 0, 28, 27, 13, 4))
    0000   0x04 0x0d 0x5b 0xfc 0xb7                   ..[..
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 5 Base (2000, 0, 16, 0, 13, 4) head[2], body[0] op[0x54]

    op hex (2)
    0000   0x54 0x0f                                  T.
    decimal
             84   15
    datetime ((2000, 0, 16, 0, 13, 4))
    0000   0x04 0x0d 0x00 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 5, 0, 0, 24, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 5, 0, 0, 24, 36))
    0000   0x64 0x58 0x00 0x00 0x00                   dX...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 Base (2011, 0, 28, 24, 60, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2011, 0, 28, 24, 60, 0))
    0000   0x00 0x3c 0x78 0x5c 0x0b                   .<x\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2012, 13, 0, 24, 4, 0) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x40                                  (@
    decimal
             40   64
    datetime ((2012, 13, 0, 24, 4, 0))
    0000   0xc0 0x44 0xb8 0xc0 0x3c                   .D..<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 9 Base (2012, 0, 0, 28, 0, 1) head[2], body[0] op[0x8a]

    op hex (2)
    0000   0x8a 0xd0                                  ..
    decimal
            138  208
    datetime ((2012, 0, 0, 28, 0, 1))
    0000   0x01 0x00 0x3c 0x00 0x3c                   ..<.<
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 10 Base (2004, 2, 15, 20, 55, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2004, 2, 15, 20, 55, 0))
    0000   0x00 0xb7 0x54 0x4f 0x04                   ..TO.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 11 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-0.data: 12 records`
