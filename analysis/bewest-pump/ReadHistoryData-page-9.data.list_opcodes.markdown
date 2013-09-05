## START logs/ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 78, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2c 0x00 0x70 0x78 0x5c 0x0e 0x74 0x66    ,.px\.tf
    0008   0xc0 0x0c 0x1a 0xd0 0x38 0x6a 0xd0 0x38    ....8j.8
    0010   0x88 0xd0 0x01 0x00 0x70 0x00 0x70 0x00    ....p.p.
    0018   0x2c 0x00 0xac 0x2d 0x55 0x6e 0x0d 0x7b    ,..-Un.{
##### DEBUG DECIMAL
             44    0  112  120   92   14  116  102
            192   12   26  208   56  106  208   56
            136  208    1    0  112    0  112    0
             44    0  172   45   85  110   13  123
#### RECORD 0 CalBGForPH 2013-08-14T20:04:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 297}
```
    op hex (2)
    0000   0x0a 0x29                                  .)
    decimal
             10   41
    datetime (2013-08-14T20:04:52)
    0000   0xb4 0x04 0x34 0x0e 0x8d                   ..4..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 BolusWizard 2013-08-14T20:04:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 297,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x29                                  [)
    decimal
             91   41
    datetime (2013-08-14T20:04:55)
    0000   0xb7 0x04 0x14 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x74 0x00    .Q.d<dt.
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   81    0  100   60  100  116    0
              0    0    0    0    0

#### RECORD 2 Base (2000, 4, 21, 12, 11, 28) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x78                                  tx
    decimal
            116  120
    datetime ((2000, 4, 21, 12, 11, 28))
    0000   0x5c 0x0b 0x0c 0xb5 0xc0                   \....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 3 Base (2001, 12, 16, 3, 56, 16) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x05                                  8.
    decimal
             56    5
    datetime ((2001, 12, 16, 3, 56, 16))
    0000   0xd0 0x38 0x23 0xd0 0x01                   .8#..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0]
#### RECORD 4 Base (2000, 1, 0, 0, 52, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x74                                  .t
    decimal
              0  116
    datetime ((2000, 1, 0, 0, 52, 0))
    0000   0x00 0x74 0x00 0x00 0x00                   .t...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 Base (2003, 4, 10, 13, 14, 20) head[2], body[0] op[0xb7]

    op hex (2)
    0000   0xb7 0x04                                  ..
    decimal
            183    4
    datetime ((2003, 4, 10, 13, 14, 20))
    0000   0x54 0x0e 0x0d 0x0a 0x63                   T...c
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 Base (2003, 0, 27, 13, 14, 53) head[2], body[0] op[0xa9]

    op hex (2)
    0000   0xa9 0x2d                                  .-
    decimal
            169   45
    datetime ((2003, 0, 27, 13, 14, 53))
    0000   0x35 0x0e 0x8d 0x5b 0x63                   5..[c
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 7 Base (2001, 1, 0, 13, 46, 21) head[2], body[0] op[0xac]

    op hex (2)
    0000   0xac 0x2d                                  .-
    decimal
            172   45
    datetime ((2001, 1, 0, 13, 46, 21))
    0000   0x15 0x6e 0x0d 0x00 0x51                   .n..Q
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2000, 1, 0, 28, 36, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x64                                  .d
    decimal
              0  100
    datetime ((2000, 1, 0, 28, 36, 60))
    0000   0x3c 0x64 0x9c 0x00 0x00                   <d...
    body (0)
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-9.data: 9 records`
