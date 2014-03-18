## START logs/ReadHistoryData-page-31.data
ERROR day is out of range for month (2013, 3, 32, 0, 0, 0) 0000   0x3f 0x8d                                  ?.
ERROR day is out of range for month 0000   0x3f 0x8d                                  ?.
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x30 0x2d                                  0-
##### DEBUG DECIMAL
             48   45
#### RECORD 0 BolusWizard 2013-03-30T22:31:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-03-30T22:31:44)
    0000   0x2c 0xdf 0x16 0x1e 0x0d                   ,....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x0f 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             42   80   13   45  106   15   32    0
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 1 LowReservoir 2013-03-30T22:32:41 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-30T22:32:41)
    0000   0x29 0xe0 0x16 0x1e 0x0d                   )....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 Bolus 2013-03-30T22:31:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-03-30T22:31:44)
    0000   0x2c 0xdf 0x56 0x1e 0x0d                   ,.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-30T23:59:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-03-30T23:59:41)
    0000   0x29 0xfb 0x37 0x1e 0x0d                   ).7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 MResultTotals 2013-03-31T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x32                   ....2
    decimal
              7    0    0    4   50
    datetime (2013-03-31T00:00:00)
    0000   0x3e 0x8d                                  >.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 Model522ResultTotals 2013-03-31T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-31T00:00:00)
    0000   0x3e 0x8d                                  >.
    body (41)
    hex
    0000   0x05 0x00 0x97 0x6d 0xc1 0x02 0x00 0x00    ...m....
    0008   0x04 0x32 0x03 0x76 0x52 0x00 0xbc 0x12    .2.vR...
    0010   0x00 0x2a 0x00 0xbc 0x12 0x00 0x80 0x44    .*.....D
    0018   0x00 0x3c 0x20 0x00 0x00 0x00 0x01 0x00    .< .....
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  151  109  193    2    0    0
              4   50    3  118   82    0  188   18
              0   42    0  188   18    0  128   68
              0   60   32    0    0    0    1    0
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 6 LowReservoir 2013-03-31T06:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-03-31T06:41:03)
    0000   0x03 0xe9 0x06 0x1f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 CalBGForPH 2013-03-31T07:50:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 262}
