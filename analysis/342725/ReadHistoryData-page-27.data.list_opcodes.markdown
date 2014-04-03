## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 54, found 19 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0c 0x00 0xe8 0x00 0x00 0x00 0x21 0x00    ......!.
    0008   0x55 0x04 0x00 0x0e 0x0d 0x03 0x00 0x00    U.......
    0010   0x00 0x2e 0x43 0x05 0x20 0x0e 0x0d 0x03    ..C. ...
    0018   0x00 0x05 0x00 0x05 0x5e 0x05 0x00 0x0e    ....^...
##### DEBUG DECIMAL
             12    0  232    0    0    0   33    0
             85    4    0   14   13    3    0    0
              0   46   67    5   32   14   13    3
              0    5    0    5   94    5    0   14
#### RECORD 0 CalBGForPH 2013-04-13T00:51:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-04-13T00:51:27)
    0000   0x5b 0x33 0x20 0x0d 0x0d                   [3 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 PumpSuspend 2013-04-13T09:34:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-13T09:34:42)
    0000   0x6a 0x22 0x09 0x0d 0x0d                   j"...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 PumpResume 2013-04-13T09:39:11 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-13T09:39:11)
    0000   0x4b 0x27 0x09 0x0d 0x0d                   K'...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 LowReservoir 2013-04-13T11:10:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-13T11:10:54)
    0000   0x76 0x0a 0x0b 0x0d 0x0d                   v....
    body (0)

#### RECORD 4 MResultTotals 2013-04-14T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x80                   .....
    decimal
              7    0    0    3  128
    datetime (2013-04-14T00:00:00)
    0000   0x4d 0x0d                                  M.
    body (3)
    hex
    0000   0x6d 0x4d 0x0d                             mM.
    decimal
            109   77   13

#### RECORD 5 Base (2000, 5, 1, 26, 26, 26) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 5, 1, 26, 26, 26))
    0000   0x5a 0x5a 0x5a 0x01 0x00                   ZZZ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 8, 4, 0, 3, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x03                                  ..
    decimal
              0    3
    datetime ((2000, 8, 4, 0, 3, 0))
    0000   0x80 0x03 0x80 0x64 0x00                   ...d.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-27.data: 7 records`
