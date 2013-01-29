### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-28.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x71 0x0c                                  q.
##### DEBUG DECIMAL
            113   12
#### RECORD 0 BolusWizard 2012-10-11T22:45:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-11T22:45:49)
    0000   0xb1 0xad 0x16 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              8   80   13   45  106    0    6    0
              0    0    0    6  125
--
    0000   0x5c 0x08 0x18 0x3a 0x04 0x38 0x80 0x04    \..:.8..
    decimal
             92    8   24   58    4   56  128    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-10-11T23:42:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-10-11T23:42:16)
    0000   0x90 0xaa 0x57 0x0b 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 7 ResultTotals 2012-08-11T13:12:43 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb8                   .....
    decimal
              7    0    0    4  184
    datetime (2012-08-11T13:12:43)
    0000   0xab 0x0c 0x6d 0xab 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x92 0x46 0xd1 0x03 0x00 0x00    ...F....
    0008   0x04 0xb8 0x03 0x78 0x4a 0x01 0x40 0x1a    ...xJ.@.
    0010   0x00 0x61 0x01 0x40 0x1a 0x01 0x08 0x52    .a.@...R
    0018   0x00 0x38 0x12 0x00 0x00 0x00 0x04 0x03    .8......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  146   70  209    3    0    0
              4  184    3  120   74    1   64   26
              0   97    1   64   26    1    8   82
              0   56   18    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 8 PumpSuspend 2012-10-12T10:56:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-12T10:56:33)
    0000   0xa1 0xb8 0x0a 0x0c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 PumpResume 2012-10-12T12:36:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-12T12:36:39)
--
    decimal
             92   14   68  100    4  106  140    4
             14  150    4  124  180    4
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2012-10-12T15:34:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-10-12T15:34:14)
    0000   0x8e 0xa2 0x4f 0x0c 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 ResultTotals 2012-08-12T13:12:44 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb2                   .....
    decimal
              7    0    0    4  178
    datetime (2012-08-12T13:12:44)
    0000   0xac 0x0c 0x6d 0xac 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x5e 0x5e 0x5e 0x01 0x00 0x00    ..^^^...
    0008   0x04 0xb2 0x03 0x3a 0x45 0x01 0x78 0x1f    ...:E.x.
    0010   0x00 0x80 0x01 0x78 0x1f 0x01 0x78 0x64    ...x..xd
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x04 0x04    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   94   94   94    1    0    0
              4  178    3   58   69    1  120   31
              0  128    1  120   31    1  120  100
              0    0    0    0    0    0    4    4
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 23 CalBGForPH 2012-10-13T01:15:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2012-10-13T01:15:21)
    0000   0x95 0x8f 0x21 0x0d 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 BolusWizard 2012-10-13T01:15:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
--
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-13T22:53:33)
    0000   0xa1 0xb5 0x16 0x0d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 Bolus 2012-10-13T22:52:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'programmed': 4.7}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-10-13T22:52:49)
    0000   0xb1 0xb4 0x56 0x0d 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 34 ResultTotals 2012-08-13T13:12:45 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x3c                   ....<
    decimal
              7    0    0    5   60
    datetime (2012-08-13T13:12:45)
    0000   0xad 0x0c 0x6d 0xad 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x9c 0x59 0xf5 0x03 0x00 0x00    ...Y....
    0008   0x05 0x3c 0x03 0x84 0x43 0x01 0xb8 0x21    .<..C..!
    0010   0x00 0x76 0x01 0xb8 0x21 0x01 0x58 0x4e    .v..!.XN
    0018   0x00 0x60 0x16 0x00 0x00 0x00 0x03 0x01    .`......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  156   89  245    3    0    0
              5   60    3  132   67    1  184   33
              0  118    1  184   33    1   88   78
              0   96   22    0    0    0    3    1
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 35 CalBGForPH 2012-10-14T03:34:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2012-10-14T03:34:17)
    0000   0x91 0xa2 0x23 0x0e 0x0c                   ..#..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 LowReservoir 2012-10-14T06:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
--
    decimal
             92   11   40   71    4  102  121    4
             50  131    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2012-10-14T21:35:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-10-14T21:35:17)
    0000   0x91 0xa3 0x55 0x0e 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 59 ResultTotals 2012-08-14T13:12:46 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x64                   ....d
    decimal
              7    0    0    5  100
    datetime (2012-08-14T13:12:46)
    0000   0xae 0x0c 0x6d 0xae 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xda 0x81 0x1b 0x07 0x00 0x00    ........
    0008   0x05 0x64 0x03 0x78 0x40 0x01 0xec 0x24    .d.x@..$
    0010   0x00 0x4b 0x01 0xec 0x24 0x00 0xe0 0x2e    .K..$...
    0018   0x01 0x0c 0x36 0x00 0x00 0x00 0x04 0x01    ..6.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  218  129   27    7    0    0
              5  100    3  120   64    1  236   36
              0   75    1  236   36    0  224   46
              1   12   54    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 60 CalBGForPH 2012-10-15T05:14:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 444}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2012-10-15T05:14:58)
    0000   0xba 0x8e 0x25 0x0f 0x8c                   ..%..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 TempBasal 2012-10-15T05:16:09 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.05}
--
    0000   0x03 0x00 0x00 0x00 0x21                   ....!
    decimal
              3    0    0    0   33
    datetime (2012-10-15T11:37:44)
    0000   0xac 0xa5 0x2b 0x0f 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 82 Prime 2012-10-15T11:38:04 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-10-15T11:38:04)
    0000   0x84 0xa6 0x0b 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-28.data: 83 records`
