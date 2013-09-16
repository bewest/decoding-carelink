## START logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 232, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x16 0x7d 0x5c 0x05 0xb8 0x2f 0x04 0x01    .}\../..
    0008   0x16 0x16 0x00 0x4b 0x81 0x4e 0x03 0x0d    ...K.N..
    0010   0x5b 0x00 0x50 0x9f 0x0e 0x03 0x0d 0x20    [.P.... 
    0018   0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00 0x00    P.-j....
##### DEBUG DECIMAL
             22  125   92    5  184   47    4    1
             22   22    0   75  129   78    3   13
             91    0   80  159   14    3   13   32
             80   13   45  106    0   24    0    0
#### RECORD 0 Bolus 2013-06-02T12:44:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-06-02T12:44:22)
    0000   0x56 0xac 0x4c 0x02 0x0d                   V.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 1 CalBGForPH 2013-06-02T17:31:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2013-06-02T17:31:49)
    0000   0x71 0x9f 0x31 0x02 0x8d                   q.1..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-06-02T17:31:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 301,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2d                                  [-
    decimal
             91   45
    datetime (2013-06-02T17:31:53)
    0000   0x75 0x9f 0x11 0x02 0x0d                   u....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   39    0    0
              0    0    0   39  125
    HOUR BITS: [1, 0, 0]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 0.7, 'curve': 20},
 {'age': 41, 'amount': 3.0, 'curve': 20},
 {'age': 121, 'amount': 1.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1c 0x1f 0x14 0x78 0x29 0x14    \....x).
    0008   0x28 0x79 0x14                             (y.
    decimal
             92   11   28   31   20  120   41   20
             40  121   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-06-02T17:31:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-06-02T17:31:53)
    0000   0x75 0x9f 0x51 0x02 0x0d                   u.Q..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalBGForPH 2013-06-02T18:30:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2013-06-02T18:30:45)
    0000   0x6d 0x9e 0x32 0x02 0x0d                   m.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 CalBGForPH 2013-06-02T20:24:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-06-02T20:24:35)
    0000   0x63 0x98 0x34 0x02 0x0d                   c.4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 BolusWizard 2013-06-02T20:25:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 144,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x90                                  [.
    decimal
             91  144
    datetime (2013-06-02T20:25:10)
    0000   0x4a 0x99 0x14 0x02 0x0d                   J....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x04 0x35 0x00    EP.-j.5.
    0008   0x00 0x08 0x00 0x35 0x7d                   ...5}
    decimal
             69   80   13   45  106    4   53    0
              0    8    0   53  125
    HOUR BITS: [1, 0, 0]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 0.85, 'curve': 4},
 {'age': 181, 'amount': 3.15, 'curve': 4},
 {'age': 205, 'amount': 0.7, 'curve': 20},
 {'age': 215, 'amount': 3.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x22 0xab 0x04 0x7e 0xb5 0x04    \."..~..
    0008   0x1c 0xcd 0x14 0x78 0xd7 0x14              ...x..
    decimal
             92   14   34  171    4  126  181    4
             28  205   20  120  215   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-06-02T20:25:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-06-02T20:25:11)
    0000   0x4b 0x99 0x54 0x02 0x0d                   K.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 ResultTotals 2013-04-02T13:13:34 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x70                   ....p
    decimal
              7    0    0    6  112
    datetime (2013-04-02T13:13:34)
    0000   0x62 0x0d 0x6d 0x62 0x0d                   b.mb.
    body (51)
    hex
    0000   0x05 0x10 0xdf 0x7b 0x69 0x06 0x00 0x00    ...{i...
    0008   0x06 0x70 0x03 0x78 0x36 0x02 0xf8 0x2e    .p.x6...
    0010   0x00 0x76 0x02 0xf8 0x2e 0x01 0x68 0x2f    .v....h/
    0018   0x01 0x90 0x35 0x00 0x00 0x00 0x06 0x03    ..5.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x42 0x8e 0x0b 0x03 0x0d    ...B....
    0030   0x1f 0x00 0x74                             ..t
    decimal
              5   16  223  123  105    6    0    0
              6  112    3  120   54    2  248   46
              0  118    2  248   46    1  104   47
              1  144   53    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0   30    0   66  142   11    3   13
             31    0  116
    DAY BITS: [0, 1, 1]
#### RECORD 11 Base (2010, 0, 14, 10, 13, 3) head[2], body[0] op[0x8b]

    op hex (2)
    0000   0x8b 0x0c                                  ..
    decimal
            139   12
    datetime ((2010, 0, 14, 10, 13, 3))
    0000   0x03 0x0d 0x0a 0x8e 0x4a                   ....J
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 12 Base (2006, 0, 14, 27, 13, 3) head[2], body[0] op[0x92]

    op hex (2)
    0000   0x92 0x2d                                  .-
    decimal
            146   45
    datetime ((2006, 0, 14, 27, 13, 3))
    0000   0x03 0x0d 0x5b 0x8e 0x76                   ..[.v
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 13 Base (2013, 0, 16, 24, 13, 3) head[2], body[0] op[0x92]

    op hex (2)
    0000   0x92 0x0d                                  ..
    decimal
            146   13
    datetime ((2013, 0, 16, 24, 13, 3))
    0000   0x03 0x0d 0x38 0x50 0x0d                   ..8P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 14 Base (2000, 0, 0, 0, 43, 3) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 43, 3))
    0000   0x03 0x2b 0x00 0x00 0x00                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 Base (2000, 4, 14, 14, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2e                                  ..
    decimal
              0   46
    datetime ((2000, 4, 14, 14, 1, 61))
    0000   0x7d 0x01 0x2e 0x2e 0x00                   }....
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 16 Base (2000, 4, 27, 13, 3, 13) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x92                                  v.
    decimal
            118  146
    datetime ((2000, 4, 27, 13, 3, 13))
    0000   0x4d 0x03 0x0d 0x5b 0x00                   M..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 17 Base (2000, 0, 29, 13, 3, 14) head[2], body[0] op[0x4b]

    op hex (2)
    0000   0x4b 0x81                                  K.
    decimal
             75  129
    datetime ((2000, 0, 29, 13, 3, 14))
    0000   0x0e 0x03 0x0d 0x1d 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 18 Base (2000, 4, 0, 22, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 22, 0, 42))
    0000   0x6a 0x00 0x16 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-14.data: 19 records`
