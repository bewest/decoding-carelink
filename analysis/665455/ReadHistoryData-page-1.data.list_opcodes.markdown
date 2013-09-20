## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 1003, found 19 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9e 0xf0                                  ..
##### DEBUG DECIMAL
            158  240
#### RECORD 0 Model522ResultTotals 2013-08-12T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-12T00:00:00)
    0000   0x8b 0x0d                                  ..
    body (41)
    hex
    0000   0x05 0x00 0x77 0x72 0x7c 0x03 0x00 0x00    ..wr|...
    0008   0x04 0x48 0x03 0x84 0x52 0x00 0xc4 0x12    .H..R...
    0010   0x00 0x40 0x00 0xc4 0x12 0x00 0xc4 0x64    .@.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  119  114  124    3    0    0
              4   72    3  132   82    0  196   18
              0   64    0  196   18    0  196  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0

#### RECORD 1 Rewind 2013-08-12T10:06:02 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-12T10:06:02)
    0000   0x82 0x06 0x0a 0x0c 0x0d                   .....
    body (0)

#### RECORD 2 Prime 2013-08-12T10:09:04 head[5], body[0] op[0x03]
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

#### RECORD 3 Prime 2013-08-12T10:09:34 head[5], body[0] op[0x03]
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

#### RECORD 4 CalBGForPH 2013-08-12T10:10:14 head[2], body[0] op[0x0a]
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
#### RECORD 5 BolusWizard 2013-08-12T10:10:19 head[2], body[13] op[0x5b]
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

#### RECORD 6 Bolus 2013-08-12T10:10:19 head[4], body[0] op[0x01]
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

#### RECORD 7 CalBGForPH 2013-08-12T13:52:46 head[2], body[0] op[0x0a]
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
#### RECORD 8 CalBGForPH 2013-08-12T13:53:02 head[2], body[0] op[0x0a]
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
#### RECORD 9 CalBGForPH 2013-08-12T13:53:52 head[2], body[0] op[0x0a]
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
#### RECORD 10 BolusWizard 2013-08-12T13:54:07 head[2], body[13] op[0x5b]
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
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 12 Bolus 2013-08-12T13:54:07 head[4], body[0] op[0x01]
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
#### RECORD 13 PumpSuspend 2013-08-12T18:33:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-12T18:33:31)
    0000   0x9f 0x21 0x12 0x0c 0x0d                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 PumpResume 2013-08-12T18:33:43 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-12T18:33:43)
    0000   0xab 0x21 0x12 0x0c 0x0d                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 CalBGForPH 2013-08-12T18:33:48 head[2], body[0] op[0x0a]
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
#### RECORD 16 CalBGForPH 2013-08-12T18:33:55 head[2], body[0] op[0x0a]
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
#### RECORD 17 CalBGForPH 2013-08-12T20:18:36 head[2], body[0] op[0x0a]
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

#### RECORD 18 BolusWizard 2013-08-12T20:18:50 head[2], body[13] op[0x5b]
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

#### RECORD 19 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 20 Bolus 2013-08-12T20:18:50 head[4], body[0] op[0x01]
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

#### RECORD 21 MResultTotals 2013-08-13T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xae                   .....
    decimal
              7    0    0    4  174
    datetime (2013-08-13T00:00:00)
    0000   0x8c 0x0d                                  ..
    body (0)

#### RECORD 22 Model522ResultTotals 2013-08-13T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-13T00:00:00)
    0000   0x8c 0x0d                                  ..
    body (41)
    hex
    0000   0x05 0x10 0x75 0x4e 0x2d 0x07 0x00 0x00    ..uN-...
    0008   0x04 0xae 0x03 0x82 0x4b 0x01 0x2c 0x19    ....K.,.
    0010   0x00 0x39 0x01 0x2c 0x19 0x00 0x90 0x30    .9.,...0
    0018   0x00 0x9c 0x34 0x00 0x00 0x00 0x03 0x02    ..4.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  117   78   45    7    0    0
              4  174    3  130   75    1   44   25
              0   57    1   44   25    0  144   48
              0  156   52    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0

#### RECORD 23 CalBGForPH 2013-08-13T07:55:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-08-13T07:55:59)
    0000   0xbb 0x37 0x27 0x0d 0x0d                   .7'..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 BolusWizard 2013-08-13T07:56:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-08-13T07:56:03)
    0000   0x83 0x38 0x07 0x0d 0x0d                   .8...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [0, 0, 1]