```
    op hex (2)
    0000   0x0a 0x06                                  ..
    decimal
             10    6
    datetime (2013-03-31T07:50:55)
    0000   0x37 0xf2 0x27 0x1f 0x8d                   7.'..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2013-03-31T07:51:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 262,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x06                                  [.
    decimal
             91    6
    datetime (2013-03-31T07:51:04)
    0000   0x04 0xf3 0x07 0x1f 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
              0   81   13   45  106   30    0    0
              0    0    0   30  125
    HOUR BITS: [1, 1, 1]
#### RECORD 9 Bolus 2013-03-31T07:51:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-03-31T07:51:05)
    0000   0x05 0xf3 0x47 0x1f 0x0d                   ..G..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 PumpSuspend 2013-03-31T08:39:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-31T08:39:57)
    0000   0x39 0xe7 0x08 0x1f 0x0d                   9....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 PumpResume 2013-03-31T09:01:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-31T09:01:20)
    0000   0x14 0xc1 0x09 0x1f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-03-31T10:28:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-03-31T10:28:13)
    0000   0x0d 0xdc 0x2a 0x1f 0x0d                   ..*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BolusWizard 2013-03-31T10:28:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 172,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2013-03-31T10:28:24)
    0000   0x18 0xdc 0x0a 0x1f 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    7    0    3  125
    HOUR BITS: [1, 1, 0]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 164, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0xa4 0x04                   \.x..
    decimal
             92    5  120  164    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-03-31T10:28:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x01 0x01 0x00                        ....
    decimal
              1    1    1    0
    datetime (2013-03-31T10:28:24)
    0000   0x18 0xdc 0x4a 0x1f 0x0d                   ..J..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 CalBGForPH 2013-03-31T12:35:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2013-03-31T12:35:13)
    0000   0x0d 0xe3 0x2c 0x1f 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 CalBGForPH 2013-03-31T12:36:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-03-31T12:36:27)
    0000   0x1b 0xe4 0x2c 0x1f 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 CalBGForPH 2013-03-31T12:38:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-03-31T12:38:44)
    0000   0x2c 0xe6 0x2c 0x1f 0x0d                   ,.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 BolusWizard 2013-03-31T12:39:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 86,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2013-03-31T12:39:18)
    0000   0x12 0xe7 0x0c 0x1f 0x0d                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xfb 0x26 0xf0    2P.-j.&.
    0008   0x00 0x01 0x00 0x21 0x7d                   ...!}
    decimal
             50   80   13   45  106  251   38  240
              0    1    0   33  125
    HOUR BITS: [1, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 135, 'amount': 0.1, 'curve': 4},
 {'age': 39, 'amount': 3.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x04 0x87 0x04 0x78 0x27 0x14    \....x'.
    decimal
             92    8    4  135    4  120   39   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-03-31T12:39:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-03-31T12:39:18)
    0000   0x12 0xe7 0x4c 0x1f 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 Rewind 2013-03-31T22:07:38 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-31T22:07:38)
    0000   0x26 0xc7 0x16 0x1f 0x0d                   &....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 Prime 2013-03-31T22:09:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x21                   ....!
    decimal
              3    0    0    0   33
    datetime (2013-03-31T22:09:44)
    0000   0x2c 0xc9 0x36 0x1f 0x0d                   ,.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 Prime 2013-03-31T22:12:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-31T22:12:30)
    0000   0x1e 0xcc 0x16 0x1f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 CalBGForPH 2013-03-31T22:12:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-03-31T22:12:57)
    0000   0x39 0xcc 0x36 0x1f 0x0d                   9.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 BolusWizard 2013-03-31T22:13:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-03-31T22:13:26)
    0000   0x1a 0xcd 0x16 0x1f 0x0d                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0xff 0x2c 0xf0    :P.-j.,.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             58   80   13   45  106  255   44  240
              0    0    0   43  125
    HOUR BITS: [1, 1, 0]
#### RECORD 27 Bolus 2013-03-31T22:13:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-03-31T22:13:27)
    0000   0x1b 0xcd 0x56 0x1f 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
ERROR day is out of range for month (2013, 3, 32, 0, 0, 0) 0000   0x3f 0x8d                                  ?.
#### RECORD 28 MResultTotals (2013, 3, 32, 0, 0, 0) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1e                   .....
    decimal
              7    0    0    5   30
    datetime ((2013, 3, 32, 0, 0, 0))
    0000   0x3f 0x8d                                  ?.
    body (0)
    HOUR BITS: [1, 0, 0]
ERROR day is out of range for month 0000   0x3f 0x8d                                  ?.
#### RECORD 29 Model522ResultTotals (2013, 3, 32, 0, 0, 0) head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime ((2013, 3, 32, 0, 0, 0))
    0000   0x3f 0x8d                                  ?.
    body (41)
    hex
    0000   0x05 0x10 0x82 0x4d 0x06 0x06 0x00 0x00    ...M....
    0008   0x05 0x1e 0x03 0x72 0x43 0x01 0xac 0x21    ...rC..!
    0010   0x00 0x6c 0x01 0xac 0x21 0x01 0x30 0x47    .l..!.0G
    0018   0x00 0x7c 0x1d 0x00 0x00 0x00 0x04 0x02    .|......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  130   77    6    6    0    0
              5   30    3  114   67    1  172   33
              0  108    1  172   33    1   48   71
              0  124   29    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 30 PumpSuspend 2013-04-01T11:48:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-01T11:48:29)
    0000   0x5d 0x30 0x0b 0x01 0x0d                   ]0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 PumpResume 2013-04-01T13:15:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-01T13:15:07)
    0000   0x47 0x0f 0x0d 0x01 0x0d                   G....
    body (0)

#### RECORD 32 CalBGForPH 2013-04-01T13:54:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-04-01T13:54:08)
    0000   0x48 0x36 0x2d 0x01 0x0d                   H6-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 BolusWizard 2013-04-01T13:54:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2013-04-01T13:54:37)
    0000   0x65 0x36 0x0d 0x01 0x0d                   e6...
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0xfd 0x2f 0xf0    >P.-j./.
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
             62   80   13   45  106  253   47  240
              0    0    0   44  125
    HOUR BITS: [0, 0, 1]
#### RECORD 34 Bolus 2013-04-01T13:54:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-04-01T13:54:37)
    0000   0x65 0x36 0x4d 0x01 0x0d                   e6M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 BolusWizard 2013-04-01T14:09:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
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
    datetime (2013-04-01T14:09:34)
    0000   0x62 0x09 0x0e 0x01 0x0d                   b....
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125

#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 4.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb0 0x0f 0x04                   \....
    decimal
             92    5  176   15    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-04-01T14:09:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-04-01T14:09:34)
    0000   0x62 0x09 0x4e 0x01 0x0d                   b.N..
    body (0)

#### RECORD 38 CalBGForPH 2013-04-01T14:21:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-04-01T14:21:08)
    0000   0x48 0x15 0x2e 0x01 0x0d                   H....
    body (0)

#### RECORD 39 BolusWizard 2013-04-01T14:21:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.5,
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
    datetime (2013-04-01T14:21:23)
    0000   0x57 0x15 0x0e 0x01 0x0d                   W....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0    0    0    5  125

#### RECORD 40 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 0.8, 'curve': 4},
 {'age': 27, 'amount': 4.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x11 0x04 0xb0 0x1b 0x04    \. .....
    decimal
             92    8   32   17    4  176   27    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-04-01T14:21:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-01T14:21:23)
    0000   0x57 0x15 0x4e 0x01 0x0d                   W.N..
    body (0)

#### RECORD 42 CalBGForPH 2013-04-01T15:10:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-04-01T15:10:56)
    0000   0x78 0x0a 0x2f 0x01 0x0d                   x./..
    body (0)

#### RECORD 43 CalBGForPH 2013-04-01T18:30:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-04-01T18:30:00)
    0000   0x40 0x1e 0x32 0x01 0x0d                   @.2..
    body (0)

#### RECORD 44 BolusWizard 2013-04-01T18:30:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 189,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2013-04-01T18:30:09)
    0000   0x49 0x1e 0x12 0x01 0x0d                   I....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125

#### RECORD 45 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 0.5, 'curve': 20},
 {'age': 10, 'amount': 0.8, 'curve': 20},
 {'age': 20, 'amount': 4.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x00 0x14 0x20 0x0a 0x14    \.... ..
    0008   0xb0 0x14 0x14                             ...
    decimal
             92   11   20    0   20   32   10   20
            176   20   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-04-01T18:30:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-04-01T18:30:09)
    0000   0x49 0x1e 0x52 0x01 0x0d                   I.R..
    body (0)

#### RECORD 47 CalBGForPH 2013-04-01T21:32:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 150}
```
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-04-01T21:32:55)
    0000   0x77 0x20 0x35 0x01 0x0d                   w 5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 BolusWizard 2013-04-01T21:33:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 150,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x96                                  [.
    decimal
             91  150
    datetime (2013-04-01T21:33:03)
    0000   0x43 0x21 0x15 0x01 0x0d                   C!...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x05 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106    5    0    0
              0    2    0    3  125
    HOUR BITS: [0, 0, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 1.4, 'curve': 4},
 {'age': 183, 'amount': 0.5, 'curve': 20},
 {'age': 193, 'amount': 0.8, 'curve': 20},
 {'age': 203, 'amount': 4.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0xbd 0x04 0x14 0xb7 0x14    \.8.....
    0008   0x20 0xc1 0x14 0xb0 0xcb 0x14               .....
    decimal
             92   14   56  189    4   20  183   20
             32  193   20  176  203   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-04-01T21:33:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-04-01T21:33:03)
    0000   0x43 0x21 0x55 0x01 0x0d                   C!U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 51 CalBGForPH 2013-04-01T21:49:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2013-04-01T21:49:18)
    0000   0x52 0x31 0x35 0x01 0x0d                   R15..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 BolusWizard 2013-04-01T21:50:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 140,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8c                                  [.
    decimal
             91  140
    datetime (2013-04-01T21:50:41)
    0000   0x69 0x32 0x15 0x01 0x0d                   i2...
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x03 0x2b 0x00    9P.-j.+.
    0008   0x00 0x05 0x00 0x2b 0x7d                   ...+}
    decimal
             57   80   13   45  106    3   43    0
              0    5    0   43  125
    HOUR BITS: [0, 0, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 0.3, 'curve': 4},
 {'age': 206, 'amount': 1.4, 'curve': 4},
 {'age': 200, 'amount': 0.5, 'curve': 20},
 {'age': 210, 'amount': 0.8, 'curve': 20},
 {'age': 220, 'amount': 4.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x0c 0x1a 0x04 0x38 0xce 0x04    \....8..
    0008   0x14 0xc8 0x14 0x20 0xd2 0x14 0xb0 0xdc    ... ....
    0010   0x14                                       .
    decimal
             92   17   12   26    4   56  206    4
             20  200   20   32  210   20  176  220
             20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-04-01T21:50:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-04-01T21:50:41)
    0000   0x69 0x32 0x55 0x01 0x0d                   i2U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 MResultTotals 2013-04-02T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x18                   .....
    decimal
              7    0    0    5   24
    datetime (2013-04-02T00:00:00)
    0000   0x41 0x0d                                  A.
    body (0)

