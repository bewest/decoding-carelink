### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-4.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x15 0x6d                                  .m
##### DEBUG DECIMAL
             21  109
#### RECORD 0 hack1 2013-01-07T00:32:21 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x06 0x8d 0x05 0x00 0x6c 0x43 0xac    m....lC.
    0008   0x03 0x00 0x00 0x04 0x0c 0x03 0x84 0x57    .......W
    0010   0x00 0x88 0x0d 0x00 0x33 0x00 0x88 0x0d    ....3...
    0018   0x00 0x88 0x64 0x00 0x00 0x00 0x00 0x00    ..d.....
    0020   0x00 0x01 0x01 0x00 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0xd8              ......
    decimal
            109    6  141    5    0  108   67  172
              3    0    0    4   12    3  132   87
              0  136   13    0   51    0  136   13
              0  136  100    0    0    0    0    0
              0    1    1    0    0    0   12    0
            232    0    0    0   10  216
    datetime (2013-01-07T00:32:21)
    0000   0x15 0x60 0x20 0x07 0x0d                   .` ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-01-07T00:32:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 216,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
--
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-01-07T20:32:01)
    0000   0x01 0x60 0x54 0x07 0x0d                   .`T..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 22 CalBGForPH 2013-01-07T21:35:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-01-07T21:35:13)
    0000   0x0d 0x63 0x35 0x07 0x0d                   .c5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 ResultTotals 2013-02-07T13:13:07 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x26                   ....&
    decimal
              7    0    0    5   38
    datetime (2013-02-07T13:13:07)
    0000   0x07 0x8d 0x6d 0x07 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x94 0x58 0xd8 0x07 0x00 0x00    ...X....
    0008   0x05 0x26 0x03 0x72 0x43 0x01 0xb4 0x21    .&.rC..!
    0010   0x00 0x79 0x01 0xb4 0x21 0x01 0x64 0x52    .y..!.dR
    0018   0x00 0x50 0x12 0x00 0x00 0x00 0x05 0x04    .P......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  148   88  216    7    0    0
              5   38    3  114   67    1  180   33
              0  121    1  180   33    1  100   82
              0   80   18    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 24 CalBGForPH 2013-01-08T03:59:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 399}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-01-08T03:59:58)
    0000   0x3a 0x7b 0x23 0x08 0x8d                   :{#..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 BolusWizard 2013-01-08T04:00:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 399,
--
    0000   0x5c 0x08 0xa4 0x06 0x14 0x60 0x1a 0x14    \....`..
    decimal
             92    8  164    6   20   96   26   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-01-08T18:56:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-01-08T18:56:05)
    0000   0x05 0x78 0x52 0x08 0x0d                   .xR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 ResultTotals 2013-02-08T13:13:08 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x74                   ....t
    decimal
              7    0    0    5  116
    datetime (2013-02-08T13:13:08)
    0000   0x08 0x8d 0x6d 0x08 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xf6 0x8e 0x8f 0x05 0x00 0x00    ........
    0008   0x05 0x74 0x03 0x74 0x3f 0x02 0x00 0x25    .t.t?..%
    0010   0x00 0x35 0x02 0x00 0x25 0x00 0xa0 0x1f    .5..%...
    0018   0x01 0x60 0x45 0x00 0x00 0x00 0x04 0x00    .`E.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  246  142  143    5    0    0
              5  116    3  116   63    2    0   37
              0   53    2    0   37    0  160   31
              1   96   69    0    0    0    4    0
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 PumpSuspend 2013-01-09T13:57:37 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-09T13:57:37)
    0000   0x25 0x79 0x0d 0x09 0x0d                   %y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 48 PumpResume 2013-01-09T14:17:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-09T14:17:27)
--
    0000   0x5c 0x05 0x7c 0x6d 0x04                   \.|m.
    decimal
             92    5  124  109    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-01-09T17:23:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-01-09T17:23:17)
    0000   0x11 0x57 0x51 0x09 0x0d                   .WQ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 60 ResultTotals 2013-02-09T13:13:09 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x46                   ....F
    decimal
              7    0    0    4   70
    datetime (2013-02-09T13:13:09)
    0000   0x09 0x8d 0x6d 0x09 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xd3 0x62 0x29 0x03 0x00 0x00    ...b)...
    0008   0x04 0x46 0x03 0x76 0x51 0x00 0xd0 0x13    .F.vQ...
    0010   0x00 0x2c 0x00 0xd0 0x13 0x00 0x7c 0x3c    .,....|<
    0018   0x00 0x54 0x28 0x00 0x00 0x00 0x02 0x01    .T(.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  211   98   41    3    0    0
              4   70    3  118   81    0  208   19
              0   44    0  208   19    0  124   60
              0   84   40    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 PumpSuspend 2013-01-10T10:29:52 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-10T10:29:52)
    0000   0x34 0x5d 0x0a 0x0a 0x0d                   4]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 PumpResume 2013-01-10T10:46:52 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-10T10:46:52)
--
    decimal
             92   11   12   64    5   68   74    4
             44   84    4
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-01-10T12:58:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-01-10T12:58:56)
    0000   0x38 0x7a 0x4c 0x0a 0x0d                   8zL..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 74 ResultTotals 2013-02-10T13:13:10 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x2e                   .....
    decimal
              7    0    0    5   46
    datetime (2013-02-10T13:13:10)
    0000   0x0a 0x8d 0x6d 0x0a 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xc7 0x6d 0xf4 0x03 0x00 0x00    ...m....
    0008   0x05 0x2e 0x03 0x76 0x43 0x01 0xb8 0x21    ...vC..!
    0010   0x00 0x6c 0x01 0xb8 0x21 0x01 0x48 0x4b    .l..!.HK
    0018   0x00 0x70 0x19 0x00 0x00 0x00 0x03 0x02    .p......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  199  109  244    3    0    0
              5   46    3  118   67    1  184   33
              0  108    1  184   33    1   72   75
              0  112   25    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 75 PumpSuspend 2013-01-11T13:37:35 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-11T13:37:35)
    0000   0x23 0x65 0x0d 0x0b 0x0d                   #e...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 76 PumpResume 2013-01-11T14:08:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-11T14:08:18)
--
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-01-11T15:38:10)
    0000   0x0a 0x66 0x4f 0x0b 0x0d                   .fO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 80 CalBGForPH 2013-01-11T17:19:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 286}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime (2013-01-11T17:19:10)
    0000   0x0a 0x53 0x31 0x0b 0x8d                   .S1..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-4.data: 81 records`
