### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-13.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb7 0x62                                  .b
##### DEBUG DECIMAL
            183   98
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 4.4, 'curve': 20},
 {'age': 210, 'amount': 3.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xb0 0x82 0x14 0x84 0xd2 0x14    \.......
    decimal
             92    8  176  130   20  132  210   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-12-06T19:10:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-12-06T19:10:46)
    0000   0xee 0x0a 0x53 0x06 0x0c                   ..S..
    body (0)

#### RECORD 2 ResultTotals 2012-12-06T13:12:06 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x3c                   ....<
    decimal
              7    0    0    5   60
    datetime (2012-12-06T13:12:06)
    0000   0xc6 0x0c 0x6d 0xc6 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa9 0x60 0x12 0x05 0x00 0x00    ...`....
    0008   0x05 0x3c 0x03 0x78 0x42 0x01 0xc4 0x22    .<.xB.."
    0010   0x00 0x6c 0x01 0xc4 0x22 0x01 0x40 0x47    .l..".@G
    0018   0x00 0x84 0x1d 0x00 0x00 0x00 0x03 0x02    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  169   96   18    5    0    0
              5   60    3  120   66    1  196   34
              0  108    1  196   34    1   64   71
              0  132   29    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 3 LowReservoir 2012-12-07T11:02:43 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-07T11:02:43)
    0000   0xeb 0x02 0x0b 0x07 0x0c                   .....
    body (0)

#### RECORD 4 BolusWizard 2012-12-07T16:47:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
--
    decimal
             92   11  184   83   20  184   93   20
             64  133   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2012-12-07T23:13:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-12-07T23:13:43)
    0000   0xeb 0x0d 0x57 0x07 0x0c                   ..W..
    body (0)

#### RECORD 22 ResultTotals 2012-12-07T13:12:07 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x68                   ....h
    decimal
              7    0    0    5  104
    datetime (2012-12-07T13:12:07)
    0000   0xc7 0x0c 0x6d 0xc7 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x4e 0x4e 0x4e 0x01 0x00 0x00    ..NNN...
    0008   0x05 0x68 0x03 0x68 0x3f 0x02 0x00 0x25    .h.h?..%
    0010   0x00 0xaa 0x02 0x00 0x25 0x02 0x00 0x64    ....%..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x04 0x04    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   78   78   78    1    0    0
              5  104    3  104   63    2    0   37
              0  170    2    0   37    2    0  100
              0    0    0    0    0    0    4    4
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 23 CalBGForPH 2012-12-08T16:18:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-12-08T16:18:48)
    0000   0xf0 0x12 0x30 0x08 0x0c                   ..0..
    body (0)

#### RECORD 24 BolusWizard 2012-12-08T16:19:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 96,
--
             92   20   14    5    4    6   15    4
             56   45    4   24  175    4  116   19
             20   36  149   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-12-08T22:59:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-08T22:59:08)
    0000   0xc8 0x3b 0x56 0x08 0x0c                   .;V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 ResultTotals 2012-12-08T13:12:08 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2012-12-08T13:12:08)
    0000   0xc8 0x0c 0x6d 0xc8 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x86 0x60 0xd8 0x06 0x00 0x00    ...`....
    0008   0x04 0x9c 0x03 0x78 0x4b 0x01 0x24 0x19    ...xK.$.
    0010   0x00 0x5e 0x01 0x24 0x19 0x01 0x10 0x5d    .^.$...]
    0018   0x00 0x14 0x07 0x00 0x00 0x00 0x06 0x05    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  134   96  216    6    0    0
              4  156    3  120   75    1   36   25
              0   94    1   36   25    1   16   93
              0   20    7    0    0    0    6    5
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2012-12-09T10:36:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 4,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
--
    0000   0x5c 0x05 0x20 0xa7 0x04                   \. ..
    decimal
             92    5   32  167    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2012-12-09T20:01:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'programmed': 3.8}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-12-09T20:01:32)
    0000   0xe0 0x01 0x54 0x09 0x0c                   ..T..
    body (0)

#### RECORD 69 ResultTotals 2012-12-09T13:12:09 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime (2012-12-09T13:12:09)
    0000   0xc9 0x0c 0x6d 0xc9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x67 0xaa 0x04 0x00 0x00    ...g....
    0008   0x05 0x00 0x03 0x84 0x46 0x01 0x7c 0x1e    ....F.|.
    0010   0x00 0x73 0x01 0x7c 0x1e 0x01 0x5c 0x5c    .s.|..\\
    0018   0x00 0x20 0x08 0x00 0x00 0x00 0x05 0x03    . ......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140  103  170    4    0    0
              5    0    3  132   70    1  124   30
              0  115    1  124   30    1   92   92
              0   32    8    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 70 CalBGForPH 2012-12-10T03:50:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 411}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2012-12-10T03:50:27)
    0000   0xdb 0x32 0x23 0x0a 0x8c                   .2#..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 71 BolusWizard 2012-12-10T03:50:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 411,
--
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2012-12-10T03:52:35)
    0000   0xe3 0x34 0x03 0x0a 0x0c                   .4...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3f 0x00 0x00    .Q.-j?..
    0008   0x00 0x05 0x00 0x3a 0x7d                   ...:}
    decimal
              0   81   13   45  106   63    0    0
              0    5    0   58  125
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-13.data: 78 records`
