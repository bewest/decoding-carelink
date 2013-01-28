### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-16.data.list_opcodes.markdown: 5
## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdf 0x80                                  ..
##### DEBUG DECIMAL
            223  128
#### RECORD 0 BolusWizard 2012-11-23T21:56:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2012-11-23T21:56:59)
    0000   0xbb 0xf8 0x15 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0xfe 0x1b 0xf0    $P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
             36   80   13   45  106  254   27  240
              0    0    0   25  125
    HOUR BITS: [1, 1, 1]
#### RECORD 1 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 5.5, 'curve': 20}]
```
--
    0000   0x5c 0x05 0x64 0x5e 0x04                   \.d^.
    decimal
             92    5  100   94    4
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-11-23T23:28:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-11-23T23:28:17)
    0000   0x91 0xdc 0x57 0x17 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 ResultTotals 2012-10-23T13:12:55 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbe                   .....
    decimal
              7    0    0    4  190
    datetime (2012-10-23T13:12:55)
    0000   0xb7 0x8c 0x6d 0xb7 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x4d 0x7a 0x05 0x00 0x00    ..fMz...
    0008   0x04 0xbe 0x03 0x6a 0x48 0x01 0x54 0x1c    ...jH.T.
    0010   0x00 0x73 0x01 0x54 0x1c 0x01 0x54 0x64    .s.T..Td
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102   77  122    5    0    0
              4  190    3  106   72    1   84   28
              0  115    1   84   28    1   84  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 CalForBG 2012-11-24T12:39:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 0}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2012-11-24T12:39:05)
    0000   0x85 0xe7 0x2c 0x18 0x8c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2012-11-24T12:39:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 256,
--
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x00 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             62   80   13   45  106    0   47    0
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 15 Bolus 2012-11-24T22:18:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'programmed': 4.7}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-11-24T22:18:28)
    0000   0x9c 0xd2 0x56 0x18 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 ResultTotals 2012-10-24T13:12:56 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2012-10-24T13:12:56)
    0000   0xb8 0x8c 0x6d 0xb8 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x9a 0x60 0x00 0x03 0x00 0x00    ...`....
    0008   0x04 0x9c 0x03 0x6c 0x4a 0x01 0x30 0x1a    ...lJ.0.
    0010   0x00 0x3e 0x01 0x30 0x1a 0x00 0xbc 0x3e    .>.0...>
    0018   0x00 0x74 0x26 0x00 0x00 0x00 0x02 0x01    .t&.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  154   96    0    3    0    0
              4  156    3  108   74    1   48   26
              0   62    1   48   26    0  188   62
              0  116   38    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 CalForBG 2012-11-25T02:50:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 87}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2012-11-25T02:50:28)
    0000   0x9c 0xf2 0x22 0x19 0x8c                   .."..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 BolusWizard 2012-11-25T02:50:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 343,
--
    0000   0x5c 0x08 0x3a 0x47 0x04 0x9e 0x51 0x04    \.:G..Q.
    decimal
             92    8   58   71    4  158   81    4
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-11-25T20:45:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'programmed': 6.2}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2012-11-25T20:45:33)
    0000   0xa1 0xed 0x54 0x19 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 ResultTotals 2012-10-25T13:12:57 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe4                   .....
    decimal
              7    0    0    5  228
    datetime (2012-10-25T13:12:57)
    0000   0xb9 0x8c 0x6d 0xb9 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x15 0x4a 0x2d 0x5b 0x03 0x00 0x00    ..J-[...
    0008   0x05 0xe4 0x03 0x54 0x38 0x02 0x90 0x2c    ...T8..,
    0010   0x00 0x51 0x02 0x90 0x2c 0x00 0xf8 0x26    .Q..,..&
    0018   0x01 0x98 0x3e 0x00 0x00 0x00 0x03 0x01    ..>.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   74   45   91    3    0    0
              5  228    3   84   56    2  144   44
              0   81    2  144   44    0  248   38
              1  152   62    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 40 CalForBG 2012-11-26T00:10:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-11-26T00:10:23)
    0000   0x97 0xca 0x20 0x1a 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 41 CalForBG 2012-11-26T00:19:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
--
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-11-26T20:40:45)
    0000   0xad 0xe8 0x54 0x1a 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 CalForBG 2012-11-26T22:02:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2012-11-26T22:02:02)
    0000   0x82 0xc2 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 ResultTotals 2012-10-26T13:12:58 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa8                   .....
    decimal
              7    0    0    5  168
    datetime (2012-10-26T13:12:58)
    0000   0xba 0x8c 0x6d 0xba 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa8 0x5f 0xfd 0x07 0x00 0x00    ..._....
    0008   0x05 0xa8 0x03 0x78 0x3d 0x02 0x30 0x27    ...x=.0'
    0010   0x00 0x84 0x02 0x30 0x27 0x01 0x78 0x43    ...0'.xC
    0018   0x00 0xb8 0x21 0x00 0x00 0x00 0x06 0x04    ..!.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  168   95  253    7    0    0
              5  168    3  120   61    2   48   39
              0  132    2   48   39    1  120   67
              0  184   33    0    0    0    6    4
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 PumpSuspend 2012-11-27T13:46:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-27T13:46:56)
    0000   0xb8 0xee 0x0d 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 PumpResume 2012-11-27T14:39:28 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-27T14:39:28)
--
    0000   0x5c 0x05 0x40 0x00 0x14                   \.@..
    decimal
             92    5   64    0   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2012-11-27T18:50:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-11-27T18:50:43)
    0000   0xab 0xf2 0x52 0x1b 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 76 ResultTotals 2012-10-27T13:12:59 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x22                   ...."
    decimal
              7    0    0    4   34
    datetime (2012-10-27T13:12:59)
    0000   0xbb 0x8c 0x6d 0xbb 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8f 0x58 0xc6 0x02 0x00 0x00    ...X....
    0008   0x04 0x22 0x03 0x62 0x52 0x00 0xc0 0x12    .".bR...
    0010   0x00 0x2f 0x00 0xc0 0x12 0x00 0x80 0x43    ./.....C
    0018   0x00 0x40 0x21 0x00 0x00 0x00 0x02 0x01    .@!.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  143   88  198    2    0    0
              4   34    3   98   82    0  192   18
              0   47    0  192   18    0  128   67
              0   64   33    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 77 PumpSuspend 2012-11-28T13:58:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-28T13:58:29)
    0000   0x9d 0xfa 0x0d 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 78 PumpResume 2012-11-28T14:16:48 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-28T14:16:48)
    0000   0xb0 0xd0 0x0e 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 CalForBG 2012-11-28T15:02:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2012-11-28T15:02:16)
    0000   0x90 0xc2 0x2f 0x1c 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-16.data: 80 records`