#### RECORD 56 Model522ResultTotals 2013-04-02T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-02T00:00:00)
    0000   0x41 0x0d                                  A.
    body (41)
    hex
    0000   0x05 0x00 0x85 0x5e 0xbd 0x06 0x00 0x00    ...^....
    0008   0x05 0x18 0x03 0x44 0x40 0x01 0xd4 0x24    ...D@..$
    0010   0x00 0x89 0x01 0xd4 0x24 0x01 0x90 0x55    ....$..U
    0018   0x00 0x44 0x0f 0x00 0x00 0x00 0x06 0x04    .D......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  133   94  189    6    0    0
              5   24    3   68   64    1  212   36
              0  137    1  212   36    1  144   85
              0   68   15    0    0    0    6    4
              2    0    0   12    0  232    0    0
              0

#### RECORD 57 CalBGForPH 2013-04-02T00:25:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-04-02T00:25:43)
    0000   0x6b 0x19 0x20 0x02 0x0d                   k. ..
    body (0)

#### RECORD 58 PumpSuspend 2013-04-02T10:09:36 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-02T10:09:36)
    0000   0x64 0x09 0x0a 0x02 0x0d                   d....
    body (0)

#### RECORD 59 PumpResume 2013-04-02T13:45:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-02T13:45:02)
    0000   0x42 0x2d 0x0d 0x02 0x0d                   B-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 CalBGForPH 2013-04-02T13:45:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 291}
