## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 78, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x34 0x64 0x5c 0x0b 0x3c 0xbd 0x80 0x6c    4d\.<..l
    0008   0x0d 0x90 0x90 0x17 0x90 0x01 0x00 0x34    .......4
    0010   0x00 0x34 0x00 0x00 0x00 0x39 0xcb 0x4f    .4...9.O
    0018   0x08 0x0e 0x0a 0x6a 0x06 0xc9 0x30 0x08    ...j..0.
##### DEBUG DECIMAL
             52  100   92   11   60  189  128  108
             13  144  144   23  144    1    0   52
              0   52    0    0    0   57  203   79
              8   14   10  106    6  201   48    8
#### RECORD 0 BolusWizard 2014-03-08T12:08:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2014-03-08T12:08:30)
    0000   0x1e 0xc8 0x0c 0x68 0x0e                   ...h.
    body (13)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x38 0x00    .P.x2P8.
    0008   0x00 0x00 0x00 0x2c 0x00                   ...,.
    decimal
              0   80    0  120   50   80   56    0
              0    0    0   44    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 ClearAlarm 2000-04-22T12:08:28 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x64                                  .d
    decimal
             12  100
    datetime (2000-04-22T12:08:28)
    0000   0x5c 0x08 0x6c 0x56 0x80                   \.lV.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 Base (2000, 8, 28, 0, 1, 0) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x60                                  .`
    decimal
            144   96
    datetime ((2000, 8, 28, 0, 1, 0))
    0000   0x80 0x01 0x00 0x3c 0x00                   ...<.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 3 Base (2012, 0, 8, 30, 0, 44) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x00                                  <.
    decimal
             60    0
    datetime ((2012, 0, 8, 30, 0, 44))
    0000   0x2c 0x00 0x1e 0xc8 0x4c                   ,...L
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2015, 2, 11, 23, 39, 10) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x0e                                  h.
    decimal
            104   14
    datetime ((2015, 2, 11, 23, 39, 10))
    0000   0x0a 0xa7 0x17 0xcb 0x2f                   ..../
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 5 Base (2015, 0, 11, 23, 20, 63) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x0e                                  h.
    decimal
            104   14
    datetime ((2015, 0, 11, 23, 20, 63))
    0000   0x3f 0x14 0x17 0xcb 0xef                   ?....
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 6 Base (2007, 14, 27, 5, 9, 2) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x0e                                  h.
    decimal
            104   14
    datetime ((2007, 14, 27, 5, 9, 2))
    0000   0xc2 0x89 0x65 0x5b 0xa7                   ..e[.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 7 Base (2000, 0, 0, 14, 8, 15) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0xcb                                  9.
    decimal
             57  203
    datetime ((2000, 0, 0, 14, 8, 15))
    0000   0x0f 0x08 0x0e 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2000, 1, 0, 20, 16, 50) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 1, 0, 20, 16, 50))
    0000   0x32 0x50 0x34 0x00 0x00                   2P4..
    body (0)
    HOUR BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-6.data: 9 records`
