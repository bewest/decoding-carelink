## START logs/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 29, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0f 0xc1 0x48 0x67 0x0e 0x83 0x01 0x37    ..Hg...7
    0008   0xec 0x08 0x07 0x0e 0x40 0x00 0x0c 0xed    ....@...
    0010   0x08 0x07 0x0e 0x05 0x01 0x41 0x00 0x13    .....A..
    0018   0xed 0x08 0x07 0x0e 0x00 0x7b 0x04 0x00    .....{..
##### DEBUG DECIMAL
             15  193   72  103   14  131    1   55
            236    8    7   14   64    0   12  237
              8    7   14    5    1   65    0   19
            237    8    7   14    0  123    4    0
#### RECORD 0 BolusWizard 2014-03-07T08:01:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 175,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 7.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xaf                                  [.
    decimal
             91  175
    datetime (2014-03-07T08:01:15)
    0000   0x0f 0xc1 0x08 0x67 0x0e                   ...g.
    body (13)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x48 0x00    .P.n(PH.
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   80    0  110   40   80   72    0
              0    0    0    0    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x64                                  Hd
    decimal
             72  100
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0x48 0x00 0x48                   ..H.H
    body (0)
    YEAR BITS: [0, 1, 0, 0]
`end logs/ReadHistoryData-page-7.data: 2 records`
