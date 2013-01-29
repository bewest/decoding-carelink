### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-7.data.list_opcodes.markdown: 2
## START logs/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x68 0x81                                  h.
##### DEBUG DECIMAL
            104  129
#### RECORD 0 BolusWizard 2012-12-28T07:48:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.5,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2012-12-28T07:48:24)
    0000   0xd8 0x30 0x07 0x1c 0x0c                   .0...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x09 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x37 0x7d                   ...7}
    decimal
             60   80   13   45  106    9   46    0
              0    0    0   55  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 LowReservoir 2012-12-28T07:49:08 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
--
    decimal
             92   14  180   67    4   12   77    4
            132  157    4  128  111   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-12-28T19:31:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-12-28T19:31:07)
    0000   0xc7 0x1f 0x53 0x1c 0x0c                   ..S..
    body (0)

#### RECORD 28 ResultTotals 2012-12-28T13:12:28 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x6c                   ....l
    decimal
              7    0    0    6  108
    datetime (2012-12-28T13:12:28)
    0000   0xdc 0x0c 0x6d 0xdc 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb7 0x58 0x22 0x07 0x00 0x00    ...X"...
    0008   0x06 0x6c 0x03 0x84 0x37 0x02 0xe8 0x2d    .l..7..-
    0010   0x00 0xbe 0x02 0xe8 0x2d 0x02 0x30 0x4b    ....-.0K
    0018   0x00 0xb8 0x19 0x00 0x00 0x00 0x06 0x02    ........
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  183   88   34    7    0    0
              6  108    3  132   55    2  232   45
              0  190    2  232   45    2   48   75
              0  184   25    0    0    0    6    2
              2    2    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2012-12-29T01:45:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-29T01:45:15)
    0000   0xcf 0x2d 0x21 0x1d 0x0c                   .-!..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 BolusWizard 2012-12-29T01:45:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 108,
--
             92   17   60  109    4  150  129    4
             86  139    4   12  189    4  116  143
             20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2012-12-29T21:23:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-12-29T21:23:46)
    0000   0xee 0x17 0x55 0x1d 0x0c                   ..U..
    body (0)

#### RECORD 56 ResultTotals 2012-12-29T13:12:29 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime (2012-12-29T13:12:29)
    0000   0xdd 0x0c 0x6d 0xdd 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x87 0x4b 0xba 0x05 0x00 0x00    ...K....
    0008   0x05 0xe8 0x03 0x68 0x3a 0x02 0x80 0x2a    ...h:..*
    0010   0x00 0xc3 0x02 0x80 0x2a 0x02 0x34 0x58    ....*.4X
    0018   0x00 0x4c 0x0c 0x00 0x00 0x00 0x07 0x04    .L......
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  135   75  186    5    0    0
              5  232    3  104   58    2  128   42
              0  195    2  128   42    2   52   88
              0   76   12    0    0    0    7    4
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 57 CalBGForPH 2012-12-30T11:31:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2012-12-30T11:31:25)
    0000   0xd9 0x1f 0x2b 0x1e 0x0c                   ..+..
    body (0)

#### RECORD 58 BolusWizard 2012-12-30T11:32:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 187,
--
             20    8  134   20   10  144   20    8
            154   20   10  164   20    8  174   20
             80  184   20
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2012-12-30T21:44:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-30T21:44:54)
    0000   0xf6 0x2c 0x55 0x1e 0x0c                   .,U..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-7.data: 81 records`
