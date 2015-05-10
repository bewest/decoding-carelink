## START ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 220, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x10 0x78 0x5c 0x05 0x78 0x43 0x14 0x01    .x\.xC..
    0008   0x00 0x10 0x00 0x10 0x00 0x00 0x00 0x4b    .......K
    0010   0x02 0x4e 0x0b 0x0f 0x7b 0x05 0x40 0x00    .N..{.@.
    0018   0x0f 0x0b 0x0f 0x1e 0x20 0x00 0x01 0x00    .... ...
##### DEBUG DECIMAL
             16  120   92    5  120   67   20    1
              0   16    0   16    0    0    0   75
              2   78   11   15  123    5   64    0
             15   11   15   30   32    0    1    0
#### RECORD 0 Ian0B 2015-04-11T04:06:37 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-11T04:06:37)
    0000   0x65 0x06 0x24 0xab 0x0f                   e.$..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 1 BasalProfileStart 2015-04-11T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-04-11T07:00:00)
    0000   0x40 0x00 0x07 0x0b 0x0f                   @....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 2 BolusWizard 2015-04-11T08:46:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 90,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 34,
 'carb_ratio': 0,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 136}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-11T08:46:42)
    0000   0x6a 0x2e 0x08 0x6b 0x0f                   j..k.
    body (13)
    hex
    0000   0x22 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    "P.d(Z..
    0008   0x88 0x00 0x00 0x00 0x00                   .....
    decimal
             34   80    0  100   40   90    0    0
            136    0    0    0    0
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 Base (2008, 4, 14, 14, 0, 27) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0x78                                  .x
    decimal
            136  120
    datetime ((2008, 4, 14, 14, 0, 27))
    0000   0x5b 0x00 0x6e 0x2e 0x08                   [.n..
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 4 Base (2008, 1, 4, 0, 16, 34) head[2], body[0] op[0x6b]

    op hex (2)
    0000   0x6b 0x0f                                  k.
    decimal
            107   15
    datetime ((2008, 1, 4, 0, 16, 34))
    0000   0x22 0x50 0x00 0x64 0x28                   "P.d(
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 5 OldBolusWizardChange (2000, 2, 0, 0, 8, 0) head[2], body[117] op[0x5a]

    op hex (2)
    0000   0x5a 0x00                                  Z.
    decimal
             90    0
    datetime ((2000, 2, 0, 0, 8, 0))
    0000   0x00 0x88 0x00 0x00 0x00                   .....
    body (117)
    hex
    0000   0x00 0x88 0x78 0x01 0x00 0x78 0x00 0x78    ..x..x.x
    0008   0x00 0x00 0x00 0x6e 0x2e 0x48 0x6b 0x0f    ...n.Hk.
    0010   0x1e 0x01 0x72 0x0a 0x09 0x0b 0x0f 0x7b    ..r....{
    0018   0x02 0x46 0x1e 0x09 0x0b 0x0f 0x0e 0x22    .F....."
    0020   0x00 0x1f 0x20 0x46 0x1e 0x09 0x0b 0x0f    .. F....
    0028   0x7b 0x03 0x40 0x00 0x0a 0x0b 0x0f 0x14    {.@.....
    0030   0x23 0x00 0x0b 0x69 0x00 0x40 0x02 0x2b    #..i.@.+
    0038   0xab 0x0f 0x0b 0x73 0x00 0x60 0x20 0x2b    ...s.` +
    0040   0xab 0x0f 0x0b 0x66 0x4f 0x4d 0x2a 0x2b    ...fOM*+
    0048   0xab 0x0f 0x7b 0x04 0x40 0x00 0x0c 0x0b    ..{.@...
    0050   0x0f 0x18 0x1e 0x00 0x0b 0x68 0x00 0x40    .....h.@
    0058   0x02 0x2c 0xab 0x0f 0x0b 0x68 0x00 0x40    .,...h.@
    0060   0x20 0x2c 0xab 0x0f 0x0b 0x68 0x00 0x40     ,...h.@
    0068   0x02 0x2d 0xab 0x0f 0x0b 0x68 0x00 0x40    .-...h.@
    0070   0x20 0x2d 0xab 0x0f 0x0a                    -...
    decimal
              0  136  120    1    0  120    0  120
              0    0    0  110   46   72  107   15
             30    1  114   10    9   11   15  123
              2   70   30    9   11   15   14   34
              0   31   32   70   30    9   11   15
            123    3   64    0   10   11   15   20
             35    0   11  105    0   64    2   43
            171   15   11  115    0   96   32   43
            171   15   11  102   79   77   42   43
            171   15  123    4   64    0   12   11
             15   24   30    0   11  104    0   64
              2   44  171   15   11  104    0   64
             32   44  171   15   11  104    0   64
              2   45  171   15   11  104    0   64
             32   45  171   15   10
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Base (2015, 0, 15, 11, 45, 59) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0x65                                  .e
    decimal
            136  101
    datetime ((2015, 0, 15, 11, 45, 59))
    0000   0x3b 0x2d 0x6b 0x0f 0x3f                   ;-k.?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 7 Base (2008, 0, 15, 11, 13, 59) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x65                                  .e
    decimal
             17  101
    datetime ((2008, 0, 15, 11, 13, 59))
    0000   0x3b 0x0d 0x6b 0x0f 0x78                   ;.k.x
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 LowReservoir (2002, 1, 0, 0, 40, 11) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 5.4}
```
    op hex (2)
    0000   0x34 0x36                                  46
    decimal
             52   54
    datetime ((2002, 1, 0, 0, 40, 11))
    0000   0x0b 0x68 0x00 0x40 0x02                   .h.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 9 Base (2002, 1, 10, 8, 27, 15) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0xab                                  ..
    decimal
             46  171
    datetime ((2002, 1, 10, 8, 27, 15))
    0000   0x0f 0x5b 0x88 0x4a 0x02                   .[.J.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 10 Base (2000, 0, 0, 16, 0, 15) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x0b                                  ..
    decimal
             14   11
    datetime ((2000, 0, 0, 16, 0, 15))
    0000   0x0f 0x00 0x50 0x00 0x50                   ..P.P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 Base (2000, 0, 0, 0, 0, 16) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x5a                                  (Z
    decimal
             40   90
    datetime ((2000, 0, 0, 0, 0, 16))
    0000   0x10 0x00 0x00 0x00 0x00                   .....
    body (0)

`end ReadHistoryData-page-1.data: 12 records`
