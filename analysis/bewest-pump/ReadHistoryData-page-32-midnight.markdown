### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-32.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-32.data
#### RECORD 0 CalBGForPH 2012-09-24T20:34:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2012-09-24T20:34:48)
    0000   0xb0 0x62 0x34 0x18 0x0c                   .b4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2012-09-24T20:35:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2012-09-24T20:35:31)
    0000   0x9f 0x63 0x14 0x18 0x0c                   .c...
    body (13)
    hex
--
    0000   0x5c 0x08 0x28 0xd3 0x04 0xf0 0xaf 0x14    \.(.....
    decimal
             92    8   40  211    4  240  175   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2012-09-24T20:35:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2012-09-24T20:35:32)
    0000   0xa0 0x63 0x54 0x18 0x0c                   .cT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 ResultTotals 2012-10-24T13:12:24 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x60                   ....`
    decimal
              7    0    0    5   96
    datetime (2012-10-24T13:12:24)
    0000   0x98 0x8c 0x6d 0x98 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8d 0x46 0xae 0x04 0x00 0x00    ...F....
    0008   0x05 0x60 0x03 0x78 0x41 0x01 0xe8 0x23    .`.xA..#
    0010   0x00 0x86 0x01 0xe8 0x23 0x01 0x9c 0x54    ....#..T
    0018   0x00 0x4c 0x10 0x00 0x00 0x00 0x03 0x01    .L......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  141   70  174    4    0    0
              5   96    3  120   65    1  232   35
              0  134    1  232   35    1  156   84
              0   76   16    0    0    0    3    1
              0    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 PumpSuspend 2012-09-25T09:55:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-25T09:55:38)
    0000   0xa6 0x77 0x09 0x19 0x0c                   .w...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 PumpResume 2012-09-25T10:59:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-25T10:59:13)
--
    decimal
             92   11   44   50    4   38  100    4
             62  110    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2012-09-25T23:44:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-09-25T23:44:47)
    0000   0xaf 0x6c 0x57 0x19 0x0c                   .lW..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 35 ResultTotals 2012-10-25T13:12:25 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x7e                   ....~
    decimal
              7    0    0    5  126
    datetime (2012-10-25T13:12:25)
    0000   0x99 0x8c 0x6d 0x99 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xca 0x8d 0x21 0x06 0x00 0x00    ....!...
    0008   0x05 0x7e 0x03 0x56 0x3d 0x02 0x28 0x27    .~.V=.('
    0010   0x00 0x75 0x02 0x28 0x27 0x01 0x5c 0x3f    .u.('.\?
    0018   0x00 0xcc 0x25 0x00 0x00 0x00 0x08 0x05    ..%.....
    0020   0x01 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  202  141   33    6    0    0
              5  126    3   86   61    2   40   39
              0  117    2   40   39    1   92   63
              0  204   37    0    0    0    8    5
              1    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 36 CalBGForPH 2012-09-26T01:21:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2012-09-26T01:21:23)
    0000   0x97 0x55 0x21 0x1a 0x0c                   .U!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 LowReservoir 2012-09-26T03:26:15 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
--
    decimal
             92   11   96   74   20   52  124   20
            116  144   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2012-09-26T17:54:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-09-26T17:54:54)
    0000   0xb6 0x76 0x51 0x1a 0x0c                   .vQ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 60 ResultTotals 2012-10-26T13:12:26 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-10-26T13:12:26)
    0000   0x9a 0x8c 0x6d 0x9a 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xbd 0x5b 0x20 0x06 0x00 0x00    ...[ ...
    0008   0x05 0x0c 0x03 0x74 0x44 0x01 0x98 0x20    ...tD.. 
    0010   0x00 0x5d 0x01 0x98 0x20 0x01 0x08 0x41    .].. ..A
    0018   0x00 0x90 0x23 0x00 0x00 0x00 0x04 0x03    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  189   91   32    6    0    0
              5   12    3  116   68    1  152   32
              0   93    1  152   32    1    8   65
              0  144   35    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 PumpSuspend 2012-09-27T14:09:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-27T14:09:20)
    0000   0x94 0x49 0x0e 0x1b 0x0c                   .I...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 PumpResume 2012-09-27T14:33:34 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-27T14:33:34)
--
    decimal
             92   14  160   16    4   60   56    4
             78  236    4   46  246    4
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2012-09-27T19:10:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-09-27T19:10:18)
    0000   0x92 0x4a 0x53 0x1b 0x0c                   .JS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 ResultTotals (2000, 10, 0, 0, 12, 27) head[5], body[14] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x10                   .....
    decimal
              7    0    0    5   16
    datetime ((2000, 10, 0, 0, 12, 27))
    0000   0x9b 0x8c 0x00 0x00 0x00                   .....
    body (14)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x85 0xc9              ......
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0  133  201
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-32.data: 81 records`
