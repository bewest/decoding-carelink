### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-3.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-3.data
#### RECORD 0 BolusWizard 2013-01-11T17:19:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 286,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1e                                  [.
    decimal
             91   30
    datetime (2013-01-11T17:19:20)
    0000   0x14 0x53 0x11 0x0b 0x0d                   .S...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x0e 0x00 0x15 0x7d                   ....}
    decimal
              0   81   13   45  106   35    0    0
              0   14    0   21  125
    HOUR BITS: [0, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 2.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0x69 0x04                   \.di.
--
    decimal
             92   11   96  106    4  104  166    4
            100   10   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-01-11T20:00:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.7, 'dual_component': '??', 'programmed': 6.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x43 0x43 0x04                        .CC.
    decimal
              1   67   67    4
    datetime (2013-01-11T20:00:33)
    0000   0x21 0x40 0x74 0x0b 0x0d                   !@t..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 ResultTotals 2013-02-11T13:13:11 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa6                   .....
    decimal
              7    0    0    5  166
    datetime (2013-02-11T13:13:11)
    0000   0x0b 0x8d 0x6d 0x0b 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xde 0x88 0x53 0x07 0x00 0x00    ....S...
    0008   0x05 0xa6 0x03 0x6e 0x3d 0x02 0x38 0x27    ...n=.8'
    0010   0x00 0x72 0x02 0x38 0x27 0x01 0x5c 0x3d    .r.8'.\=
    0018   0x00 0xdc 0x27 0x00 0x00 0x00 0x04 0x01    ..'.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  222  136   83    7    0    0
              5  166    3  110   61    2   56   39
              0  114    2   56   39    1   92   61
              0  220   39    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 CalBGForPH 2013-01-12T02:12:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 379}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-01-12T02:12:46)
    0000   0x2e 0x4c 0x22 0x0c 0x8d                   .L"..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2013-01-12T02:13:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 56,
--
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-01-12T16:57:17)
    0000   0x11 0x79 0x50 0x0c 0x0d                   .yP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 35 LowReservoir 2013-01-12T21:28:25 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-01-12T21:28:25)
    0000   0x19 0x5c 0x15 0x0c 0x0d                   .\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 ResultTotals 2013-02-12T13:13:12 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x80                   .....
    decimal
              7    0    0    6  128
    datetime (2013-02-12T13:13:12)
    0000   0x0c 0x8d 0x6d 0x0c 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xdb 0x72 0x7b 0x05 0x00 0x00    ...r{...
    0008   0x06 0x80 0x03 0x84 0x36 0x02 0xfc 0x2e    ....6...
    0010   0x00 0x65 0x02 0xfc 0x2e 0x01 0x30 0x28    .e....0(
    0018   0x01 0xcc 0x3c 0x00 0x00 0x00 0x05 0x02    ..<.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  219  114  123    5    0    0
              6  128    3  132   54    2  252   46
              0  101    2  252   46    1   48   40
              1  204   60    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 CalBGForPH 2013-01-13T00:27:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-01-13T00:27:30)
    0000   0x1e 0x5b 0x20 0x0d 0x0d                   .[ ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 BolusWizard 2013-01-13T00:27:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
--
    0000   0x5c 0x08 0x54 0x0f 0x04 0x80 0x23 0x04    \.T...#.
    decimal
             92    8   84   15    4  128   35    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-01-13T22:09:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-01-13T22:09:33)
    0000   0x21 0x49 0x56 0x0d 0x0d                   !IV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 68 ResultTotals 2013-02-13T13:13:13 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x40                   ....@
    decimal
              7    0    0    6   64
    datetime (2013-02-13T13:13:13)
    0000   0x0d 0x8d 0x6d 0x0d 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x9c 0x4c 0x4b 0x05 0x00 0x00    ...LK...
    0008   0x06 0x40 0x03 0x48 0x34 0x02 0xf8 0x30    .@.H4..0
    0010   0x00 0xc9 0x02 0xf8 0x30 0x02 0x44 0x4c    ....0.DL
    0018   0x00 0xb4 0x18 0x00 0x00 0x00 0x07 0x06    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  156   76   75    5    0    0
              6   64    3   72   52    2  248   48
              0  201    2  248   48    2   68   76
              0  180   24    0    0    0    7    6
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 CalBGForPH 2013-01-14T02:19:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 428}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-01-14T02:19:22)
    0000   0x16 0x53 0x22 0x0e 0x8d                   .S"..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 BolusWizard 2013-01-14T02:19:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 67,
--
{'amount': 372}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-01-14T05:44:25)
    0000   0x19 0x6c 0x25 0x0e 0x8d                   .l%..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 83 Base unknown head[2], body[0] op[0xf6]

    op hex (2)
    0000   0xf6 0xb1                                  ..
    decimal
            246  177
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-3.data: 84 records`
