## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 79, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0x00 0x00 0x04 0x46 0x02 0xbe 0x40    ....F..@
    0008   0x01 0x88 0x24 0x00 0x32 0x00 0x58 0x00    ..$.2.X.
    0010   0x00 0x00 0x98 0x00 0x98 0x01 0x00 0x01    ........
    0018   0x03 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              2    0    0    4   70    2  190   64
              1  136   36    0   50    0   88    0
              0    0  152    0  152    1    0    1
              3    0    0    0    0    0    0    0
#### RECORD 0 BolusWizard 2013-08-03T17:45:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-03T17:45:10)
    0000   0x8a 0x2d 0x11 0x03 0x0d                   .-...
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x0c 0x00 0x58 0x78         X....Xx
    decimal
             22   80    0  100   60  100    0    0
             88    0    0   12    0   88  120
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 0.45, 'curve': 192},
 {'age': 122, 'amount': 0.55, 'curve': 192},
 {'age': 66, 'amount': 3.8, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x12 0x70 0xc0 0x16 0x7a 0xc0    \..p..z.
    0008   0x98 0x42 0xd0                             .B.
    decimal
             92   11   18  112  192   22  122  192
            152   66  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus (2010, 4, 0, 12, 0, 24) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x58 0x00                        ..X.
    decimal
              1    0   88    0
    datetime ((2010, 4, 0, 12, 0, 24))
    0000   0x58 0x00 0x0c 0x00 0x8a                   X....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Base (2000, 0, 26, 19, 13, 3) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x51                                  -Q
    decimal
             45   81
    datetime ((2000, 0, 26, 19, 13, 3))
    0000   0x03 0x0d 0x33 0x5a 0x80                   ..3Z.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 Base (2000, 0, 22, 8, 13, 3) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x13                                  ..
    decimal
              9   19
    datetime ((2000, 0, 22, 8, 13, 3))
    0000   0x03 0x0d 0x08 0x16 0x30                   ....0
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 5 Base (2000, 0, 7, 13, 3, 19) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x09                                  ..
    decimal
            128    9
    datetime ((2000, 0, 7, 13, 3, 19))
    0000   0x13 0x03 0x0d 0x07 0x00                   .....
    body (0)

#### RECORD 6 Base (2000, 6, 0, 13, 3, 6) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2000, 6, 0, 13, 3, 6))
    0000   0x46 0x83 0x0d 0x00 0x00                   F....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 Base (2002, 8, 0, 5, 13, 3) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2002, 8, 0, 5, 13, 3))
    0000   0x83 0x0d 0x05 0x00 0xa2                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
`end logs/ReadHistoryData-page-15.data: 8 records`
