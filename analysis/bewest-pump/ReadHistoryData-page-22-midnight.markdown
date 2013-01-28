### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-22.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-22.data
#### RECORD 0 CalForBG 2012-11-01T15:43:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2012-11-01T15:43:51)
    0000   0xb3 0xeb 0x2f 0x01 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 CalForBG 2012-11-01T16:54:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2012-11-01T16:54:55)
    0000   0xb7 0xf6 0x30 0x01 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 CalForBG 2012-11-01T18:23:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2012-11-01T18:23:40)
    0000   0xa8 0xd7 0x32 0x01 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2012-11-01T18:23:49 head[2], body[13] op[0x5b]
--
    decimal
             92   14   48   53   20   80  113   20
            192  123   20   32  133   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-11-01T18:23:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-11-01T18:23:49)
    0000   0xb1 0xd7 0x52 0x01 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 ResultTotals 2012-10-01T13:12:33 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x3a                   ....:
    decimal
              7    0    0    5   58
    datetime (2012-10-01T13:12:33)
    0000   0xa1 0x8c 0x6d 0xa1 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x36 0x88 0x05 0x00 0x00    ..f6....
    0008   0x05 0x3a 0x03 0x7a 0x43 0x01 0xc0 0x21    .:.zC..!
    0010   0x00 0x88 0x01 0xc0 0x21 0x01 0x9c 0x5c    ....!..\
    0018   0x00 0x24 0x08 0x00 0x00 0x00 0x05 0x03    .$......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102   54  136    5    0    0
              5   58    3  122   67    1  192   33
              0  136    1  192   33    1  156   92
              0   36    8    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 PumpSuspend 2012-11-02T13:45:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-02T13:45:01)
    0000   0x81 0xed 0x0d 0x02 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 PumpResume 2012-11-02T14:00:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-02T14:00:33)
--
    decimal
             92   14   68  208    4   36  218    4
             40  142   20   48  182   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-11-02T23:32:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'programmed': 5.3}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2012-11-02T23:32:36)
    0000   0xa4 0xe0 0x57 0x02 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 ResultTotals 2012-10-02T13:12:34 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb4                   .....
    decimal
              7    0    0    5  180
    datetime (2012-10-02T13:12:34)
    0000   0xa2 0x8c 0x6d 0xa2 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x65 0x4d 0x95 0x05 0x00 0x00    ..eM....
    0008   0x05 0xb4 0x03 0x78 0x3d 0x02 0x3c 0x27    ...x=.<'
    0010   0x00 0xc6 0x02 0x3c 0x27 0x02 0x3c 0x64    ...<'.<d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  101   77  149    5    0    0
              5  180    3  120   61    2   60   39
              0  198    2   60   39    2   60  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 CalForBG 2012-11-03T03:52:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-11-03T03:52:28)
    0000   0x9c 0xf4 0x23 0x03 0x0c                   ..#..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 CalForBG 2012-11-03T03:53:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
--
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x01 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             62   80   13   45  106    1   47    0
              0    0    0   48  125
    HOUR BITS: [1, 1, 0]
#### RECORD 52 Bolus 2012-11-03T21:29:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'programmed': 4.8}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-11-03T21:29:42)
    0000   0xaa 0xdd 0x55 0x03 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 ResultTotals 2012-10-03T13:12:35 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xc0                   .....
    decimal
              7    0    0    5  192
    datetime (2012-10-03T13:12:35)
    0000   0xa3 0x8c 0x6d 0xa3 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb8 0x2d 0xa8 0x08 0x00 0x00    ...-....
    0008   0x05 0xc0 0x03 0xa8 0x40 0x02 0x18 0x24    ....@..$
    0010   0x00 0x3e 0x02 0x18 0x24 0x00 0xbc 0x23    .>..$..#
    0018   0x01 0x5c 0x41 0x00 0x00 0x00 0x04 0x00    .\A.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  184   45  168    8    0    0
              5  192    3  168   64    2   24   36
              0   62    2   24   36    0  188   35
              1   92   65    0    0    0    4    0
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 CalForBG 2012-11-04T01:25:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2012-11-04T01:25:52)
    0000   0xb4 0xd9 0x21 0x04 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 BolusWizard 2012-11-04T01:25:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 214,
--
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-04T22:39:51)
    0000   0xb3 0xe7 0x56 0x04 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 86 LowReservoir 2012-11-04T23:53:41 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-04T23:53:41)
    0000   0xa9 0xf5 0x17 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 87 ResultTotals 2005-10-03T00:12:36 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x64                   ....d
    decimal
              7    0    0    5  100
    datetime (2005-10-03T00:12:36)
    0000   0xa4 0x8c 0x00 0x23 0x85                   ...#.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-22.data: 88 records`
