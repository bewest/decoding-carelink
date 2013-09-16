## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 145, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x64 0x00 0x00 0x00 0x00 0x64 0x78 0x01    d....dx.
    0008   0x00 0x64 0x00 0x64 0x00 0x00 0x00 0x8b    .d.d....
    0010   0x39 0x49 0x64 0x0d 0x01 0x00 0x44 0x00    9Id...D.
    0018   0x44 0x00 0x5c 0x00 0xaf 0x1c 0x4a 0x04    D.\...J.
##### DEBUG DECIMAL
            100    0    0    0    0  100  120    1
              0  100    0  100    0    0    0  139
             57   73  100   13    1    0   68    0
             68    0   92    0  175   28   74    4
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

#### RECORD 2 Bolus 2013-08-03T17:45:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x0c 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   12    0
    datetime (2013-08-03T17:45:10)
    0000   0x8a 0x2d 0x51 0x03 0x0d                   .-Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 TempBasal 2013-08-03T19:09:00 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.25}
```
    op hex (2)
    0000   0x33 0x5a                                  3Z
    decimal
             51   90
    datetime (2013-08-03T19:09:00)
    0000   0x80 0x09 0x13 0x03 0x0d                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 4 TempBasalDuration 2013-08-03T19:09:00 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 1440}
```
    op hex (2)
    0000   0x16 0x30                                  .0
    decimal
             22   48
    datetime (2013-08-03T19:09:00)
    0000   0x80 0x09 0x13 0x03 0x0d                   .....
    body (0)

#### RECORD 5 ResultTotals (2000, 8, 0, 0, 13, 3) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x46                   ....F
    decimal
              7    0    0    4   70
    datetime ((2000, 8, 0, 0, 13, 3))
    0000   0x83 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x83 0x0d 0x05 0x00 0xa2 0x00 0x00    n.......
    0008   0x02 0x00 0x00 0x04 0x46 0x02 0xbe 0x40    ....F..@
    0010   0x01 0x88 0x24 0x00 0x32 0x00 0x58 0x00    ..$.2.X.
    0018   0x00 0x00 0x98 0x00 0x98 0x01 0x00 0x01    ........
    0020   0x03 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6d 0xd7 0x00 0x00 0x00 0x00    ..m.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  131   13    5    0  162    0    0
              2    0    0    4   70    2  190   64
              1  136   36    0   50    0   88    0
              0    0  152    0  152    1    0    1
              3    0    0    0    0    0    0    0
              0    0  109  215    0    0    0    0
              0    0    0

#### RECORD 6 Base (2004, 6, 9, 25, 2, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2004, 6, 9, 25, 2, 61))
    0000   0x7d 0x82 0x39 0x29 0x04                   }.9).
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1]
#### RECORD 7 Base (2004, 6, 9, 25, 11, 61) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2004, 6, 9, 25, 11, 61))
    0000   0x7d 0x8b 0x39 0x09 0x64                   }.9.d
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 Base (2004, 4, 28, 24, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1e                                  ..
    decimal
             13   30
    datetime ((2004, 4, 28, 24, 0, 16))
    0000   0x50 0x00 0x78 0x3c 0x64                   P.x<d
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
`end logs/ReadHistoryData-page-15.data: 9 records`