#### RECORD 25 Bolus 2013-08-13T07:56:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-08-13T07:56:03)
    0000   0x83 0x38 0x47 0x0d 0x0d                   .8G..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 CalBGForPH 2013-08-13T19:37:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-08-13T19:37:20)
    0000   0x94 0x25 0x33 0x0d 0x0d                   .%3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 27 BolusWizard 2013-08-13T19:38:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-08-13T19:38:16)
    0000   0x90 0x26 0x13 0x0d 0x0d                   .&...
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             65   80   13   45  106    0   50    0
              0    0    0   50  125
    HOUR BITS: [0, 0, 1]
#### RECORD 28 Bolus 2013-08-13T19:38:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-08-13T19:38:17)
    0000   0x91 0x26 0x53 0x0d 0x0d                   .&S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 BolusWizard 2013-08-13T22:00:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.3,
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
    datetime (2013-08-13T22:00:11)
    0000   0x8b 0x00 0x16 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125

#### RECORD 30 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 5.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x92 0x04                   \....
    decimal
             92    5  200  146    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-08-13T22:00:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-08-13T22:00:11)
    0000   0x8b 0x00 0x56 0x0d 0x0d                   ..V..
    body (0)

#### RECORD 32 MResultTotals 2013-08-14T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime (2013-08-14T00:00:00)
    0000   0x8d 0x0d                                  ..
    body (0)

#### RECORD 33 Model522ResultTotals 2013-08-14T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-14T00:00:00)
    0000   0x8d 0x0d                                  ..
    body (41)
    hex
    0000   0x05 0x00 0xa7 0x69 0xe4 0x02 0x00 0x00    ...i....
    0008   0x05 0x00 0x03 0x84 0x46 0x01 0x7c 0x1e    ....F.|.
    0010   0x00 0x60 0x01 0x7c 0x1e 0x01 0x24 0x4d    .`.|..$M
    0018   0x00 0x58 0x17 0x00 0x00 0x00 0x03 0x02    .X......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  167  105  228    2    0    0
              5    0    3  132   70    1  124   30
              0   96    1  124   30    1   36   77
              0   88   23    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0

#### RECORD 34 CalBGForPH 2013-08-14T08:28:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 361}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-08-14T08:28:54)
    0000   0xb6 0x1c 0x28 0x0e 0x8d                   ..(..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 BolusWizard 2013-08-14T08:28:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 52,
 '_byte[7]': 0,
 'bg': 361,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-08-14T08:28:56)
    0000   0xb8 0x1c 0x08 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x34 0x00 0x00    .Q.-j4..
    0008   0x00 0x00 0x00 0x34 0x7d                   ...4}
    decimal
              0   81   13   45  106   52    0    0
              0    0    0   52  125

#### RECORD 36 Bolus 2013-08-14T08:28:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2013-08-14T08:28:56)
    0000   0xb8 0x1c 0x48 0x0e 0x0d                   ..H..
    body (0)

#### RECORD 37 LowBattery 2013-08-14T11:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-08-14T11:01:00)
    0000   0x80 0x01 0x0b 0x0e 0x0d                   .....
    body (0)

#### RECORD 38 Battery 2013-08-14T11:09:38 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-08-14T11:09:38)
    0000   0xa6 0x09 0x0b 0x0e 0x0d                   .....
    body (0)

#### RECORD 39 Battery 2013-08-14T11:10:06 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-08-14T11:10:06)
    0000   0x86 0x0a 0x0b 0x0e 0x0d                   .....
    body (0)

#### RECORD 40 CalBGForPH 2013-08-14T11:10:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-08-14T11:10:47)
    0000   0xaf 0x0a 0x2b 0x0e 0x8d                   ..+..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 41 CalBGForPH 2013-08-14T11:14:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-08-14T11:14:50)
    0000   0xb2 0x0e 0x2b 0x0e 0x8d                   ..+..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 42 CalBGForPH 2013-08-14T11:16:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-08-14T11:16:33)
    0000   0xa1 0x10 0x2b 0x0e 0x8d                   ..+..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 BolusWizard 2013-08-14T11:17:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 269,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0d                                  [.
    decimal
             91   13
    datetime (2013-08-14T11:17:40)
    0000   0xa8 0x11 0x0b 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x21 0x51 0x0d 0x2d 0x6a 0x20 0x19 0x00    !Q.-j ..
    0008   0x00 0x0b 0x00 0x2e 0x7d                   ....}
    decimal
             33   81   13   45  106   32   25    0
              0   11    0   46  125

#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 5.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xd0 0xad 0x04                   \....
    decimal
             92    5  208  173    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-08-14T11:17:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-08-14T11:17:40)
    0000   0xa8 0x11 0x4b 0x0e 0x0d                   ..K..
    body (0)

#### RECORD 46 CalBGForPH 2013-08-14T19:08:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-08-14T19:08:59)
    0000   0xbb 0x08 0x33 0x0e 0x0d                   ..3..
    body (0)

#### RECORD 47 BolusWizard 2013-08-14T19:09:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-08-14T19:09:25)
    0000   0x99 0x09 0x13 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    BP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             66   80   13   45  106    0   50    0
              0    0    0   50  125

#### RECORD 48 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 219, 'amount': 3.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0xdb 0x14                   \....
    decimal
             92    5  128  219   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-08-14T19:09:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-08-14T19:09:25)
    0000   0x99 0x09 0x53 0x0e 0x0d                   ..S..
    body (0)

#### RECORD 50 MResultTotals 2013-08-15T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9c                   .....
    decimal
              7    0    0    5  156
    datetime (2013-08-15T00:00:00)
    0000   0x8e 0x0d                                  ..
    body (0)

#### RECORD 51 Model522ResultTotals 2013-08-15T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-15T00:00:00)
    0000   0x8e 0x0d                                  ..
    body (41)
    hex
    0000   0x05 0x11 0x03 0x7d 0x69 0x05 0x00 0x00    ...}i...
    0008   0x05 0x9c 0x03 0x84 0x3f 0x02 0x18 0x25    ....?..%
    0010   0x00 0x63 0x02 0x18 0x25 0x01 0x2c 0x38    .c..%.,8
    0018   0x00 0xec 0x2c 0x00 0x00 0x00 0x03 0x01    ..,.....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17    3  125  105    5    0    0
              5  156    3  132   63    2   24   37
              0   99    2   24   37    1   44   56
              0  236   44    0    0    0    3    1
              1    1    0   12    0  232    0    0
              0

#### RECORD 52 CalBGForPH 2013-08-15T01:07:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 267}
```
    op hex (2)
    0000   0x0a 0x0b                                  ..
    decimal
             10   11
    datetime (2013-08-15T01:07:32)
    0000   0xa0 0x07 0x21 0x0f 0x8d                   ..!..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 53 BolusWizard 2013-08-15T01:07:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 267,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0b                                  [.
    decimal
             91   11
    datetime (2013-08-15T01:07:49)
    0000   0xb1 0x07 0x01 0x0f 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125

#### RECORD 54 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 107, 'amount': 5.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x6b 0x14                   \..k.
    decimal
             92    5  200  107   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-08-15T01:07:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-08-15T01:07:50)
    0000   0xb2 0x07 0x41 0x0f 0x0d                   ..A..
    body (0)

