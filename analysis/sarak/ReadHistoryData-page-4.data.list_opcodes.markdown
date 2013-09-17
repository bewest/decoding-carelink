## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 29, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x82 0x21 0x4c 0x1b 0x0d 0x0a 0x7f 0xb8    .!L.....
    0008   0x12 0x2d 0x1b 0x0d 0x5b 0x7f 0x81 0x13    .-..[...
    0010   0x0d 0x1b 0x0d 0x0d 0x50 0x00 0x78 0x3c    ....P.x<
    0018   0x64 0x04 0x00 0x28 0x00 0x00 0x28 0x00    d..(..(.
##### DEBUG DECIMAL
            130   33   76   27   13   10  127  184
             18   45   27   13   91  127  129   19
             13   27   13   13   80    0  120   60
            100    4    0   40    0    0   40    0
#### RECORD 0 BolusWizard 2013-08-27T12:33:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-08-27T12:33:02)
    0000   0x82 0x21 0x0c 0x1b 0x0d                   .!...
    body (13)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00                   0....
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Base (2000, 0, 0, 16, 0, 1) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x78                                  0x
    decimal
             48  120
    datetime ((2000, 0, 0, 16, 0, 1))
    0000   0x01 0x00 0x30 0x00 0x30                   ..0.0
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-4.data: 2 records`
