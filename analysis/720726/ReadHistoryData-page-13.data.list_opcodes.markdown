## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 103, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x30 0x00 0x00 0x00 0x00 0x30 0x36 0x5c    0....06\
    0008   0x17 0x30 0x04 0x04 0x20 0x0e 0x04 0x50    .0.. ..P
    0010   0x90 0x04 0x40 0xf4 0x04 0x10 0xfe 0x04    ..@.....
    0018   0x34 0x9e 0x14 0x74 0xbc 0x14 0x01 0x00    4..t....
##### DEBUG DECIMAL
             48    0    0    0    0   48   54   92
             23   48    4    4   32   14    4   80
            144    4   64  244    4   16  254    4
             52  158   20  116  188   20    1    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 1.6, 'curve': 4},
 {'age': 114, 'amount': 0.4, 'curve': 4},
 {'age': 18, 'amount': 1.3, 'curve': 20},
 {'age': 48, 'amount': 2.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0x68 0x04 0x10 0x72 0x04    \.@h..r.
    0008   0x34 0x12 0x14 0x74 0x30 0x14              4..t0.
    decimal
             92   14   64  104    4   16  114    4
             52   18   20  116   48   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-08-25T17:28:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x2c 0x00    ..P.P.,.
    decimal
              1    0   80    0   80    0   44    0
    datetime (2012-08-25T17:28:07)
    0000   0x87 0x1c 0x51 0x79 0x0c                   ..Qy.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2012-08-25T19:43:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-25T19:43:28)
    0000   0x9c 0x2b 0x13 0x79 0x0c                   .+.y.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 2.0, 'curve': 4},
 {'age': 239, 'amount': 1.6, 'curve': 4},
 {'age': 249, 'amount': 0.4, 'curve': 4},
 {'age': 153, 'amount': 1.3, 'curve': 20},
 {'age': 183, 'amount': 2.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x8b 0x04 0x40 0xef 0x04    \.P..@..
    0008   0x10 0xf9 0x04 0x34 0x99 0x14 0x74 0xb7    ...4..t.
    0010   0x14                                       .
    decimal
             92   17   80  139    4   64  239    4
             16  249    4   52  153   20  116  183
             20
    datetime (unknown)

    body (0)

#### RECORD 4 Base (2012, 8, 25, 19, 43, 28) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2012, 8, 25, 19, 43, 28))
    0000   0x9c 0x2b 0x73 0x19 0x0c                   .+s..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Base (2000, 0, 0, 16, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2000, 0, 0, 16, 0, 1))
    0000   0x01 0x00 0x50 0x00 0x50                   ..P.P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 6 Base (2009, 2, 19, 11, 28, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2009, 2, 19, 11, 28, 0))
    0000   0x00 0x9c 0x2b 0x53 0x79                   ..+Sy
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 7 ClearAlarm 2009-02-19T16:43:00 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x5b                                  .[
    decimal
             12   91
    datetime (2009-02-19T16:43:00)
    0000   0x00 0xab 0x30 0x13 0x79                   ..0.y
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 ClearAlarm 2006-08-23T14:00:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x0e                                  ..
    decimal
             12   14
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-13.data: 9 records`
