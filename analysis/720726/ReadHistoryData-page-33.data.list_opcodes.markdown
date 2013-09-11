## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 73, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x06 0xa0 0x03 0x52 0x32 0x03 0x4e 0x32    ...R2.N2
    0008   0x00 0xde 0x02 0x92 0x00 0x50 0x00 0x6c    .....P.l
    0010   0x00 0x00 0x08 0x01 0x01 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              6  160    3   82   50    3   78   50
              0  222    2  146    0   80    0  108
              0    0    8    1    1    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 BolusWizard 2013-07-27T22:33:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 20.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2013-07-27T22:33:03)
    0000   0x43 0xe1 0x16 0x7b 0x0d                   C..{.
    body (13)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0xcc 0x00                   .....
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  204    0
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2004, 4, 16, 16, 20, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x36                                  .6
    decimal
              0   54
    datetime ((2004, 4, 16, 16, 20, 28))
    0000   0x5c 0x14 0x50 0x30 0x04                   \.P0.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 2 Base (2008, 2, 4, 4, 12, 4) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x3a                                  .:
    decimal
             28   58
    datetime ((2008, 2, 4, 4, 12, 4))
    0000   0x04 0x8c 0x44 0x04 0x48                   ..D.H
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 3 Base (2010, 5, 30, 20, 48, 10) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x14                                  f.
    decimal
            102   20
    datetime ((2010, 5, 30, 20, 48, 10))
    0000   0x4a 0x70 0x14 0x3e 0x7a                   Jp.>z
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 4 SelectBasalProfile (2012, 1, 0, 0, 0, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x7b                                  .{
    decimal
             20  123
    datetime ((2012, 1, 0, 0, 0, 0))
    0000   0x00 0x40 0xc0 0x00 0x1c                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Base (2000, 0, 0, 7, 0, 32) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2000, 0, 0, 7, 0, 32))
    0000   0x20 0x00 0x07 0x00 0x00                    ....
    body (0)

#### RECORD 6 NoDelivery (2011, 0, 14, 0, 0, 0) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0xa0 0x7b 0x8d                        ..{.
    decimal
              6  160  123  141
    datetime ((2011, 0, 14, 0, 0, 0))
    0000   0x00 0x00 0x00 0x6e 0x7b                   ...n{
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 7 Base (2004, 2, 24, 11, 35, 0) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x06                                  ..
    decimal
            141    6
    datetime ((2004, 2, 24, 11, 35, 0))
    0000   0x00 0xa3 0x6b 0xf8 0x04                   ..k..
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-33.data: 8 records`
