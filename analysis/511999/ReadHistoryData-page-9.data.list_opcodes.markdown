## START logs/ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 114, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0f 0x0d 0x00 0x1d 0x00 0x07 0x00 0x00    ........
    0008   0x04 0x8c 0x8e 0x0d 0x00 0x00 0x00 0x6e    .......n
    0010   0x8e 0x0d 0x05 0x00 0xc2 0x00 0x00 0x06    ........
    0018   0x00 0x00 0x04 0x8c 0x02 0xdc 0x3f 0x01    ......?.
##### DEBUG DECIMAL
             15   13    0   29    0    7    0    0
              4  140  142   13    0    0    0  110
            142   13    5    0  194    0    0    6
              0    0    4  140    2  220   63    1
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
#### RECORD 1 BolusWizard 2013-08-14T20:04:55 head[2], body[15] op[0x5b]
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
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x74 0x00    .Q.d<dt.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x78         .....tx
    decimal
              0   81    0  100   60  100  116    0
              0    0    0    0    0  116  120

#### RECORD 2 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 0.3, 'curve': 192},
 {'age': 5, 'amount': 1.4, 'curve': 208},
 {'age': 35, 'amount': 1.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0xb5 0xc0 0x38 0x05 0xd0    \....8..
    0008   0x38 0x23 0xd0                             8#.
    decimal
             92   11   12  181  192   56    5  208
             56   35  208
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus (2007, 4, 0, 0, 0, 52) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x74 0x00                        ..t.
    decimal
              1    0  116    0
    datetime ((2007, 4, 0, 0, 0, 52))
    0000   0x74 0x00 0x00 0x00 0xb7                   t....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 4 Base (2009, 0, 3, 10, 13, 14) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x54                                  .T
    decimal
              4   84
    datetime ((2009, 0, 3, 10, 13, 14))
    0000   0x0e 0x0d 0x0a 0x63 0xa9                   ...c.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 5 Base (2012, 2, 3, 27, 13, 14) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x35                                  -5
    decimal
             45   53
    datetime ((2012, 2, 3, 27, 13, 14))
    0000   0x0e 0x8d 0x5b 0x63 0xac                   ..[c.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 6 Base (2000, 4, 17, 0, 13, 46) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x15                                  -.
    decimal
             45   21
    datetime ((2000, 4, 17, 0, 13, 46))
    0000   0x6e 0x0d 0x00 0x51 0x00                   n..Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 ChangeTimeDisplay (2000, 6, 0, 0, 28, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 6, 0, 0, 28, 36))
    0000   0x64 0x9c 0x00 0x00 0x00                   d....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 Base (2014, 1, 28, 24, 48, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2c                                  .,
    decimal
              0   44
    datetime ((2014, 1, 28, 24, 48, 0))
    0000   0x00 0x70 0x78 0x5c 0x0e                   .px\.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 9 Base (2008, 12, 16, 26, 12, 0) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x66                                  tf
    decimal
            116  102
    datetime ((2008, 12, 16, 26, 12, 0))
    0000   0xc0 0x0c 0x1a 0xd0 0x38                   ....8
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 10 Base (2000, 2, 1, 16, 8, 56) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xd0                                  j.
    decimal
            106  208
    datetime ((2000, 2, 1, 16, 8, 56))
    0000   0x38 0x88 0xd0 0x01 0x00                   8....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 Base (2012, 4, 0, 12, 0, 48) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x00                                  p.
    decimal
            112    0
    datetime ((2012, 4, 0, 12, 0, 48))
    0000   0x70 0x00 0x2c 0x00 0xac                   p.,..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 12 Base (2000, 4, 0, 27, 13, 46) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x55                                  -U
    decimal
             45   85
    datetime ((2000, 4, 0, 27, 13, 46))
    0000   0x6e 0x0d 0x7b 0x00 0x80                   n.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-9.data: 13 records`