```
    op hex (2)
    0000   0x0a 0x23                                  .#
    decimal
             10   35
    datetime (2013-04-02T13:45:17)
    0000   0x51 0x2d 0x2d 0x02 0x8d                   Q--..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 BolusWizard 2013-04-02T13:45:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 291,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
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
    0000   0x5b 0x23                                  [#
    decimal
             91   35
    datetime (2013-04-02T13:45:20)
    0000   0x54 0x2d 0x0d 0x02 0x0d                   T-...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [0, 0, 1]
#### RECORD 62 Bolus 2013-04-02T13:45:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-04-02T13:45:20)
    0000   0x54 0x2d 0x4d 0x02 0x0d                   T-M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 PumpSuspend 2013-04-02T13:48:26 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-02T13:48:26)
    0000   0x5a 0x30 0x0d 0x02 0x0d                   Z0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 PumpResume 2013-04-02T14:08:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-02T14:08:50)
    0000   0x72 0x08 0x0e 0x02 0x0d                   r....
    body (0)

#### RECORD 65 CalBGForPH 2013-04-02T14:43:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 273}
```
    op hex (2)
    0000   0x0a 0x11                                  ..
    decimal
             10   17
    datetime (2013-04-02T14:43:43)
    0000   0x6b 0x2b 0x2e 0x02 0x8d                   k+...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 66 BolusWizard 2013-04-02T14:43:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 273,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x11                                  [.
    decimal
             91   17
    datetime (2013-04-02T14:43:55)
    0000   0x77 0x2b 0x0e 0x02 0x0d                   w+...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x1e 0x00 0x02 0x7d                   ....}
    decimal
              0   81   13   45  106   32    0    0
              0   30    0    2  125
    HOUR BITS: [0, 0, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 3.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x3b 0x04                   \..;.
    decimal
             92    5  144   59    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-04-02T14:43:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-04-02T14:43:55)
    0000   0x77 0x2b 0x4e 0x02 0x0d                   w+N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 CalBGForPH 2013-04-02T14:53:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 263}
