## START logs/ReadHistoryData-page-26.data
#### STOPPING DOUBLE NULLS @ 74, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1a 0x7d 0x5c 0x05 0x50 0x56 0x14 0x34    .}\.PV.4
    0008   0x64 0x68 0x10 0x17 0x11 0x0d 0x01 0x1a    dh......
    0010   0x1a 0x00 0x68 0x10 0x57 0x11 0x0d 0x07    ..h.W...
    0018   0x00 0x00 0x04 0xd6 0x51 0x0d 0x6d 0x51    ....Q.mQ
##### DEBUG DECIMAL
             26  125   92    5   80   86   20   52
            100  104   16   23   17   13    1   26
             26    0  104   16   87   17   13    7
              0    0    4  214   81   13  109   81
#### RECORD 0 BolusWizard 2013-04-17T17:42:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-04-17T17:42:13)
    0000   0x4d 0x2a 0x11 0x11 0x0d                   M*...
    body (15)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x01 0x14 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x14 0x7d 0x5c 0x05         ....}\.
    decimal
             27   80   13   45  106    1   20    0
              0    3    0   20  125   92    5
    HOUR BITS: [0, 0, 1]
#### RECORD 1 IanA8 (2001, 0, 24, 19, 13, 17) head[10], body[0] op[0xa8]

    op hex (10)
    0000   0xa8 0xe4 0x04 0x01 0x14 0x14 0x00 0x4d    .......M
    0008   0x2a 0x51                                  *Q
    decimal
            168  228    4    1   20   20    0   77
             42   81
    datetime ((2001, 0, 24, 19, 13, 17))
    0000   0x11 0x0d 0x33 0x18 0x41                   ..3.A
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 2 Base (2002, 0, 22, 0, 13, 17) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x15                                  ..
    decimal
              9   21
    datetime ((2002, 0, 22, 0, 13, 17))
    0000   0x11 0x0d 0x00 0x16 0x02                   .....
    body (0)

#### RECORD 3 Base (2012, 0, 10, 13, 17, 21) head[2], body[0] op[0x41]

    op hex (2)
    0000   0x41 0x09                                  A.
    decimal
             65    9
    datetime ((2012, 0, 10, 13, 17, 21))
    0000   0x15 0x11 0x0d 0x0a 0x5c                   ....\
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 4 Base (2012, 0, 27, 13, 17, 55) head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0x10                                  J.
    decimal
             74   16
    datetime ((2012, 0, 27, 13, 17, 55))
    0000   0x37 0x11 0x0d 0x5b 0x5c                   7..[\
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2000, 0, 6, 13, 17, 23) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x10                                  h.
    decimal
            104   16
    datetime ((2000, 0, 6, 13, 17, 23))
    0000   0x17 0x11 0x0d 0x26 0x50                   ...&P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 6 Base (2000, 7, 16, 29, 61, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 7, 16, 29, 61, 42))
    0000   0x6a 0xfd 0x1d 0xf0 0x00                   j....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-26.data: 7 records`
