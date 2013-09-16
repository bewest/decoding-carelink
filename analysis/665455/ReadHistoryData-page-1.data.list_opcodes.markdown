## START logs/ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 343, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x32 0x7d 0x01 0x32 0x32 0x00 0x91 0x26    2}.22..&
    0008   0x53 0x0d 0x0d 0x5b 0x00 0x8b 0x00 0x16    S..[....
    0010   0x0d 0x0d 0x1f 0x50 0x0d 0x2d 0x6a 0x00    ...P.-j.
    0018   0x17 0x00 0x00 0x00 0x00 0x17 0x7d 0x5c    ......}\
##### DEBUG DECIMAL
             50  125    1   50   50    0  145   38
             83   13   13   91    0  139    0   22
             13   13   31   80   13   45  106    0
             23    0    0    0    0   23  125   92
#### RECORD 0 hack1 2013-08-12T10:06:02 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x8b 0x0d 0x05 0x00 0x77 0x72 0x7c    m....wr|
    0008   0x03 0x00 0x00 0x04 0x48 0x03 0x84 0x52    ....H..R
    0010   0x00 0xc4 0x12 0x00 0x40 0x00 0xc4 0x12    ....@...
    0018   0x00 0xc4 0x64 0x00 0x00 0x00 0x00 0x00    ..d.....
    0020   0x00 0x01 0x01 0x00 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x21 0x00              ....!.
    decimal
            109  139   13    5    0  119  114  124
              3    0    0    4   72    3  132   82
              0  196   18    0   64    0  196   18
              0  196  100    0    0    0    0    0
              0    1    1    0    0    0   12    0
            232    0    0    0   33    0
    datetime (2013-08-12T10:06:02)
    0000   0x82 0x06 0x0a 0x0c 0x0d                   .....
    body (0)

#### RECORD 1 Prime 2013-08-12T10:09:04 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-08-12T10:09:04)
    0000   0x84 0x09 0x2a 0x0c 0x0d                   ..*..
    body (0)

#### RECORD 2 Prime 2013-08-12T10:09:34 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-08-12T10:09:34)
    0000   0xa2 0x09 0x0a 0x0c 0x0d                   .....
    body (0)

#### RECORD 3 CalBGForPH 2013-08-12T10:10:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2013-08-12T10:10:14)
    0000   0x8e 0x0a 0x2a 0x0c 0x8d                   ..*..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 BolusWizard 2013-08-12T10:10:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 301,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2d                                  [-
    decimal
             91   45
    datetime (2013-08-12T10:10:19)
    0000   0x93 0x0a 0x0a 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   39    0    0
              0    0    0   39  125

#### RECORD 5 Bolus 2013-08-12T10:10:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-08-12T10:10:19)
    0000   0x93 0x0a 0x4a 0x0c 0x0d                   ..J..
    body (0)

#### RECORD 6 CalBGForPH 2013-08-12T13:52:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-08-12T13:52:46)
    0000   0xae 0x34 0x2d 0x0c 0x0d                   .4-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 CalBGForPH 2013-08-12T13:53:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-08-12T13:53:02)
    0000   0x82 0x35 0x2d 0x0c 0x0d                   .5-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 CalBGForPH 2013-08-12T13:53:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-08-12T13:53:52)
    0000   0xb4 0x35 0x2d 0x0c 0x0d                   .5-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 BolusWizard 2013-08-12T13:54:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 84,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-08-12T13:54:07)
    0000   0x87 0x36 0x0d 0x0c 0x0d                   .6...
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0xfb 0x10 0xf0    .P.-j...
    0008   0x00 0x03 0x00 0x0b 0x7d                   ....}
    decimal
             21   80   13   45  106  251   16  240
              0    3    0   11  125
    HOUR BITS: [0, 0, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 230, 'amount': 3.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0xe6 0x04                   \....
    decimal
             92    5  156  230    4
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-08-12T13:54:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-08-12T13:54:07)
    0000   0x87 0x36 0x4d 0x0c 0x0d                   .6M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 12 PumpSuspend 2013-08-12T18:33:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-12T18:33:31)
    0000   0x9f 0x21 0x12 0x0c 0x0d                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 PumpResume 2013-08-12T18:33:43 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-12T18:33:43)
    0000   0xab 0x21 0x12 0x0c 0x0d                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-08-12T18:33:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-08-12T18:33:48)
    0000   0xb0 0x21 0x32 0x0c 0x0d                   .!2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 CalBGForPH 2013-08-12T18:33:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2013-08-12T18:33:55)
    0000   0xb7 0x21 0x32 0x0c 0x0d                   .!2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 16 CalBGForPH 2013-08-12T20:18:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-12T20:18:36)
    0000   0xa4 0x12 0x34 0x0c 0x0d                   ..4..
    body (0)

