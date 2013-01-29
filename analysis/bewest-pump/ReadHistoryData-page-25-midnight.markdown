### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-25.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x38 0xa2                                  8.
##### DEBUG DECIMAL
             56  162
#### RECORD 0 Bolus 2012-10-23T20:03:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-10-23T20:03:54)
    0000   0xb6 0x83 0x54 0x17 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 1 LowReservoir 2012-10-23T20:50:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-23T20:50:31)
    0000   0x9f 0xb2 0x14 0x17 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2012-10-23T20:53:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 208}
```
    op hex (2)
--
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2012-10-23T21:06:22)
    0000   0x96 0x86 0x35 0x17 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 CalBGForPH 2012-10-23T23:01:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2012-10-23T23:01:11)
    0000   0x8b 0x81 0x37 0x17 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 ResultTotals 2012-08-23T13:12:55 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x70                   ....p
    decimal
              7    0    0    5  112
    datetime (2012-08-23T13:12:55)
    0000   0xb7 0x0c 0x6d 0xb7 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x95 0x4b 0xda 0x09 0x00 0x00    ...K....
    0008   0x05 0x70 0x03 0x6c 0x3f 0x02 0x04 0x25    .p.l?..%
    0010   0x00 0x73 0x02 0x04 0x25 0x01 0x5c 0x43    .s..%.\C
    0018   0x00 0xa8 0x21 0x00 0x00 0x00 0x06 0x03    ..!.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  149   75  218    9    0    0
              5  112    3  108   63    2    4   37
              0  115    2    4   37    1   92   67
              0  168   33    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 9 CalBGForPH 2012-10-24T00:51:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2012-10-24T00:51:29)
    0000   0x9d 0xb3 0x20 0x18 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 10 BolusWizard 2012-10-24T00:51:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
--
    decimal
             92   11   72   11    4  112   75   20
             16  175   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-10-24T23:45:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-10-24T23:45:00)
    0000   0x80 0xad 0x57 0x18 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 ResultTotals 2012-08-24T13:12:56 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf2                   .....
    decimal
              7    0    0    4  242
    datetime (2012-08-24T13:12:56)
    0000   0xb8 0x0c 0x6d 0xb8 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x56 0xc4 0x0d 0x00 0x00    ...V....
    0008   0x04 0xf2 0x03 0x72 0x46 0x01 0x80 0x1e    ...rF...
    0010   0x00 0x77 0x01 0x80 0x1e 0x01 0x4c 0x56    .w....LV
    0018   0x00 0x34 0x0e 0x00 0x00 0x00 0x07 0x03    .4......
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140   86  196   13    0    0
              4  242    3  114   70    1  128   30
              0  119    1  128   30    1   76   86
              0   52   14    0    0    0    7    3
              3    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 49 PumpSuspend 2012-10-25T11:04:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-25T11:04:15)
    0000   0x8f 0x84 0x0b 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 PumpResume 2012-10-25T11:06:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-25T11:06:02)
--
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-10-25T20:38:24)
    0000   0x98 0xa6 0x54 0x19 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 CalBGForPH 2012-10-25T21:53:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2012-10-25T21:53:35)
    0000   0xa3 0xb5 0x35 0x19 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 ResultTotals 2012-08-25T13:12:57 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime (2012-08-25T13:12:57)
    0000   0xb9 0x0c 0x6d 0xb9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa6 0x61 0x0a 0x06 0x00 0x00    ...a....
    0008   0x05 0x00 0x03 0x78 0x45 0x01 0x88 0x1f    ...xE...
    0010   0x00 0x33 0x01 0x88 0x1f 0x00 0x98 0x27    .3.....'
    0018   0x00 0xf0 0x3d 0x00 0x00 0x00 0x04 0x02    ..=.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  166   97   10    6    0    0
              5    0    3  120   69    1  136   31
              0   51    1  136   31    0  152   39
              0  240   61    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 73 PumpSuspend 2012-10-26T03:57:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-26T03:57:03)
    0000   0x83 0xb9 0x03 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 PumpResume 2012-10-26T09:34:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-26T09:34:18)
--
    0000   0x5c 0x08 0x50 0xdd 0x04 0xbc 0x91 0x14    \.P.....
    decimal
             92    8   80  221    4  188  145   20
    datetime (unknown)

    body (0)

#### RECORD 89 Bolus 2012-10-26T16:15:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-10-26T16:15:54)
    0000   0xb6 0x8f 0x50 0x1a 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-25.data: 90 records`
