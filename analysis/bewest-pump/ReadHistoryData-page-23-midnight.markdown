### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-23.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x3b 0x5c                                  ;\
##### DEBUG DECIMAL
             59   92
#### RECORD 0 BolusGiven unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 0.3, 'curve': 4},
 {'age': 215, 'amount': 0.8, 'curve': 4},
 {'age': 225, 'amount': 0.5, 'curve': 4},
 {'age': 119, 'amount': 1.5, 'curve': 20},
 {'age': 129, 'amount': 2.7, 'curve': 20},
 {'age': 169, 'amount': 1.9, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0c 0x69 0x04 0x20 0xd7 0x04    \..i. ..
    0008   0x14 0xe1 0x04 0x3c 0x77 0x14 0x6c 0x81    ...<w.l.
    0010   0x14 0x4c 0xa9 0x14                        .L..
    decimal
             92   20   12  105    4   32  215    4
             20  225    4   60  119   20  108  129
             20   76  169   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-10-29T18:59:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'programmed': 4.5}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2012-10-29T18:59:38)
    0000   0xa6 0xbb 0x52 0x1d 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalForBG 2012-10-29T19:43:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2012-10-29T19:43:45)
    0000   0xad 0xab 0x33 0x1d 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 ResultTotals (2012, 8, 29, 13, 12, 61) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x8e                   .....
    decimal
              7    0    0    5  142
    datetime ((2012, 8, 29, 13, 12, 61))
    0000   0xbd 0x0c 0x6d 0xbd 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x95 0x67 0xcd 0x0a 0x00 0x00    ...g....
    0008   0x05 0x8e 0x03 0x7a 0x3f 0x02 0x14 0x25    ...z?..%
    0010   0x00 0x80 0x02 0x14 0x25 0x01 0x80 0x48    ....%..H
    0018   0x00 0x94 0x1c 0x00 0x00 0x00 0x06 0x03    ........
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  149  103  205   10    0    0
              5  142    3  122   63    2   20   37
              0  128    2   20   37    1  128   72
              0  148   28    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 4 CalForBG 2012-10-30T11:11:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 192}
```
    op hex (2)
    0000   0x0a 0xc0                                  ..
    decimal
             10  192
    datetime (2012-10-30T11:11:34)
    0000   0xa2 0x8b 0x2b 0x1e 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 BolusWizard 2012-10-30T11:11:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 192,
--
             92   17   16   21    4  152   41    4
            116  111    4   32  171    4   16   35
             20
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2012-10-30T22:25:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-10-30T22:25:04)
    0000   0x84 0x99 0x56 0x1e 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 ResultTotals (2012, 8, 30, 13, 12, 62) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x2c                   ....,
    decimal
              7    0    0    6   44
    datetime ((2012, 8, 30, 13, 12, 62))
    0000   0xbe 0x0c 0x6d 0xbe 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x96 0x46 0xcb 0x0c 0x00 0x00    ...F....
    0008   0x06 0x2c 0x03 0x84 0x39 0x02 0xa8 0x2b    .,..9..+
    0010   0x00 0xbb 0x02 0xa8 0x2b 0x02 0x14 0x4e    ....+..N
    0018   0x00 0x94 0x16 0x00 0x00 0x00 0x09 0x05    ........
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  150   70  203   12    0    0
              6   44    3  132   57    2  168   43
              0  187    2  168   43    2   20   78
              0  148   22    0    0    0    9    5
              3    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 43 PumpSuspend 2012-10-31T13:40:36 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-31T13:40:36)
    0000   0xa4 0xa8 0x0d 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 PumpResume 2012-10-31T13:53:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-31T13:53:02)
--
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2012-10-31T22:17:35)
    0000   0xa3 0x91 0x36 0x1f 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 LowReservoir 2012-10-31T22:50:31 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-31T22:50:31)
    0000   0x9f 0xb2 0x16 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 63 ResultTotals (2012, 8, 31, 13, 12, 63) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9e                   .....
    decimal
              7    0    0    4  158
    datetime ((2012, 8, 31, 13, 12, 63))
    0000   0xbf 0x0c 0x6d 0xbf 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x76 0x3c 0xa6 0x05 0x00 0x00    ..v<....
    0008   0x04 0x9e 0x03 0x7a 0x4b 0x01 0x24 0x19    ...zK.$.
    0010   0x00 0x5d 0x01 0x24 0x19 0x00 0xfc 0x56    .].$...V
    0018   0x00 0x28 0x0e 0x00 0x00 0x00 0x04 0x02    .(......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  118   60  166    5    0    0
              4  158    3  122   75    1   36   25
              0   93    1   36   25    0  252   86
              0   40   14    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 64 PumpSuspend 2012-11-01T10:43:24 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-01T10:43:24)
    0000   0x98 0xeb 0x0a 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 PumpResume 2012-11-01T10:55:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-01T10:55:30)
--
    decimal
             92   11   80   66    4  192   76    4
             32   86    4
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2012-11-01T13:20:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-01T13:20:44)
    0000   0xac 0xd4 0x4d 0x01 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-23.data: 82 records`