#### RECORD 17 BolusWizard 2013-08-12T20:18:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-12T20:18:50)
    0000   0xb2 0x12 0x14 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0xfe 0x1b 0xf0    $P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
             36   80   13   45  106  254   27  240
              0    0    0   25  125

#### RECORD 18 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 128, 'amount': 1.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0x80 0x14                   \.,..
    decimal
             92    5   44  128   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-08-12T20:18:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-08-12T20:18:50)
    0000   0xb2 0x12 0x54 0x0c 0x0d                   ..T..
    body (0)

#### RECORD 20 ResultTotals 2013-08-12T13:13:12 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xae                   .....
    decimal
              7    0    0    4  174
    datetime (2013-08-12T13:13:12)
    0000   0x8c 0x0d 0x6d 0x8c 0x0d                   ..m..
    body (51)
    hex
    0000   0x05 0x10 0x75 0x4e 0x2d 0x07 0x00 0x00    ..uN-...
    0008   0x04 0xae 0x03 0x82 0x4b 0x01 0x2c 0x19    ....K.,.
    0010   0x00 0x39 0x01 0x2c 0x19 0x00 0x90 0x30    .9.,...0
    0018   0x00 0x9c 0x34 0x00 0x00 0x00 0x03 0x02    ..4.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0xe4 0xbb 0x37 0x27 0x0d 0x0d    ....7'..
    0030   0x5b 0xe4 0x83                             [..
    decimal
              5   16  117   78   45    7    0    0
              4  174    3  130   75    1   44   25
              0   57    1   44   25    0  144   48
              0  156   52    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0   10  228  187   55   39   13   13
             91  228  131
    DAY BITS: [1, 0, 0]
#### RECORD 21 Base (2013, 0, 16, 0, 13, 13) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x07                                  8.
    decimal
             56    7
    datetime ((2013, 0, 16, 0, 13, 13))
    0000   0x0d 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 22 Base (2000, 0, 0, 0, 0, 22) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 22))
    0000   0x16 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 23 Base (2000, 4, 22, 22, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x16                                  ..
    decimal
              0   22
    datetime ((2000, 4, 22, 22, 1, 61))
    0000   0x7d 0x01 0x16 0x16 0x00                   }....
    body (0)

#### RECORD 24 Base (2009, 4, 10, 13, 13, 7) head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x38                                  .8
    decimal
            131   56
    datetime ((2009, 4, 10, 13, 13, 7))
    0000   0x47 0x0d 0x0d 0x0a 0x69                   G...i
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 25 Base (2009, 0, 27, 13, 13, 51) head[2], body[0] op[0x94]

    op hex (2)
    0000   0x94 0x25                                  .%
    decimal
            148   37
    datetime ((2009, 0, 27, 13, 13, 51))
    0000   0x33 0x0d 0x0d 0x5b 0x69                   3..[i
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 26 Base (2000, 0, 1, 13, 13, 19) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x26                                  .&
    decimal
            144   38
    datetime ((2000, 0, 1, 13, 13, 19))
    0000   0x13 0x0d 0x0d 0x41 0x50                   ...AP
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 27 Base (2000, 4, 0, 18, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 18, 0, 42))
    0000   0x6a 0x00 0x32 0x00 0x00                   j.2..
    body (0)

`end logs/ReadHistoryData-page-1.data: 28 records`
