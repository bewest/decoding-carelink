### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-11.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1a 0xd5                                  ..
##### DEBUG DECIMAL
             26  213
#### RECORD 0 BolusWizard 2012-12-13T18:36:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 133,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2012-12-13T18:36:46)
    0000   0xee 0x24 0x12 0x0d 0x0c                   .$...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x01 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    1    0    0
              0    0    0    1  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 2.0, 'curve': 20},
 {'age': 46, 'amount': 2.1, 'curve': 20},
--
    decimal
             92   11    4    2    4   72  212    4
             80  216   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2012-12-13T22:06:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-12-13T22:06:13)
    0000   0xcd 0x06 0x56 0x0d 0x0c                   ..V..
    body (0)

#### RECORD 17 ResultTotals 2012-12-13T13:12:13 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x12                   .....
    decimal
              7    0    0    5   18
    datetime (2012-12-13T13:12:13)
    0000   0xcd 0x0c 0x6d 0xcd 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8f 0x54 0xb7 0x05 0x00 0x00    ...T....
    0008   0x05 0x12 0x03 0x76 0x44 0x01 0x9c 0x20    ...vD.. 
    0010   0x00 0x86 0x01 0x9c 0x20 0x01 0x80 0x5d    .... ..]
    0018   0x00 0x1c 0x07 0x00 0x00 0x00 0x07 0x04    ........
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  143   84  183    5    0    0
              5   18    3  118   68    1  156   32
              0  134    1  156   32    1  128   93
              0   28    7    0    0    0    7    4
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 18 PumpSuspend 2012-12-14T14:22:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-14T14:22:15)
    0000   0xcf 0x16 0x0e 0x0e 0x0c                   .....
    body (0)

#### RECORD 19 PumpResume 2012-12-14T14:45:25 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-14T14:45:25)
--
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-12-14T19:18:56)
    0000   0xf8 0x12 0x53 0x0e 0x0c                   ..S..
    body (0)

#### RECORD 30 CalForBG 2012-12-14T19:30:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2012-12-14T19:30:23)
    0000   0xd7 0x1e 0x33 0x0e 0x0c                   ..3..
    body (0)

#### RECORD 31 ResultTotals 2012-12-14T13:12:14 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x56                   ....V
    decimal
              7    0    0    4   86
    datetime (2012-12-14T13:12:14)
    0000   0xce 0x0c 0x6d 0xce 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x62 0x6d 0x03 0x00 0x00    ..fbm...
    0008   0x04 0x56 0x03 0x76 0x50 0x00 0xe0 0x14    .V.vP...
    0010   0x00 0x4c 0x00 0xe0 0x14 0x00 0xe0 0x64    .L.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102   98  109    3    0    0
              4   86    3  118   80    0  224   20
              0   76    0  224   20    0  224  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 32 PumpSuspend 2012-12-15T19:07:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-15T19:07:29)
    0000   0xdd 0x07 0x13 0x0f 0x0c                   .....
    body (0)

#### RECORD 33 PumpResume 2012-12-15T19:39:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-15T19:39:16)
--
    0000   0x5c 0x08 0x1c 0x2b 0x04 0x5c 0x5d 0x04    \..+.\].
    decimal
             92    8   28   43    4   92   93    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2012-12-15T21:37:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'programmed': 0.8}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-12-15T21:37:07)
    0000   0xc7 0x25 0x55 0x0f 0x0c                   .%U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 ResultTotals 2012-12-15T13:12:15 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x08                   .....
    decimal
              7    0    0    4    8
    datetime (2012-12-15T13:12:15)
    0000   0xcf 0x0c 0x6d 0xcf 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7b 0x7b 0x7b 0x01 0x00 0x00    ..{{{...
    0008   0x04 0x08 0x03 0x70 0x55 0x00 0x98 0x0f    ...pU...
    0010   0x00 0x33 0x00 0x98 0x0f 0x00 0x98 0x64    .3.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  123  123  123    1    0    0
              4    8    3  112   85    0  152   15
              0   51    0  152   15    0  152  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 44 PumpSuspend 2012-12-16T09:47:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-16T09:47:21)
    0000   0xd5 0x2f 0x09 0x10 0x0c                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 PumpResume 2012-12-16T10:04:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-16T10:04:29)
--
             42   55    4   12   65    4   12   75
              4   10   85    4   90   95    4  128
             89   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2012-12-16T22:29:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-16T22:29:45)
    0000   0xed 0x1d 0x56 0x10 0x0c                   ..V..
    body (0)

#### RECORD 67 ResultTotals 2012-12-16T13:12:16 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x94                   .....
    decimal
              7    0    0    5  148
    datetime (2012-12-16T13:12:16)
    0000   0xd0 0x0c 0x6d 0xd0 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x9b 0x67 0x0e 0x04 0x00 0x00    ...g....
    0008   0x05 0x94 0x03 0x78 0x3e 0x02 0x1c 0x26    ...x>..&
    0010   0x00 0x83 0x02 0x1c 0x26 0x01 0x7e 0x47    ....&.~G
    0018   0x00 0x9e 0x1d 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  155  103   14    4    0    0
              5  148    3  120   62    2   28   38
              0  131    2   28   38    1  126   71
              0  158   29    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 68 Rewind 2012-12-17T09:08:30 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-17T09:08:30)
    0000   0xde 0x08 0x09 0x11 0x0c                   .....
    body (0)

#### RECORD 69 Prime 2012-12-17T09:10:40 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x22                   ...."
    decimal
              3    0    0    0   34
    datetime (2012-12-17T09:10:40)
--
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-17T12:48:58)
    0000   0xfa 0x30 0x0c 0x11 0x0c                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 76 CalForBG 2012-12-17T13:14:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2012-12-17T13:14:31)
    0000   0xdf 0x0e 0x2d 0x11 0x0c                   ..-..
    body (0)

`end logs/ReadHistoryData-page-11.data: 77 records`
