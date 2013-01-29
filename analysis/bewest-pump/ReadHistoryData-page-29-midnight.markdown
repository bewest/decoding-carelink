### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-29.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 1010, found 12 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x99 0x20                                  . 
##### DEBUG DECIMAL
            153   32
#### RECORD 0 hack1 2012-10-08T09:15:28 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xa7 0x0c 0x05 0x00 0xb9 0x5e 0xfd    m.....^.
    0008   0x05 0x00 0x00 0x04 0x52 0x02 0xa6 0x3d    ....R..=
    0010   0x01 0xac 0x27 0x00 0x49 0x01 0xac 0x27    ..'.I..'
    0018   0x00 0xdc 0x33 0x00 0xd0 0x31 0x00 0x00    ..3..1..
    0020   0x00 0x04 0x01 0x02 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x1a              ......
    decimal
            109  167   12    5    0  185   94  253
              5    0    0    4   82    2  166   61
              1  172   39    0   73    1  172   39
              0  220   51    0  208   49    0    0
              0    4    1    2    1    0   12    0
            232    0    0    0   10   26
    datetime (2012-10-08T09:15:28)
    0000   0x9c 0x8f 0x29 0x08 0x8c                   ..)..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 BolusWizard 2012-10-08T09:15:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 282,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
--
    decimal
             92   14   14    5    4  142   15    4
            122   49   20   42   59   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-10-08T20:59:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-10-08T20:59:16)
    0000   0x90 0xbb 0x54 0x08 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 ResultTotals 2012-08-08T13:12:40 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9c                   .....
    decimal
              7    0    0    5  156
    datetime (2012-08-08T13:12:40)
    0000   0xa8 0x0c 0x6d 0xa8 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xab 0x61 0x1a 0x03 0x00 0x00    ...a....
    0008   0x05 0x9c 0x03 0x78 0x3e 0x02 0x24 0x26    ...x>.$&
    0010   0x00 0x8b 0x02 0x24 0x26 0x01 0x9c 0x4b    ...$&..K
    0018   0x00 0x88 0x19 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  171   97   26    3    0    0
              5  156    3  120   62    2   36   38
              0  139    2   36   38    1  156   75
              0  136   25    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 17 CalBGForPH 2012-10-09T00:59:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2012-10-09T00:59:34)
    0000   0xa2 0xbb 0x20 0x09 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 BolusWizard 2012-10-09T00:59:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
--
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-09T18:26:59)
    0000   0xbb 0x9a 0x12 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 45 Bolus 2012-10-09T18:26:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-10-09T18:26:45)
    0000   0xad 0x9a 0x52 0x09 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 ResultTotals 2012-08-09T13:12:41 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x72                   ....r
    decimal
              7    0    0    5  114
    datetime (2012-08-09T13:12:41)
    0000   0xa9 0x0c 0x6d 0xa9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x96 0x73 0xb6 0x03 0x00 0x00    ...s....
    0008   0x05 0x72 0x03 0x76 0x40 0x01 0xfc 0x24    .r.v@..$
    0010   0x00 0x91 0x01 0xfc 0x24 0x01 0xb4 0x56    ....$..V
    0018   0x00 0x48 0x0e 0x00 0x00 0x00 0x07 0x05    .H......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  150  115  182    3    0    0
              5  114    3  118   64    1  252   36
              0  145    1  252   36    1  180   86
              0   72   14    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 47 CalBGForPH 2012-10-10T01:48:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2012-10-10T01:48:14)
    0000   0x8e 0xb0 0x21 0x0a 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 BolusWizard 2012-10-10T01:48:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
--
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-10-10T17:13:57)
    0000   0xb9 0x8d 0x31 0x0a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 68 CalBGForPH 2012-10-10T17:14:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2012-10-10T17:14:01)
    0000   0x81 0x8e 0x31 0x0a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 ResultTotals 2012-08-10T13:12:42 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime (2012-08-10T13:12:42)
    0000   0xaa 0x0c 0x6d 0xaa 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb6 0x8d 0x23 0x05 0x00 0x00    ....#...
    0008   0x04 0xd2 0x03 0x72 0x47 0x01 0x60 0x1d    ...rG.`.
    0010   0x00 0x36 0x01 0x60 0x1d 0x00 0xa0 0x2d    .6.`...-
    0018   0x00 0xc0 0x37 0x00 0x00 0x00 0x04 0x02    ..7.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  182  141   35    5    0    0
              4  210    3  114   71    1   96   29
              0   54    1   96   29    0  160   45
              0  192   55    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 70 PumpSuspend 2012-10-11T10:51:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-11T10:51:33)
    0000   0xa1 0xb3 0x0a 0x0b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 PumpResume 2012-10-11T11:06:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-11T11:06:50)
--
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    0    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 Bolus 2012-10-11T21:37:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'programmed': 1.4}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2012-10-11T21:37:04)
    0000   0x84 0xa5 0x55 0x0b 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-29.data: 78 records`
