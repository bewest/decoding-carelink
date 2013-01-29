### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-24.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x76 0x5d                                  v]
##### DEBUG DECIMAL
            118   93
#### RECORD 0 CalBGForPH 2012-10-26T17:30:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2012-10-26T17:30:40)
    0000   0xa8 0x9e 0x31 0x1a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2012-10-26T22:08:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2012-10-26T22:08:57)
    0000   0xb9 0x88 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 2 BolusWizard 2012-10-26T22:09:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 111,
 'bg_target_high': 125,
 'bg_target_low': 106,
--
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2012-10-26T22:43:59)
    0000   0xbb 0xab 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 CalBGForPH 2012-10-26T22:53:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-10-26T22:53:00)
    0000   0x80 0xb5 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 7 ResultTotals 2012-08-26T13:12:58 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbc                   .....
    decimal
              7    0    0    4  188
    datetime (2012-08-26T13:12:58)
    0000   0xba 0x0c 0x6d 0xba 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x8b 0x46 0x47 0x09 0x00 0x00    ...FG...
    0008   0x04 0xbc 0x02 0xb4 0x39 0x02 0x08 0x2b    ....9..+
    0010   0x00 0x56 0x02 0x08 0x2b 0x00 0xfc 0x30    .V..+..0
    0018   0x01 0x0c 0x34 0x00 0x00 0x00 0x04 0x02    ..4.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  139   70   71    9    0    0
              4  188    2  180   57    2    8   43
              0   86    2    8   43    0  252   48
              1   12   52    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 8 CalBGForPH 2012-10-27T00:20:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2012-10-27T00:20:03)
    0000   0x83 0x94 0x20 0x1b 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 9 CalBGForPH 2012-10-27T00:20:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
--
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2012-10-27T19:53:10)
    0000   0x8a 0xb5 0x33 0x1b 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 LowReservoir 2012-10-27T21:25:15 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-27T21:25:15)
    0000   0x8f 0x99 0x15 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 ResultTotals 2012-08-27T13:12:59 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9a                   .....
    decimal
              7    0    0    5  154
    datetime (2012-08-27T13:12:59)
    0000   0xbb 0x0c 0x6d 0xbb 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x64 0xe5 0x07 0x00 0x00    ...d....
    0008   0x05 0x9a 0x03 0x66 0x3d 0x02 0x34 0x27    ...f=.4'
    0010   0x00 0x96 0x02 0x34 0x27 0x01 0xc8 0x51    ...4'..Q
    0018   0x00 0x6c 0x13 0x00 0x00 0x00 0x04 0x02    .l......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140  100  229    7    0    0
              5  154    3  102   61    2   52   39
              0  150    2   52   39    1  200   81
              0  108   19    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 32 CalBGForPH 2012-10-28T01:32:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2012-10-28T01:32:35)
    0000   0xa3 0xa0 0x21 0x1c 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 PumpSuspend 2012-10-28T08:46:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
--
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2012-10-28T20:04:03)
    0000   0x83 0x84 0x34 0x1c 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 CalBGForPH 2012-10-28T22:01:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2012-10-28T22:01:42)
    0000   0xaa 0x81 0x36 0x1c 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 ResultTotals (2012, 8, 28, 13, 12, 60) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x2a                   ....*
    decimal
              7    0    0    5   42
    datetime ((2012, 8, 28, 13, 12, 60))
    0000   0xbc 0x0c 0x6d 0xbc 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x91 0x3e 0xd7 0x09 0x00 0x00    ...>....
    0008   0x05 0x2a 0x03 0x6a 0x42 0x01 0xc0 0x22    .*.jB.."
    0010   0x00 0x6d 0x01 0xc0 0x22 0x01 0x44 0x48    .m..".DH
    0018   0x00 0x7c 0x1c 0x00 0x00 0x00 0x05 0x03    .|......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  145   62  215    9    0    0
              5   42    3  106   66    1  192   34
              0  109    1  192   34    1   68   72
              0  124   28    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 64 CalBGForPH 2012-10-29T02:55:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2012-10-29T02:55:13)
    0000   0x8d 0xb7 0x22 0x1d 0x0c                   .."..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 BolusWizard 2012-10-29T02:55:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 175,
--
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2012-10-29T18:59:38)
    0000   0xa6 0xbb 0x12 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x0a 0x26 0x00    2P.-j.&.
    0008   0x00 0x03 0x00 0x2d 0x7d                   ...-}
    decimal
             50   80   13   45  106   10   38    0
              0    3    0   45  125
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-24.data: 90 records`
