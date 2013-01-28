### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-35.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 1009, found 13 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x73 0xd3                                  s.
##### DEBUG DECIMAL
            115  211
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 127, 'amount': 0.3, 'curve': 4},
 {'age': 157, 'amount': 0.6, 'curve': 4},
 {'age': 227, 'amount': 4.5, 'curve': 4},
 {'age': 21, 'amount': 0.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0c 0x7f 0x04 0x18 0x9d 0x04    \.......
    0008   0xb4 0xe3 0x04 0x14 0x15 0x14              ......
    decimal
             92   14   12  127    4   24  157    4
            180  227    4   20   21   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-09-13T18:51:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-09-13T18:51:05)
    0000   0x85 0x73 0x52 0x0d 0x0c                   .sR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 ResultTotals 2012-10-13T13:12:13 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x96                   .....
    decimal
              7    0    0    4  150
    datetime (2012-10-13T13:12:13)
    0000   0x8d 0x8c 0x6d 0x8d 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x80 0x68 0x97 0x02 0x00 0x00    ...h....
    0008   0x04 0x96 0x03 0x42 0x47 0x01 0x54 0x1d    ...BG.T.
    0010   0x00 0x6d 0x01 0x54 0x1d 0x01 0x40 0x5e    .m.T..@^
    0018   0x00 0x14 0x06 0x00 0x00 0x00 0x05 0x04    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  128  104  151    2    0    0
              4  150    3   66   71    1   84   29
              0  109    1   84   29    1   64   94
              0   20    6    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 PumpSuspend 2012-09-14T11:21:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-14T11:21:30)
    0000   0x9e 0x55 0x0b 0x0e 0x0c                   .U...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 PumpResume 2012-09-14T11:41:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-14T11:41:33)
--
    decimal
             92   11   16   51    4   20  205   20
            124  215   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2012-09-14T22:15:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-09-14T22:15:38)
    0000   0xa6 0x4f 0x56 0x0e 0x0c                   .OV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 ResultTotals 2012-10-14T13:12:14 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe0                   .....
    decimal
              7    0    0    4  224
    datetime (2012-10-14T13:12:14)
    0000   0x8e 0x8c 0x6d 0x8e 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x74 0x66 0x8e 0x07 0x00 0x00    ..tf....
    0008   0x04 0xe0 0x03 0x74 0x47 0x01 0x6c 0x1d    ...tG.l.
    0010   0x00 0x7b 0x01 0x6c 0x1d 0x01 0x6c 0x64    .{.l..ld
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  116  102  142    7    0    0
              4  224    3  116   71    1  108   29
              0  123    1  108   29    1  108  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 28 Battery 2012-09-15T10:08:35 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2012-09-15T10:08:35)
    0000   0xa3 0x48 0x0a 0x0f 0x0c                   .H...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 Battery 2012-09-15T10:08:58 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2012-09-15T10:08:58)
--
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-09-15T19:13:59)
    0000   0xbb 0x4d 0x53 0x0f 0x0c                   .MS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 41 CalForBG 2012-09-15T20:44:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 66}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2012-09-15T20:44:41)
    0000   0xa9 0x6c 0x34 0x0f 0x0c                   .l4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 42 ResultTotals 2012-10-15T13:12:15 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x66                   ....f
    decimal
              7    0    0    4  102
    datetime (2012-10-15T13:12:15)
    0000   0x8f 0x8c 0x6d 0x8f 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x80 0x42 0xf2 0x05 0x00 0x00    ...B....
    0008   0x04 0x66 0x03 0x56 0x4c 0x01 0x10 0x18    .f.VL...
    0010   0x00 0x5b 0x01 0x10 0x18 0x01 0x10 0x64    .[.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  128   66  242    5    0    0
              4  102    3   86   76    1   16   24
              0   91    1   16   24    1   16  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 PumpSuspend 2012-09-16T08:12:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-16T08:12:59)
    0000   0xbb 0x4c 0x08 0x10 0x0c                   .L...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 44 PumpResume 2012-09-16T08:32:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-16T08:32:58)
--
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x01 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x33 0x7d                   ...3}
    decimal
             65   80   13   45  106    1   50    0
              0    0    0   51  125
    HOUR BITS: [0, 1, 0]
#### RECORD 60 Bolus 2012-09-16T22:16:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'programmed': 5.1}
```
    op hex (4)
    0000   0x01 0x33 0x33 0x00                        .33.
    decimal
              1   51   51    0
    datetime (2012-09-16T22:16:58)
    0000   0xba 0x50 0x56 0x10 0x0c                   .PV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 61 ResultTotals 2012-10-16T13:12:16 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x20                   .... 
    decimal
              7    0    0    5   32
    datetime (2012-10-16T13:12:16)
    0000   0x90 0x8c 0x6d 0x90 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x89 0x6c 0xaa 0x03 0x00 0x00    ...l....
    0008   0x05 0x20 0x03 0x78 0x44 0x01 0xa8 0x20    . .xD.. 
    0010   0x00 0x7e 0x01 0xa8 0x20 0x01 0x80 0x5b    .~.. ..[
    0018   0x00 0x28 0x09 0x00 0x00 0x00 0x05 0x03    .(......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  137  108  170    3    0    0
              5   32    3  120   68    1  168   32
              0  126    1  168   32    1  128   91
              0   40    9    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 CalForBG 2012-09-17T00:03:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2012-09-17T00:03:52)
    0000   0xb4 0x43 0x20 0x11 0x0c                   .C ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 63 BolusWizard 2012-09-17T00:04:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 143,
--
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-09-17T17:52:41)
    0000   0xa9 0x74 0x51 0x11 0x0c                   .tQ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 81 CalForBG 2012-09-17T18:55:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2012-09-17T18:55:56)
    0000   0xb8 0x77 0x32 0x11 0x0c                   .w2..
    body (0)
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-35.data: 82 records`