#### RECORD 56 LowReservoir 2013-08-15T09:12:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-15T09:12:37)
    0000   0xa5 0x0c 0x09 0x0f 0x0d                   .....
    body (0)

#### RECORD 57 PumpSuspend 2013-08-15T14:15:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-15T14:15:53)
    0000   0xb5 0x0f 0x0e 0x0f 0x0d                   .....
    body (0)

#### RECORD 58 PumpResume 2013-08-15T14:27:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-15T14:27:07)
    0000   0x87 0x1b 0x0e 0x0f 0x0d                   .....
    body (0)

#### RECORD 59 CalBGForPH 2013-08-15T14:37:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-08-15T14:37:58)
    0000   0xba 0x25 0x2e 0x0f 0x0d                   .%...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 BolusWizard 2013-08-15T14:38:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 206,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2013-08-15T14:38:05)
    0000   0x85 0x26 0x0e 0x0f 0x0d                   .&...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    0    0   18  125
    HOUR BITS: [0, 0, 1]
#### RECORD 61 Bolus 2013-08-15T14:38:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-08-15T14:38:05)
    0000   0x85 0x26 0x4e 0x0f 0x0d                   .&N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 62 LowReservoir 2013-08-15T17:53:41 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-15T17:53:41)
    0000   0xa9 0x35 0x11 0x0f 0x0d                   .5...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 CalBGForPH 2013-08-15T20:32:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-08-15T20:32:29)
    0000   0x9d 0x20 0x34 0x0f 0x0d                   . 4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 BolusWizard 2013-08-15T20:33:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-08-15T20:33:16)
    0000   0x90 0x21 0x14 0x0f 0x0d                   .!...
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x00 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             62   80   13   45  106    0   47    0
              0    0    0   47  125
    HOUR BITS: [0, 0, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 1.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x67 0x14                   \.0g.
    decimal
             92    5   48  103   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-08-15T20:33:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-08-15T20:33:16)
    0000   0x90 0x21 0x54 0x0f 0x0d                   .!T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 67 MResultTotals 2013-08-16T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xce                   .....
    decimal
              7    0    0    4  206
    datetime (2013-08-16T00:00:00)
    0000   0x8f 0x0d                                  ..
    body (0)

