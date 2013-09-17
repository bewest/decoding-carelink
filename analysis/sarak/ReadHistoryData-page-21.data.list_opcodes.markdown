## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 78, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x34 0x78 0x5c 0x0b 0x10 0xce 0xc0 0x14    4x\.....
    0008   0xf6 0xc0 0x4c 0x3c 0xd0 0x01 0x00 0x34    ..L<...4
    0010   0x00 0x34 0x00 0x00 0x00 0x68 0xd3 0x4e    .4...h.N
    0018   0x76 0x0d 0x0a 0xd3 0x57 0xfb 0x30 0x16    v...W.0.
##### DEBUG DECIMAL
             52  120   92   11   16  206  192   20
            246  192   76   60  208    1    0   52
              0   52    0    0    0  104  211   78
            118   13   10  211   87  251   48   22
#### RECORD 0 BolusWizard 2013-07-22T10:57:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 205,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcd                                  [.
    decimal
             91  205
    datetime (2013-07-22T10:57:56)
    0000   0x78 0xf9 0x0a 0x76 0x0d                   x..v.
    body (13)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x38 0x00    .P.x<d8.
    0008   0x00 0x00 0x00 0x28 0x00                   ...(.
    decimal
              0   80    0  120   60  100   56    0
              0    0    0   40    0
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2000, 4, 12, 20, 8, 28) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x78                                  .x
    decimal
             16  120
    datetime ((2000, 4, 12, 20, 8, 28))
    0000   0x5c 0x08 0x14 0x2c 0xc0                   \..,.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 Base (2000, 12, 16, 0, 1, 0) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x72                                  Lr
    decimal
             76  114
    datetime ((2000, 12, 16, 0, 1, 0))
    0000   0xc0 0x01 0x00 0x10 0x00                   .....
    body (0)

#### RECORD 3 Base (2010, 0, 25, 25, 0, 40) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2010, 0, 25, 25, 0, 40))
    0000   0x28 0x00 0x79 0xf9 0x4a                   (.y.J
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2012, 4, 0, 0, 3, 59) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x0d                                  v.
    decimal
            118   13
    datetime ((2012, 4, 0, 0, 3, 59))
    0000   0x7b 0x03 0x40 0xc0 0x0c                   {.@..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 5 TempBasalDuration (2007, 0, 10, 0, 29, 24) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 390}
```
    op hex (2)
    0000   0x16 0x0d                                  ..
    decimal
             22   13
    datetime ((2007, 0, 10, 0, 29, 24))
    0000   0x18 0x1d 0x00 0x0a 0xc7                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 6 Base (2007, 0, 27, 13, 22, 46) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0xd3                                  f.
    decimal
            102  211
    datetime ((2007, 0, 27, 13, 22, 46))
    0000   0x2e 0x16 0x0d 0x5b 0xc7                   ...[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 7 Base (2000, 1, 0, 13, 54, 14) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0xd3                                  h.
    decimal
            104  211
    datetime ((2000, 1, 0, 13, 54, 14))
    0000   0x0e 0x76 0x0d 0x00 0x50                   .v..P
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2000, 1, 0, 20, 36, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 1, 0, 20, 36, 60))
    0000   0x3c 0x64 0x34 0x00 0x00                   <d4..
    body (0)
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-21.data: 9 records`
