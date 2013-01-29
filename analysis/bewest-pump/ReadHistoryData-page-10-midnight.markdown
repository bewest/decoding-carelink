### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-10.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-10.data
#### RECORD 0 BolusWizard 2012-12-17T13:14:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 184,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.5,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2012-12-17T13:14:48)
    0000   0xf0 0x0e 0x0d 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x0d 0x35 0x00    EP.-j.5.
    0008   0x00 0x01 0x00 0x41 0x7d                   ...A}
    decimal
             69   80   13   45  106   13   53    0
              0    1    0   65  125

#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 240, 'amount': 1.05, 'curve': 4},
 {'age': 250, 'amount': 2.85, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2a 0xf0 0x04 0x72 0xfa 0x04    \.*..r..
    decimal
             92    8   42  240    4  114  250    4
    datetime (unknown)

    body (0)
--
    0000   0x5c 0x05 0x04 0x72 0x15                   \..r.
    decimal
             92    5    4  114   21
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-12-17T19:24:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-12-17T19:24:22)
    0000   0xd6 0x18 0x53 0x11 0x0c                   ..S..
    body (0)

#### RECORD 7 ResultTotals 2012-12-17T13:12:17 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x26                   ....&
    decimal
              7    0    0    5   38
    datetime (2012-12-17T13:12:17)
    0000   0xd1 0x0c 0x6d 0xd1 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xd5 0x97 0x31 0x03 0x00 0x00    ....1...
    0008   0x05 0x26 0x03 0x72 0x43 0x01 0xb4 0x21    .&.rC..!
    0010   0x00 0x45 0x01 0xb4 0x21 0x00 0xd4 0x31    .E..!..1
    0018   0x00 0xe0 0x33 0x00 0x00 0x00 0x03 0x00    ..3.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  213  151   49    3    0    0
              5   38    3  114   67    1  180   33
              0   69    1  180   33    0  212   49
              0  224   51    0    0    0    3    0
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 8 PumpSuspend 2012-12-18T13:34:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-18T13:34:07)
    0000   0xc7 0x22 0x0d 0x12 0x0c                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 PumpResume 2012-12-18T14:20:57 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-18T14:20:57)
--
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-18T22:05:19)
    0000   0xd3 0x05 0x56 0x12 0x0c                   ..V..
    body (0)

#### RECORD 32 CalBGForPH 2012-12-18T22:11:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 59}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2012-12-18T22:11:12)
    0000   0xcc 0x0b 0x36 0x12 0x0c                   ..6..
    body (0)

#### RECORD 33 ResultTotals 2012-12-18T13:12:18 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x38                   ....8
    decimal
              7    0    0    5   56
    datetime (2012-12-18T13:12:18)
    0000   0xd2 0x0c 0x6d 0xd2 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x71 0x3b 0x97 0x06 0x00 0x00    ..q;....
    0008   0x05 0x38 0x03 0x64 0x41 0x01 0xd4 0x23    .8.dA..#
    0010   0x00 0x92 0x01 0xd4 0x23 0x01 0xb8 0x5e    ....#..^
    0018   0x00 0x1c 0x06 0x00 0x00 0x00 0x06 0x04    ........
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  113   59  151    6    0    0
              5   56    3  100   65    1  212   35
              0  146    1  212   35    1  184   94
              0   28    6    0    0    0    6    4
              0    2    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 34 BolusWizard 2012-12-19T00:34:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
--
    0000   0x5c 0x05 0x60 0x1b 0x14                   \.`..
    decimal
             92    5   96   27   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-12-19T23:57:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-12-19T23:57:19)
    0000   0xd3 0x39 0x57 0x13 0x0c                   .9W..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 ResultTotals 2012-12-19T13:12:19 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x86                   .....
    decimal
              7    0    0    5  134
    datetime (2012-12-19T13:12:19)
    0000   0xd3 0x0c 0x6d 0xd3 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa2 0x6a 0x0c 0x06 0x00 0x00    ...j....
    0008   0x05 0x86 0x03 0x72 0x3e 0x02 0x14 0x26    ...r>..&
    0010   0x00 0x61 0x02 0x14 0x26 0x01 0x24 0x37    .a..&.$7
    0018   0x00 0xf0 0x2d 0x00 0x00 0x00 0x05 0x03    ..-.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  162  106   12    6    0    0
              5  134    3  114   62    2   20   38
              0   97    2   20   38    1   36   55
              0  240   45    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2012-12-20T04:04:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2012-12-20T04:04:49)
    0000   0xf1 0x04 0x24 0x14 0x0c                   ..$..
    body (0)

#### RECORD 60 CalBGForPH 2012-12-20T07:52:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
--
    0000   0x5c 0x05 0x98 0x72 0x04                   \..r.
    decimal
             92    5  152  114    4
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2012-12-20T19:48:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-12-20T19:48:05)
    0000   0xc5 0x30 0x53 0x14 0x0c                   .0S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 75 ResultTotals 2012-12-20T13:12:20 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x3e                   ....>
    decimal
              7    0    0    4   62
    datetime (2012-12-20T13:12:20)
    0000   0xd4 0x0c 0x6d 0xd4 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x63 0x4c 0x80 0x03 0x00 0x00    ..cL....
    0008   0x04 0x3e 0x03 0x12 0x48 0x01 0x2c 0x1c    .>..H.,.
    0010   0x00 0x67 0x01 0x2c 0x1c 0x01 0x2c 0x64    .g.,..,d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   99   76  128    3    0    0
              4   62    3   18   72    1   44   28
              0  103    1   44   28    1   44  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 76 LowReservoir 2012-12-21T04:18:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-12-21T04:18:45)
    0000   0xed 0x12 0x04 0x15 0x0c                   .....
    body (0)

#### RECORD 77 PumpSuspend 2012-12-21T12:56:50 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
--
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-12-21T14:30:58)
    0000   0xfa 0x1e 0x4e 0x15 0x0c                   ..N..
    body (0)

#### RECORD 82 Base unknown head[2], body[0] op[0xdf]

    op hex (2)
    0000   0xdf 0x9a                                  ..
    decimal
            223  154
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-10.data: 83 records`