```
    op hex (2)
    0000   0x0a 0x07                                  ..
    decimal
             10    7
    datetime (2013-04-02T14:53:39)
    0000   0x67 0x35 0x2e 0x02 0x8d                   g5...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 BolusWizard 2013-04-02T14:54:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 263,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x07                                  [.
    decimal
             91    7
    datetime (2013-04-02T14:54:41)
    0000   0x69 0x36 0x0e 0x02 0x0d                   i6...
    body (13)
    hex
    0000   0x2a 0x51 0x0d 0x2d 0x6a 0x1e 0x20 0x00    *Q.-j. .
    0008   0x00 0x1f 0x00 0x20 0x7d                   ... }
    decimal
             42   81   13   45  106   30   32    0
              0   31    0   32  125
    HOUR BITS: [0, 0, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 0.15, 'curve': 4},
 {'age': 20, 'amount': 0.15, 'curve': 4},
 {'age': 70, 'amount': 3.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x06 0x0a 0x04 0x06 0x14 0x04    \.......
    0008   0x90 0x46 0x04                             .F.
    decimal
             92   11    6   10    4    6   20    4
            144   70    4
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-04-02T14:54:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-04-02T14:54:41)
    0000   0x69 0x36 0x4e 0x02 0x0d                   i6N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 73 BolusWizard 2013-04-02T15:04:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
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
    datetime (2013-04-02T15:04:04)
    0000   0x44 0x04 0x0f 0x02 0x0d                   D....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125

#### RECORD 74 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 3.2, 'curve': 4},
 {'age': 20, 'amount': 0.15, 'curve': 4},
 {'age': 30, 'amount': 0.15, 'curve': 4},
 {'age': 80, 'amount': 3.6, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x80 0x0a 0x04 0x06 0x14 0x04    \.......
    0008   0x06 0x1e 0x04 0x90 0x50 0x04              ....P.
    decimal
             92   14  128   10    4    6   20    4
              6   30    4  144   80    4
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-04-02T15:04:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-04-02T15:04:04)
    0000   0x44 0x04 0x4f 0x02 0x0d                   D.O..
    body (0)

#### RECORD 76 CalBGForPH 2013-04-02T15:54:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 257}
```
    op hex (2)
    0000   0x0a 0x01                                  ..
    decimal
             10    1
    datetime (2013-04-02T15:54:27)
    0000   0x5b 0x36 0x2f 0x02 0x8d                   [6/..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 77 BolusWizard 2013-04-02T15:54:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 257,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 1.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 5.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x01                                  [.
    decimal
             91    1
    datetime (2013-04-02T15:54:42)
    0000   0x6a 0x36 0x0f 0x02 0x0d                   j6...
    body (13)
    hex
    0000   0x0d 0x51 0x0d 0x2d 0x6a 0x1d 0x0a 0x00    .Q.-j...
    0008   0x00 0x34 0x00 0x0a 0x7d                   .4..}
    decimal
             13   81   13   45  106   29   10    0
              0   52    0   10  125
    HOUR BITS: [0, 0, 1]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 1.0, 'curve': 4},
 {'age': 60, 'amount': 3.2, 'curve': 4},
 {'age': 70, 'amount': 0.15, 'curve': 4},
 {'age': 80, 'amount': 0.15, 'curve': 4},
 {'age': 130, 'amount': 3.6, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x32 0x04 0x80 0x3c 0x04    \.(2..<.
    0008   0x06 0x46 0x04 0x06 0x50 0x04 0x90 0x82    .F..P...
    0010   0x04                                       .
    decimal
             92   17   40   50    4  128   60    4
              6   70    4    6   80    4  144  130
              4
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-04-02T15:54:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-04-02T15:54:43)
    0000   0x6b 0x36 0x4f 0x02 0x0d                   k6O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 80 BolusWizard 2013-04-02T17:13:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 19,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.4,
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
    datetime (2013-04-02T17:13:53)
    0000   0x75 0x0d 0x11 0x02 0x0d                   u....
    body (13)
    hex
    0000   0x13 0x50 0x0d 0x2d 0x6a 0x00 0x0e 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
             19   80   13   45  106    0   14    0
              0    0    0   14  125

#### RECORD 81 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.0, 'curve': 4},
 {'age': 129, 'amount': 1.0, 'curve': 4},
 {'age': 139, 'amount': 3.2, 'curve': 4},
 {'age': 149, 'amount': 0.15, 'curve': 4},
 {'age': 159, 'amount': 0.15, 'curve': 4},
 {'age': 209, 'amount': 3.6, 'curve': 4}]
```
    op hex (20)
    0000   0x5c 0x14 0x28 0x4f 0x04 0x28 0x81 0x04    \.(O.(..
    0008   0x80 0x8b 0x04 0x06 0x95 0x04 0x06 0x9f    ........
    0010   0x04 0x90 0xd1 0x04                        ....
    decimal
             92   20   40   79    4   40  129    4
            128  139    4    6  149    4    6  159
              4  144  209    4
    datetime (unknown)

    body (0)

#### RECORD 82 Bolus 2013-04-02T17:13:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-04-02T17:13:53)
    0000   0x75 0x0d 0x51 0x02 0x0d                   u.Q..
    body (0)

#### RECORD 83 CalBGForPH 2013-04-02T19:19:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-04-02T19:19:16)
    0000   0x50 0x13 0x33 0x02 0x0d                   P.3..
    body (0)

`end logs/ReadHistoryData-page-31.data: 84 records`
