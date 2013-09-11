## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 80, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x60 0x36 0x5c 0x14 0x30 0x8a 0x04 0x34    `6\.0..4
    0008   0x94 0x04 0x24 0xf8 0x04 0x64 0x34 0x14    ..$..d4.
    0010   0x7c 0x48 0x14 0x48 0xde 0x14 0x01 0x00    |H.H....
    0018   0x60 0x00 0x60 0x00 0x24 0x00 0x91 0x02    `.`.$...
##### DEBUG DECIMAL
             96   54   92   20   48  138    4   52
            148    4   36  248    4  100   52   20
            124   72   20   72  222   20    1    0
             96    0   96    0   36    0  145    2
#### RECORD 0 BolusWizard 2012-08-22T13:47:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 52,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.8,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x34                                  [4
    decimal
             91   52
    datetime (2012-08-22T13:47:06)
    0000   0x86 0x2f 0x0d 0x76 0x0c                   ./.v.
    body (13)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x24 0xf8 0x00 0x6c 0x00                   $..l.
    decimal
             10  144    0  110   23   54  252    0
             36  248    0  108    0
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2004, 4, 13, 20, 26, 28) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x36                                   6
    decimal
             32   54
    datetime ((2004, 4, 13, 20, 26, 28))
    0000   0x5c 0x1a 0x34 0x0d 0x04                   \.4..
    body (0)

#### RECORD 2 Base (2012, 1, 4, 13, 36, 4) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x71                                  $q
    decimal
             36  113
    datetime ((2012, 1, 4, 13, 36, 4))
    0000   0x04 0x64 0xad 0x04 0x7c                   .d..|
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Base (2011, 5, 12, 20, 23, 8) head[2], body[0] op[0xc1]

    op hex (2)
    0000   0xc1 0x04                                  ..
    decimal
            193    4
    datetime ((2011, 5, 12, 20, 23, 8))
    0000   0x48 0x57 0x14 0x6c 0x6b                   HW.lk
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 SelectBasalProfile 2004-08-15T00:20:19 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x4c                                  .L
    decimal
             20   76
    datetime (2004-08-15T00:20:19)
    0000   0x93 0x14 0xc0 0xcf 0x14                   .....
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Bolus (2006, 0, 0, 12, 0, 48) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x30 0x00                        ..0.
    decimal
              1    0   48    0
    datetime ((2006, 0, 0, 12, 0, 48))
    0000   0x30 0x00 0x6c 0x00 0x86                   0.l..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 Base (2001, 4, 0, 27, 12, 54) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0x4d                                  /M
    decimal
             47   77
    datetime ((2001, 4, 0, 27, 12, 54))
    0000   0x76 0x0c 0x5b 0x00 0x91                   v.[..
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 7 Base (2000, 4, 16, 27, 12, 54) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x10                                  ..
    decimal
              2   16
    datetime ((2000, 4, 16, 27, 12, 54))
    0000   0x76 0x0c 0x1b 0x90 0x00                   v....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 8 Base (2000, 0, 0, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 0, 0, 0, 54))
    0000   0x36 0x00 0x00 0x60 0x00                   6..`.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-15.data: 9 records`
