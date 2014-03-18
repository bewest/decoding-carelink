## START logs/ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 218, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x50 0x64 0x5c 0x17 0xbc 0x49 0x80 0xb0    Pd\..I..
    0008   0x53 0x80 0x40 0x71 0x80 0x2c 0x2f 0x90    S.@q.,/.
    0010   0x64 0x39 0x90 0xa0 0x43 0x90 0x50 0x75    d9..C.Pu
    0018   0x90 0x34 0x64 0x2a 0xd0 0x0f 0x02 0x0e    .4d*....
##### DEBUG DECIMAL
             80  100   92   23  188   73  128  176
             83  128   64  113  128   44   47  144
            100   57  144  160   67  144   80  117
            144   52  100   42  208   15    2   14
#### RECORD 0 BolusWizard 2014-03-02T10:10:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-02T10:10:20)
    0000   0x14 0xca 0x0a 0x62 0x0e                   ...b.
    body (13)
    hex
    0000   0x28 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    (P.n(P..
    0008   0x90 0x00 0x00 0x00 0x00                   .....
    decimal
             40   80    0  110   40   80    0    0
            144    0    0    0    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2000, 4, 18, 0, 11, 28) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x64                                  .d
    decimal
            144  100
    datetime ((2000, 4, 18, 0, 11, 28))
    0000   0x5c 0x0b 0xa0 0x12 0x80                   \....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 Ian50 (2001, 10, 16, 28, 12, 0) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x44                                  PD
    decimal
             80   68
    datetime ((2001, 10, 16, 28, 12, 0))
    0000   0x80 0x8c 0x5c 0x90 0x01                   ..\..
    body (34)
    hex
    0000   0x00 0x90 0x00 0x90 0x00 0xb4 0x00 0x14    ........
    0008   0xca 0x4a 0x62 0x0e 0x7b 0x04 0x00 0xde    .Jb.{...
    0010   0x0a 0x02 0x0e 0x15 0x10 0x00 0x0a 0xa1    ........
    0018   0x23 0xd9 0x2d 0x62 0x0e 0x3f 0x14 0x23    #.-b.?.#
    0020   0xd9 0x2d                                  .-
    decimal
              0  144    0  144    0  180    0   20
            202   74   98   14  123    4    0  222
             10    2   14   21   16    0   10  161
             35  217   45   98   14   63   20   35
            217   45
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0]
#### RECORD 3 Base (2008, 14, 10, 5, 9, 2) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x0e                                  b.
    decimal
             98   14
    datetime ((2008, 14, 10, 5, 9, 2))
    0000   0xc2 0x89 0x65 0x0a 0xb8                   ..e..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 4 ChangeTime 2007-01-31T14:34:45 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0xda                                  ..
    decimal
             23  218
    datetime (2007-01-31T14:34:45)
    0000   0x2d 0x62 0x0e 0x3f 0x17                   -b.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 ChangeTime 2009-01-02T14:34:13 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0xda                                  ..
    decimal
             23  218
    datetime (2009-01-02T14:34:13)
    0000   0x0d 0x62 0x0e 0xc2 0x89                   .b...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 Base (2002, 8, 13, 26, 47, 56) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x5b                                  e[
    decimal
            101   91
    datetime ((2002, 8, 13, 26, 47, 56))
    0000   0xb8 0x2f 0xda 0x0d 0x02                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 Base (2000, 4, 18, 24, 0, 16) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x00                                  ..
    decimal
             14    0
    datetime ((2000, 4, 18, 24, 0, 16))
    0000   0x50 0x00 0x78 0x32 0x50                   P.x2P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 9 Base (2000, 4, 2, 12, 14, 28) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x64                                  @d
    decimal
             64  100
    datetime ((2000, 4, 2, 12, 14, 28))
    0000   0x5c 0x0e 0x2c 0xc2 0x80                   \.,..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 ChangeTimeDisplay (2000, 10, 0, 22, 32, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0xcc                                  d.
    decimal
            100  204
    datetime ((2000, 10, 0, 22, 32, 0))
    0000   0x80 0xa0 0xd6 0x80 0x50                   ....P
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 ChangeBasalProfile (2000, 0, 0, 0, 0, 1) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x90                                  ..
    decimal
              8  144
    datetime ((2000, 0, 0, 0, 0, 1))
    0000   0x01 0x00 0x40 0x00 0x40                   ..@.@
    body (44)
    hex
    0000   0x00 0x00 0x00 0x2f 0xda 0x4d 0x02 0x0e    .../.M..
    0008   0x5b 0x00 0x09 0xc0 0x0e 0x62 0x0e 0x6e    [....b.n
    0010   0x50 0x00 0x78 0x32 0x50 0x00 0x01 0x6c    P.x2P..l
    0018   0x00 0x00 0x00 0x01 0x6c 0x64 0x5c 0x11    ....ld\.
    0020   0x40 0x26 0x80 0x2c 0xe4 0x80 0x64 0xee    @&.,..d.
    0028   0x80 0xa0 0xf8 0x80                        ....
    decimal
              0    0    0   47  218   77    2   14
             91    0    9  192   14   98   14  110
             80    0  120   50   80    0    1  108
              0    0    0    1  108  100   92   17
             64   38  128   44  228  128  100  238
            128  160  248  128
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 12 Ian50 2000-08-05T08:52:16 head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x2a                                  P*
    decimal
             80   42
    datetime (2000-08-05T08:52:16)
    0000   0x90 0x34 0xc8 0x25 0xc0                   .4.%.
    body (34)
    hex
    0000   0x0e 0x02 0x0e 0x01 0x01 0x6c 0x01 0x6c    .....l.l
    0008   0x00 0x30 0x00 0x09 0xc0 0x4e 0x62 0x0e    .0...Nb.
    0010   0x5b 0x00 0x1b 0xcf 0x0f 0x62 0x0e 0x18    [....b..
    0018   0x50 0x00 0x78 0x32 0x50 0x00 0x00 0x50    P.x2P..P
    0020   0x00 0x00                                  ..
    decimal
             14    2   14    1    1  108    1  108
              0   48    0    9  192   78   98   14
             91    0   27  207   15   98   14   24
             80    0  120   50   80    0    0   80
              0    0
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
`end logs/ReadHistoryData-page-10.data: 13 records`
