## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 184, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x98 0x00 0x00 0x00 0x00 0x98 0x36 0x01    ......6.
    0008   0x00 0x98 0x00 0x98 0x00 0x00 0x00 0x47    .......G
    0010   0xf2 0x4a 0x7c 0x0d 0x5b 0x00 0x68 0xdf    .J|.[.h.
    0018   0x0b 0x7c 0x0d 0x0b 0x90 0x00 0x6e 0x17    .|....n.
##### DEBUG DECIMAL
            152    0    0    0    0  152   54    1
              0  152    0  152    0    0    0   71
            242   74  124   13   91    0  104  223
             11  124   13   11  144    0  110   23
#### RECORD 0 BolusWizard 2013-07-27T22:33:03 head[2], body[15] op[0x5b]
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
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0xcc 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  204    0    0   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.0, 'curve': 4},
 {'age': 58, 'amount': 0.7, 'curve': 4},
 {'age': 68, 'amount': 3.5, 'curve': 4},
 {'age': 102, 'amount': 1.8, 'curve': 20},
 {'age': 112, 'amount': 1.85, 'curve': 20},
 {'age': 122, 'amount': 1.55, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x50 0x30 0x04 0x1c 0x3a 0x04    \.P0..:.
    0008   0x8c 0x44 0x04 0x48 0x66 0x14 0x4a 0x70    .D.Hf.Jp
    0010   0x14 0x3e 0x7a 0x14                        .>z.
    decimal
             92   20   80   48    4   28   58    4
            140   68    4   72  102   20   74  112
             20   62  122   20
    datetime (unknown)

    body (0)

#### RECORD 2 BasalProfileStart 2013-07-28T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-28T00:00:00)
    0000   0x40 0xc0 0x00 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 ResultTotals (2000, 6, 0, 0, 13, 59) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xa0                   .....
    decimal
              7    0    0    6  160
    datetime ((2000, 6, 0, 0, 13, 59))
    0000   0x7b 0x8d 0x00 0x00 0x00                   {....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7b 0x8d 0x06 0x00 0xa3 0x6b 0xf8    n{....k.
    0008   0x04 0x00 0x00 0x06 0xa0 0x03 0x52 0x32    ......R2
    0010   0x03 0x4e 0x32 0x00 0xde 0x02 0x92 0x00    .N2.....
    0018   0x50 0x00 0x6c 0x00 0x00 0x08 0x01 0x01    P.l.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  123  141    6    0  163  107  248
              4    0    0    6  160    3   82   50
              3   78   50    0  222    2  146    0
             80    0  108    0    0    8    1    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 5 BasalProfileStart 2013-07-28T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-28T04:00:00)
    0000   0x40 0xc0 0x04 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 NoDelivery 2013-07-28T08:33:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2013-07-28T08:33:00)
    0000   0x40 0xe1 0x48 0xbc 0x0d                   @.H..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 7 ClearAlarm 2013-07-28T08:33:11 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2013-07-28T08:33:11)
    0000   0x4b 0xe1 0x08 0x1c 0x0d                   K....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BasalProfileStart 2013-07-28T08:33:11 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-28T08:33:11)
    0000   0x4b 0xe1 0x08 0x1c 0x0d                   K....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BasalProfileStart 2013-07-28T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-28T09:30:00)
    0000   0x40 0xde 0x09 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 10 Ian69 2013-07-28T10:30:00 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-28T10:30:00)
    0000   0x40 0xde 0x0a 0x1c 0x0d                   @....
    body (8)
    hex
    0000   0x2a 0x1e 0x5b 0x00 0x47 0xf2 0x0a 0x7c    *.[.G..|
    decimal
             42   30   91    0   71  242   10  124
    HOUR BITS: [1, 1, 0]
#### RECORD 11 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2a                                  .*
    decimal
             13   42
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-33.data: 12 records`
