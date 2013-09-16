## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 146, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x06 0x4d 0x03 0x89 0x38 0x02 0xc4 0x2c    .M..8..,
    0008   0x00 0x9d 0x02 0x30 0x00 0x94 0x00 0x00    ...0....
    0010   0x00 0x00 0x07 0x02 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              6   77    3  137   56    2  196   44
              0  157    2   48    0  148    0    0
              0    0    7    2    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 BolusWizard 2013-08-02T19:48:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-02T19:48:46)
    0000   0xae 0x30 0x13 0x62 0x0d                   .0.b.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.0, 'curve': 4},
 {'age': 83, 'amount': 2.7, 'curve': 4},
 {'age': 87, 'amount': 1.2, 'curve': 20},
 {'age': 187, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x35 0x04 0x6c 0x53 0x04    \.(5.lS.
    0008   0x30 0x57 0x14 0x6c 0xbb 0x14              0W.l..
    decimal
             92   14   40   53    4  108   83    4
             48   87   20  108  187   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-08-02T19:48:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x70 0x00    ..T.T.p.
    decimal
              1    0   84    0   84    0  112    0
    datetime (2013-08-02T19:48:46)
    0000   0xae 0x30 0x53 0x62 0x0d                   .0Sb.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-08-02T21:25:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-08-02T21:25:28)
    0000   0x9c 0x19 0x35 0x62 0x0d                   ..5b.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 4 Base (2013, 8, 2, 21, 25, 28) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime ((2013, 8, 2, 21, 25, 28))
    0000   0x9c 0x19 0xd5 0x62 0x0d                   ...b.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 Ian69 2009-09-05T00:27:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2009-09-05T00:27:22)
    0000   0x96 0x5b 0x00 0xa5 0x29                   .[..)
    body (8)
    hex
    0000   0x15 0x62 0x0d 0x1f 0x90 0x00 0x6e 0x17    .b....n.
    decimal
             21   98   13   31  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 6 Base (2000, 1, 0, 0, 48, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x00                                  6.
    decimal
             54    0
    datetime ((2000, 1, 0, 0, 48, 0))
    0000   0x00 0x70 0x00 0x00 0x00                   .p...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 Base (2004, 1, 20, 14, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x70                                  .p
    decimal
              0  112
    datetime ((2004, 1, 20, 14, 28, 54))
    0000   0x36 0x5c 0x0e 0x54 0x74                   6\.Tt
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 Base (2004, 8, 4, 12, 4, 38) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x28                                  .(
    decimal
              4   40
    datetime ((2004, 8, 4, 12, 4, 38))
    0000   0xa6 0x04 0x6c 0xc4 0x04                   ..l..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 9 Base (2000, 0, 16, 0, 1, 20) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0xc8                                  0.
    decimal
             48  200
    datetime ((2000, 0, 16, 0, 1, 20))
    0000   0x14 0x01 0x00 0x70 0x00                   ...p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 10 Base (2005, 4, 9, 5, 0, 0) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x00                                  p.
    decimal
            112    0
    datetime ((2005, 4, 9, 5, 0, 0))
    0000   0x40 0x00 0xa5 0x29 0x55                   @..)U
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 Base (2000, 4, 0, 0, 0, 59) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x0d                                  b.
    decimal
             98   13
    datetime ((2000, 4, 0, 0, 0, 59))
    0000   0x7b 0x00 0x80 0x00 0x00                   {....
    body (0)

#### RECORD 12 Prime (2013, 0, 6, 0, 0, 7) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x0d 0x00 0x20 0x00                   ... .
    decimal
              3   13    0   32    0
    datetime ((2013, 0, 6, 0, 0, 7))
    0000   0x07 0x00 0x00 0x06 0x4d                   ....M
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 13 Base (2002, 0, 14, 0, 0, 0) head[2], body[0] op[0x82]

    op hex (2)
    0000   0x82 0x0d                                  ..
    decimal
            130   13
    datetime ((2002, 0, 14, 0, 0, 0))
    0000   0x00 0x00 0x00 0x6e 0x82                   ...n.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 Base (2003, 1, 7, 6, 48, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x06                                  ..
    decimal
             13    6
    datetime ((2003, 1, 7, 6, 48, 0))
    0000   0x00 0x70 0x46 0xa7 0x03                   .pF..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-29.data: 15 records`
