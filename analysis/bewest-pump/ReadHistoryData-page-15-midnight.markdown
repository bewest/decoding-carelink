### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-15.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc5 0x76                                  .v
##### DEBUG DECIMAL
            197  118
#### RECORD 0 BolusWizard 2012-11-28T15:02:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 1.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2012-11-28T15:02:26)
    0000   0x9a 0xc2 0x0f 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfc 0x0b 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             15   80   13   45  106  252   11  240
              0    0    0    7  125
--
    0000   0x5c 0x05 0x0c 0x8d 0x04                   \....
    decimal
             92    5   12  141    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-11-28T23:45:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-11-28T23:45:35)
    0000   0xa3 0xed 0x57 0x1c 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 ResultTotals (2012, 10, 28, 13, 12, 60) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime ((2012, 10, 28, 13, 12, 60))
    0000   0xbc 0x8c 0x6d 0xbc 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x74 0x49 0xba 0x03 0x00 0x00    ..tI....
    0008   0x04 0xe4 0x03 0x78 0x47 0x01 0x6c 0x1d    ...xG.l.
    0010   0x00 0x84 0x01 0x6c 0x1d 0x01 0x60 0x61    ...l..`a
    0018   0x00 0x0c 0x03 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  116   73  186    3    0    0
              4  228    3  120   71    1  108   29
              0  132    1  108   29    1   96   97
              0   12    3    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 LowReservoir 2012-11-29T10:49:05 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-29T10:49:05)
    0000   0x85 0xf1 0x0a 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 15 PumpSuspend 2012-11-29T10:53:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
--
    0000   0x5c 0x05 0x30 0x14 0x04                   \.0..
    decimal
             92    5   48   20    4
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2012-11-29T20:44:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-11-29T20:44:04)
    0000   0x84 0xec 0x54 0x1d 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 ResultTotals (2012, 10, 29, 13, 12, 61) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd8                   .....
    decimal
              7    0    0    4  216
    datetime ((2012, 10, 29, 13, 12, 61))
    0000   0xbd 0x8c 0x6d 0xbd 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xd4 0xc6 0xe2 0x02 0x00 0x00    ........
    0008   0x04 0xd8 0x03 0x78 0x48 0x01 0x60 0x1c    ...xH.`.
    0010   0x00 0x48 0x01 0x60 0x1c 0x00 0xd8 0x3d    .H.`...=
    0018   0x00 0x88 0x27 0x00 0x00 0x00 0x04 0x02    ..'.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  212  198  226    2    0    0
              4  216    3  120   72    1   96   28
              0   72    1   96   28    0  216   61
              0  136   39    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 32 Rewind 2012-11-30T08:36:02 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-30T08:36:02)
    0000   0x82 0xe4 0x08 0x1e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Prime 2012-11-30T08:36:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
--
    0000   0x5c 0x08 0x34 0xaf 0x04 0x7c 0xcd 0x04    \.4..|..
    decimal
             92    8   52  175    4  124  205    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-11-30T18:59:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2012-11-30T18:59:32)
    0000   0xa0 0xfb 0x52 0x1e 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 ResultTotals (2012, 10, 30, 13, 12, 62) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xac                   .....
    decimal
              7    0    0    4  172
    datetime ((2012, 10, 30, 13, 12, 62))
    0000   0xbe 0x8c 0x6d 0xbe 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x76 0x5f 0x8d 0x03 0x00 0x00    ..v_....
    0008   0x04 0xac 0x03 0x58 0x48 0x01 0x54 0x1c    ...XH.T.
    0010   0x00 0x74 0x01 0x54 0x1c 0x01 0x54 0x64    .t.T..Td
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  118   95  141    3    0    0
              4  172    3   88   72    1   84   28
              0  116    1   84   28    1   84  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 CalBGForPH 2012-12-01T21:31:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2012-12-01T21:31:52)
    0000   0xf4 0x1f 0x35 0x01 0x0c                   ..5..
    body (0)

#### RECORD 50 BolusWizard 2012-12-01T21:32:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
--
    0000   0x5c 0x05 0x1a 0x09 0x04                   \....
    decimal
             92    5   26    9    4
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-12-01T21:33:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2012-12-01T21:33:58)
    0000   0xfa 0x21 0x95 0x01 0x0c                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 ResultTotals 2012-12-01T13:12:01 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd8                   .....
    decimal
              7    0    0    4  216
    datetime (2012-12-01T13:12:01)
    0000   0xc1 0x0c 0x6d 0xc1 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x72 0x72 0x72 0x02 0x00 0x00    ..rrr...
    0008   0x04 0xd8 0x03 0x84 0x49 0x01 0x54 0x1b    ....I.T.
    0010   0x00 0xab 0x01 0x54 0x1b 0x01 0x46 0x60    ...T..F`
    0018   0x00 0x0e 0x04 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  114  114  114    2    0    0
              4  216    3  132   73    1   84   27
              0  171    1   84   27    1   70   96
              0   14    4    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 59 Bolus 2012-12-01T21:36:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x05                        .%%.
    decimal
              1   37   37    5
    datetime (2012-12-01T21:36:51)
    0000   0xf3 0x24 0xb5 0x01 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 CalBGForPH 2012-12-02T02:04:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
--
              0   80   13   45  106   10    0    0
              0    3    0    7  125
    HOUR BITS: [0, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 216, 'amount': 2.0, 'curve': 4},
 {'age': 226, 'amount': 0.8, 'curve': 4},
 {'age': 120, 'amount': 6.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0xd8 0x04 0x20 0xe2 0x04    \.P.. ..
    0008   0xf0 0x78 0x14                             .x.
    decimal
             92   11   80  216    4   32  226    4
            240  120   20
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-15.data: 78 records`
