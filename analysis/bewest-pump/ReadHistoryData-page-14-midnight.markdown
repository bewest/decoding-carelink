### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-14.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xea 0x8f                                  ..
##### DEBUG DECIMAL
            234  143
#### RECORD 0 Bolus 2012-12-02T15:50:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-02T15:50:27)
    0000   0xdb 0x32 0x4f 0x02 0x0c                   .2O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 CalBGForPH 2012-12-02T18:30:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2012-12-02T18:30:09)
    0000   0xc9 0x1e 0x32 0x02 0x0c                   ..2..
    body (0)

#### RECORD 2 BolusWizard 2012-12-02T18:30:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 190,
 'bg_target_high': 125,
 'bg_target_low': 106,
--
    decimal
             92   11  124   77    4   36    1   20
             12  161   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2012-12-02T22:41:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-12-02T22:41:49)
    0000   0xf1 0x29 0x56 0x02 0x0c                   .)V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 ResultTotals 2012-12-02T13:12:02 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x06                   .....
    decimal
              7    0    0    6    6
    datetime (2012-12-02T13:12:02)
    0000   0xc2 0x0c 0x6d 0xc2 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb1 0x60 0x8b 0x09 0x00 0x00    ...`....
    0008   0x06 0x06 0x03 0x7c 0x3a 0x02 0x8a 0x2a    ...|:..*
    0010   0x00 0x64 0x02 0x8a 0x2a 0x01 0x2e 0x2e    .d..*...
    0018   0x01 0x5c 0x36 0x00 0x00 0x00 0x07 0x03    .\6.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  177   96  139    9    0    0
              6    6    3  124   58    2  138   42
              0  100    2  138   42    1   46   46
              1   92   54    0    0    0    7    3
              4    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2012-12-03T04:09:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2012-12-03T04:09:49)
    0000   0xf1 0x09 0x24 0x03 0x8c                   ..$..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2012-12-03T04:09:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 276,
--
             22  127   20   22  137   20   22  147
             20   22  157   20   22  167   20    6
            177   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2012-12-03T20:47:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-03T20:47:01)
    0000   0xc1 0x2f 0x54 0x03 0x0c                   ./T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 ResultTotals 2012-12-03T13:12:03 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-12-03T13:12:03)
    0000   0xc3 0x0c 0x6d 0xc3 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb7 0x4d 0x14 0x03 0x00 0x00    ...M....
    0008   0x05 0x0c 0x03 0x7c 0x45 0x01 0x90 0x1f    ...|E...
    0010   0x00 0x5f 0x01 0x90 0x1f 0x01 0x04 0x41    ._.....A
    0018   0x00 0x8c 0x23 0x00 0x00 0x00 0x04 0x03    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  183   77   20    3    0    0
              5   12    3  124   69    1  144   31
              0   95    1  144   31    1    4   65
              0  140   35    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 36 PumpSuspend 2012-12-04T11:17:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-04T11:17:38)
    0000   0xe6 0x11 0x0b 0x04 0x0c                   .....
    body (0)

#### RECORD 37 PumpResume 2012-12-04T11:17:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-04T11:17:55)
--
             92   17   76  108    4   40  152   20
              4  182   20  168  192   20   44  212
             20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2012-12-04T20:32:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'programmed': 5.5}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2012-12-04T20:32:54)
    0000   0xf6 0x20 0x54 0x04 0x0c                   . T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 ResultTotals 2012-12-04T13:12:04 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9e                   .....
    decimal
              7    0    0    5  158
    datetime (2012-12-04T13:12:04)
    0000   0xc4 0x0c 0x6d 0xc4 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xaa 0x89 0xc6 0x03 0x00 0x00    ........
    0008   0x05 0x9e 0x03 0x76 0x3e 0x02 0x28 0x26    ...v>.(&
    0010   0x00 0x8f 0x02 0x28 0x26 0x01 0xb0 0x4e    ...(&..N
    0018   0x00 0x78 0x16 0x00 0x00 0x00 0x05 0x03    .x......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  170  137  198    3    0    0
              5  158    3  118   62    2   40   38
              0  143    2   40   38    1  176   78
              0  120   22    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 58 CalBGForPH 2012-12-05T00:08:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-12-05T00:08:18)
    0000   0xd2 0x08 0x20 0x05 0x0c                   .. ..
    body (0)

#### RECORD 59 CalBGForPH 2012-12-05T23:56:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
--
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0xfa 0x28 0xf0    4P.-j.(.
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             52   80   13   45  106  250   40  240
              0    0    0   34  125
    HOUR BITS: [0, 0, 1]
#### RECORD 61 Bolus 2012-12-05T23:56:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-12-05T23:56:51)
    0000   0xf3 0x38 0x57 0x05 0x0c                   .8W..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 62 ResultTotals 2012-12-05T13:12:05 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x0c                   .....
    decimal
              7    0    0    4   12
    datetime (2012-12-05T13:12:05)
    0000   0xc5 0x0c 0x6d 0xc5 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x4a 0x43 0x50 0x02 0x00 0x00    ..JCP...
    0008   0x04 0x0c 0x03 0x84 0x57 0x00 0x88 0x0d    ....W...
    0010   0x00 0x34 0x00 0x88 0x0d 0x00 0x88 0x64    .4.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   74   67   80    2    0    0
              4   12    3  132   87    0  136   13
              0   52    0  136   13    0  136  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 63 CalBGForPH 2012-12-06T02:56:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2012-12-06T02:56:25)
    0000   0xd9 0x38 0x22 0x06 0x0c                   .8"..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 PumpSuspend 2012-12-06T10:47:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
--
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2012-12-06T19:10:46)
    0000   0xee 0x0a 0x13 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xfe 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             50   80   13   45  106  254   38  240
              0    0    0   36  125

`end logs/ReadHistoryData-page-14.data: 76 records`
