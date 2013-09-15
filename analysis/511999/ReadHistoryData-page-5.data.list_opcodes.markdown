## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 153, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2c 0x78 0x5c 0x0b 0x34 0xc5 0xc0 0x34    ,x\.4..4
    0008   0x5b 0xd0 0x38 0x8d 0xd0 0x01 0x00 0x2c    [.8....,
    0010   0x00 0x2c 0x00 0x00 0x00 0xa1 0x28 0x51    .,....(Q
    0018   0x18 0x0d 0x0a 0x6d 0xb3 0x23 0x32 0x18    ...m.#2.
##### DEBUG DECIMAL
             44  120   92   11   52  197  192   52
             91  208   56  141  208    1    0   44
              0   44    0    0    0  161   40   81
             24   13   10  109  179   35   50   24
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 4.45, 'curve': 208},
 {'age': 147, 'amount': 0.75, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0xb2 0x89 0xd0 0x1e 0x93 0xd0    \.......
    decimal
             92    8  178  137  208   30  147  208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2012, 0, 0, 0, 0, 56) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x38 0x00                        ..8.
    decimal
              1    0   56    0
    datetime ((2012, 0, 0, 0, 0, 56))
    0000   0x38 0x00 0x00 0x00 0xac                   8....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 NoDelivery (2011, 1, 23, 27, 45, 10) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x4b 0x18 0x0d                        .K..
    decimal
              6   75   24   13
    datetime ((2011, 1, 23, 27, 45, 10))
    0000   0x0a 0x6d 0x9b 0x37 0x2b                   .m.7+
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 3 NewTimeSet 2011-05-23T03:45:27 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime (2011-05-23T03:45:27)
    0000   0x5b 0x6d 0xa3 0x37 0x0b                   [m.7.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 4 NewTimeSet 2012-01-24T00:16:16 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime (2012-01-24T00:16:16)
    0000   0x10 0x50 0x00 0x78 0x3c                   .P.x<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 5 ChangeTimeDisplay (2012, 0, 0, 0, 52, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime ((2012, 0, 0, 0, 52, 0))
    0000   0x00 0x34 0x00 0x00 0x2c                   .4..,
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 6 Base (2004, 5, 24, 11, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2004, 5, 24, 11, 28, 56))
    0000   0x78 0x5c 0x0b 0x38 0x34                   x\.84
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 7 Base (2000, 11, 4, 30, 16, 58) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0xb2                                  ..
    decimal
            192  178
    datetime ((2000, 11, 4, 30, 16, 58))
    0000   0xba 0xd0 0x1e 0xc4 0xd0                   .....
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 8 Bolus (2003, 0, 0, 12, 0, 52) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x34 0x00                        ..4.
    decimal
              1    0   52    0
    datetime ((2003, 0, 0, 12, 0, 52))
    0000   0x34 0x00 0x2c 0x00 0xa3                   4.,..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 9 Base (2000, 0, 3, 27, 13, 24) head[2], body[0] op[0x37]

    op hex (2)
    0000   0x37 0x4b                                  7K
    decimal
             55   75
    datetime ((2000, 0, 3, 27, 13, 24))
    0000   0x18 0x0d 0x7b 0x03 0x80                   ..{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 Base (2000, 0, 29, 24, 13, 24) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2000, 0, 29, 24, 13, 24))
    0000   0x18 0x0d 0x18 0x1d 0x00                   .....
    body (0)

#### RECORD 11 CalBGForPH 2013-08-24T14:31:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-08-24T14:31:49)
    0000   0xb1 0x1f 0x2e 0x18 0x0d                   .....
    body (0)

#### RECORD 12 BolusWizard 2013-08-24T14:31:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-08-24T14:31:59)
    0000   0xbb 0x1f 0x0e 0x18 0x0d                   .....
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x08 0x00 0x34 0x78         4....4x
    decimal
             16   80    0  120   60  100    0    0
             52    0    0    8    0   52  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 1.3, 'curve': 192},
 {'age': 208, 'amount': 1.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x9e 0xc0 0x38 0xd0 0xc0    \.4..8..
    decimal
             92    8   52  158  192   56  208  192
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus (2011, 0, 0, 8, 0, 52) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x34 0x00                        ..4.
    decimal
              1    0   52    0
    datetime ((2011, 0, 0, 8, 0, 52))
    0000   0x34 0x00 0x08 0x00 0xbb                   4....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 15 PumpResume (2001, 0, 0, 27, 13, 24) head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x4e                                  .N
    decimal
             31   78
    datetime ((2001, 0, 0, 27, 13, 24))
    0000   0x18 0x0d 0x5b 0x00 0xa1                   ..[..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 16 Base (2000, 0, 16, 11, 13, 24) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x11                                  (.
    decimal
             40   17
    datetime ((2000, 0, 16, 11, 13, 24))
    0000   0x18 0x0d 0x0b 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 17 ChangeTimeDisplay 2000-04-12T00:00:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-12T00:00:36)
    0000   0x64 0x00 0x00 0x2c 0x00                   d..,.
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-5.data: 18 records`