#### RECORD 68 Model522ResultTotals 2013-08-16T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-16T00:00:00)
    0000   0x8f 0x0d                                  ..
    body (41)
    hex
    0000   0x05 0x10 0xc4 0x72 0x0b 0x03 0x00 0x00    ...r....
    0008   0x04 0xce 0x03 0x7e 0x49 0x01 0x50 0x1b    ...~I.P.
    0010   0x00 0x3e 0x01 0x50 0x1b 0x00 0xbc 0x38    .>.P...8
    0018   0x00 0x94 0x2c 0x00 0x00 0x00 0x03 0x01    ..,.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  196  114   11    3    0    0
              4  206    3  126   73    1   80   27
              0   62    1   80   27    0  188   56
              0  148   44    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0

#### RECORD 69 PumpSuspend 2013-08-16T11:07:58 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-16T11:07:58)
    0000   0xba 0x07 0x0b 0x10 0x0d                   .....
    body (0)

#### RECORD 70 PumpResume 2013-08-16T11:30:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-16T11:30:50)
    0000   0xb2 0x1e 0x0b 0x10 0x0d                   .....
    body (0)

#### RECORD 71 Rewind 2013-08-16T11:30:55 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-16T11:30:55)
    0000   0xb7 0x1e 0x0b 0x10 0x0d                   .....
    body (0)

#### RECORD 72 Prime 2013-08-16T11:32:39 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1d                   .....
    decimal
              3    0    0    0   29
    datetime (2013-08-16T11:32:39)
    0000   0xa7 0x20 0x2b 0x10 0x0d                   . +..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 73 Prime 2013-08-16T11:33:07 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-08-16T11:33:07)
    0000   0x87 0x21 0x0b 0x10 0x0d                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 74 CalBGForPH 2013-08-16T13:09:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-08-16T13:09:00)
    0000   0x80 0x09 0x2d 0x10 0x0d                   ..-..
    body (0)

#### RECORD 75 BolusWizard 2013-08-16T13:09:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 142,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-08-16T13:09:12)
    0000   0x8c 0x09 0x0d 0x10 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x03 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106    3    0    0
              0    0    0    3  125

#### RECORD 76 Bolus 2013-08-16T13:09:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-08-16T13:09:12)
    0000   0x8c 0x09 0x4d 0x10 0x0d                   ..M..
    body (0)

#### RECORD 77 CalBGForPH 2013-08-16T13:24:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-08-16T13:24:14)
    0000   0x8e 0x18 0x2d 0x10 0x0d                   ..-..
    body (0)

#### RECORD 78 BolusWizard 2013-08-16T13:24:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 123,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-08-16T13:24:49)
    0000   0xb1 0x18 0x0d 0x10 0x0d                   .....
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x03 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0    3    0   31  125

#### RECORD 79 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 0.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x0c 0x14 0x04                   \....
    decimal
             92    5   12   20    4
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2013-08-16T13:24:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-08-16T13:24:49)
    0000   0xb1 0x18 0x4d 0x10 0x0d                   ..M..
    body (0)

#### RECORD 81 CalBGForPH 2013-08-16T21:39:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-08-16T21:39:16)
    0000   0x90 0x27 0x35 0x10 0x0d                   .'5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 82 BolusWizard 2013-08-16T21:39:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2013-08-16T21:39:38)
    0000   0xa6 0x27 0x15 0x10 0x0d                   .'...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfd 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             55   80   13   45  106  253   42  240
              0    0    0   39  125
    HOUR BITS: [0, 0, 1]
#### RECORD 83 Bolus 2013-08-16T21:39:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-08-16T21:39:39)
    0000   0xa7 0x27 0x55 0x10 0x0d                   .'U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 84 MResultTotals 2013-08-17T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x94                   .....
    decimal
              7    0    0    4  148
    datetime (2013-08-17T00:00:00)
    0000   0x90 0x0d                                  ..
    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-1.data: 85 records`
