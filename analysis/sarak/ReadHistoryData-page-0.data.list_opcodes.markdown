## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 101, found 921 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x74 0x42                                  tB
##### DEBUG DECIMAL
            116   66
#### RECORD 0 BolusWizard 2013-09-04T14:17:33 head[2], body[13] op[0x5b]
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
    body (13)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x14 0x00                   (....
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   20    0
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Base (2000, 4, 25, 4, 8, 28) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x78                                  (x
    decimal
             40  120
    datetime ((2000, 4, 25, 4, 8, 28))
    0000   0x5c 0x08 0x44 0x79 0xc0                   \.Dy.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 Base (2000, 12, 8, 0, 1, 16) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x4b                                  <K
    decimal
             60   75
    datetime ((2000, 12, 8, 0, 1, 16))
    0000   0xd0 0x01 0x00 0x28 0x00                   ...(.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 3 Base (2014, 0, 17, 1, 0, 20) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x00                                  (.
    decimal
             40    0
    datetime ((2014, 0, 17, 1, 0, 20))
    0000   0x14 0x00 0xa1 0x51 0x4e                   ...QN
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2015, 3, 20, 20, 60, 10) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x0d                                  ..
    decimal
              4   13
    datetime ((2015, 3, 20, 20, 60, 10))
    0000   0x0a 0xfc 0xb4 0x54 0x2f                   ...T/
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 5 Base (2015, 7, 20, 23, 60, 27) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x0d                                  ..
    decimal
              4   13
    datetime ((2015, 7, 20, 23, 60, 27))
    0000   0x5b 0xfc 0xb7 0x54 0x0f                   [..T.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2012, 1, 24, 0, 16, 0) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x0d                                  ..
    decimal
              4   13
    datetime ((2012, 1, 24, 0, 16, 0))
    0000   0x00 0x50 0x00 0x78 0x3c                   .P.x<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 7 ChangeTimeDisplay (2012, 0, 0, 0, 0, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x58                                  dX
    decimal
            100   88
    datetime ((2012, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x1c                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2000, 5, 8, 11, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x3c                                  .<
    decimal
              0   60
    datetime ((2000, 5, 8, 11, 28, 56))
    0000   0x78 0x5c 0x0b 0x28 0x40                   x\.(@
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 9 Base (2000, 11, 10, 28, 0, 56) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x44                                  .D
    decimal
            192   68
    datetime ((2000, 11, 10, 28, 0, 56))
    0000   0xb8 0xc0 0x3c 0x8a 0xd0                   ..<..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 10 Bolus (2007, 0, 0, 28, 0, 60) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x3c 0x00                        ..<.
    decimal
              1    0   60    0
    datetime ((2007, 0, 0, 28, 0, 60))
    0000   0x3c 0x00 0x1c 0x00 0xb7                   <....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 11 Base (2000, 0, 0, 0, 13, 4) head[2], body[0] op[0x54]

    op hex (2)
    0000   0x54 0x4f                                  TO
    decimal
             84   79
    datetime ((2000, 0, 0, 0, 13, 4))
    0000   0x04 0x0d 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-0.data: 12 records`
