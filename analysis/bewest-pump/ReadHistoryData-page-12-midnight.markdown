### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-12.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 1011, found 11 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0xe7                                  l.
##### DEBUG DECIMAL
            108  231
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.5, 'curve': 4},
 {'age': 212, 'amount': 0.15, 'curve': 20},
 {'age': 222, 'amount': 3.65, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x08 0x04 0x06 0xd4 0x14    \.......
    0008   0x92 0xde 0x14                             ...
    decimal
             92   11   20    8    4    6  212   20
            146  222   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-12-10T03:52:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8, 'dual_component': '??', 'programmed': 5.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3a 0x3a 0x00                        .::.
    decimal
              1   58   58    0
    datetime (2012-12-10T03:52:35)
    0000   0xe3 0x34 0x43 0x0a 0x0c                   .4C..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 PumpSuspend 2012-12-10T13:08:44 head[2], body[0] op[0x1e]

--
    decimal
             92   11  136  104   20   92  174   20
             16  194   20
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2012-12-10T21:04:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2012-12-10T21:04:55)
    0000   0xf7 0x04 0x55 0x0a 0x0c                   ..U..
    body (0)

#### RECORD 18 ResultTotals 2012-12-10T13:12:10 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x12                   .....
    decimal
              7    0    0    6   18
    datetime (2012-12-10T13:12:10)
    0000   0xca 0x0c 0x6d 0xca 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x11 0x1d 0x7b 0x9b 0x05 0x00 0x00    ...{....
    0008   0x06 0x12 0x03 0x72 0x39 0x02 0xa0 0x2b    ...r9..+
    0010   0x00 0x4b 0x02 0xa0 0x2b 0x00 0xe4 0x22    .K..+.."
    0018   0x01 0xbc 0x42 0x00 0x00 0x00 0x06 0x02    ..B.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17   29  123  155    5    0    0
              6   18    3  114   57    2  160   43
              0   75    2  160   43    0  228   34
              1  188   66    0    0    0    6    2
              4    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 19 PumpSuspend 2012-12-11T08:49:52 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-11T08:49:52)
    0000   0xf4 0x31 0x08 0x0b 0x0c                   .1...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 PumpResume 2012-12-11T13:26:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-11T13:26:59)
--
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-11T19:56:16)
    0000   0xd0 0x38 0x53 0x0b 0x0c                   .8S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 CalBGForPH 2012-12-11T20:10:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 138}
```
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2012-12-11T20:10:13)
    0000   0xcd 0x0a 0x34 0x0b 0x0c                   ..4..
    body (0)

#### RECORD 56 ResultTotals 2012-12-11T13:12:11 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x20                   .... 
    decimal
              7    0    0    5   32
    datetime (2012-12-11T13:12:11)
    0000   0xcb 0x0c 0x6d 0xcb 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xba 0x6c 0xed 0x09 0x00 0x00    ...l....
    0008   0x05 0x20 0x02 0xb4 0x35 0x02 0x6c 0x2f    . ..5.l/
    0010   0x00 0xa8 0x02 0x6c 0x2f 0x01 0xfc 0x52    ...l/..R
    0018   0x00 0x70 0x12 0x00 0x00 0x00 0x07 0x05    .p......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  186  108  237    9    0    0
              5   32    2  180   53    2  108   47
              0  168    2  108   47    1  252   82
              0  112   18    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 57 PumpSuspend 2012-12-12T15:42:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-12T15:42:30)
    0000   0xde 0x2a 0x0f 0x0c 0x0c                   .*...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 PumpResume 2012-12-12T16:06:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-12T16:06:03)
--
    0000   0x5c 0x05 0x5c 0xe7 0x04                   \.\..
    decimal
             92    5   92  231    4
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2012-12-12T20:55:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2012-12-12T20:55:56)
    0000   0xf8 0x37 0x54 0x0c 0x0c                   .7T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 ResultTotals 2012-12-12T13:12:12 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x78                   ....x
    decimal
              7    0    0    4  120
    datetime (2012-12-12T13:12:12)
    0000   0xcc 0x0c 0x6d 0xcc 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x70 0x46 0xab 0x04 0x00 0x00    ..pF....
    0008   0x04 0x78 0x03 0x74 0x4d 0x01 0x04 0x17    .x.tM...
    0010   0x00 0x56 0x01 0x04 0x17 0x00 0xe4 0x58    .V.....X
    0018   0x00 0x20 0x0c 0x00 0x00 0x00 0x02 0x01    . ......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  112   70  171    4    0    0
              4  120    3  116   77    1    4   23
              0   86    1    4   23    0  228   88
              0   32   12    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 72 PumpSuspend 2012-12-13T11:03:12 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-13T11:03:12)
    0000   0xcc 0x03 0x0b 0x0d 0x0c                   .....
    body (0)

#### RECORD 73 PumpResume 2012-12-13T11:23:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-13T11:23:22)
--
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-12-13T14:14:34)
    0000   0xe2 0x0e 0x4e 0x0d 0x0c                   ..N..
    body (0)

#### RECORD 83 CalBGForPH 2012-12-13T18:36:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2012-12-13T18:36:00)
    0000   0xc0 0x24 0x32 0x0d 0x0c                   .$2..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-12.data: 84 records`
