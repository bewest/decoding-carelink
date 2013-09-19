## START analysis/ianj/raw//ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 1014, found 8 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x94 0xa4                                  ..
##### DEBUG DECIMAL
            148  164
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.4, 'curve': 4},
 {'age': 106, 'amount': 1.4, 'curve': 4},
 {'age': 116, 'amount': 2.2, 'curve': 4},
 {'age': 70, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x42 0x04 0x38 0x6a 0x04    \.`B.8j.
    0008   0x58 0x74 0x04 0x68 0x46 0x14              Xt.hF.
    decimal
             92   14   96   66    4   56  106    4
             88  116    4  104   70   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-09-06T15:44:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x98 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  152    0
    datetime (2013-09-06T15:44:18)
    0000   0x92 0x6c 0x4f 0x66 0x0d                   .lOf.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-09-06T18:28:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-09-06T18:28:26)
    0000   0x9a 0x5c 0x32 0x66 0x0d                   .\2f.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 Ian3F 2013-09-06T18:28:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-09-06T18:28:26)
    0000   0x9a 0x5c 0xf2 0x66 0x0d                   .\.f.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2013-09-06T18:28:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 84,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-09-06T18:28:58)
    0000   0xba 0x5c 0x12 0x66 0x0d                   .\.f.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    !..n.64.
    0008   0x78 0x00 0x00 0x10 0x00 0x9c 0x36         x.....6
    decimal
             33  144    0  110   23   54   52    0
            120    0    0   16    0  156   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 1.0, 'curve': 4},
 {'age': 230, 'amount': 2.4, 'curve': 4},
 {'age': 14, 'amount': 1.4, 'curve': 20},
 {'age': 24, 'amount': 2.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0xaa 0x04 0x60 0xe6 0x04    \.(..`..
    0008   0x38 0x0e 0x14 0x58 0x18 0x14              8..X..
    decimal
             92   14   40  170    4   96  230    4
             56   14   20   88   24   20
    datetime (unknown)

    body (0)

#### RECORD 6 Ian69 2013-09-06T18:28:58 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-06T18:28:58)
    0000   0xba 0x5c 0x72 0x06 0x0d                   .\r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 0]
#### RECORD 7 Bolus 2013-09-06T18:28:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x10 0x00    ........
    decimal
              1    0  156    0  156    0   16    0
    datetime (2013-09-06T18:28:58)
    0000   0xba 0x5c 0x52 0x66 0x0d                   .\Rf.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2013-09-06T21:43:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-09-06T21:43:40)
    0000   0xa8 0x6b 0x35 0x66 0x0d                   .k5f.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2013-09-06T21:43:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2013-09-06T21:43:40)
    0000   0xa8 0x6b 0xb5 0x66 0x0d                   .k.f.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2013-09-06T22:44:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-06T22:44:26)
    0000   0x9a 0x6c 0x16 0x66 0x0d                   .l.f.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 3.9, 'curve': 20},
 {'age': 170, 'amount': 1.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x9c 0x00 0x14 0x28 0xaa 0x14    \....(..
    decimal
             92    8  156    0   20   40  170   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-09-06T22:44:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-09-06T22:44:27)
    0000   0x9b 0x6c 0x56 0x66 0x0d                   .lVf.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-09-06T23:33:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-06T23:33:01)
    0000   0x81 0x61 0x17 0x66 0x0d                   .a.f.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 2.4, 'curve': 4},
 {'age': 49, 'amount': 3.9, 'curve': 20},
 {'age': 219, 'amount': 1.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x60 0x37 0x04 0x9c 0x31 0x14    \.`7..1.
    0008   0x28 0xdb 0x14                             (..
    decimal
             92   11   96   55    4  156   49   20
             40  219   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-09-06T23:33:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x54 0x00    ..P.P.T.
    decimal
              1    0   80    0   80    0   84    0
    datetime (2013-09-06T23:33:01)
    0000   0x81 0x61 0x57 0x66 0x0d                   .aWf.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 BasalProfileStart 2013-09-07T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-07T00:00:00)
    0000   0x80 0x40 0x00 0x07 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 17 ResultTotals (2000, 10, 0, 0, 13, 6) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xcd                   .....
    decimal
              7    0    0    6  205
    datetime ((2000, 10, 0, 0, 13, 6))
    0000   0x86 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x86 0x8d 0x06 0x00 0x6b 0x33 0x9c    n....k3.
    0008   0x05 0x00 0x00 0x06 0xcd 0x03 0x85 0x34    .......4
    0010   0x03 0x48 0x30 0x00 0xd7 0x02 0xac 0x00    .H0.....
    0018   0x00 0x00 0x9c 0x00 0x00 0x07 0x00 0x01    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  134  141    6    0  107   51  156
              5    0    0    6  205    3  133   52
              3   72   48    0  215    2  172    0
              0    0  156    0    0    7    0    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 19 CalBGForPH 2013-09-07T01:20:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 262}
```
    op hex (2)
    0000   0x0a 0x06                                  ..
    decimal
             10    6
    datetime (2013-09-07T01:20:42)
    0000   0xaa 0x54 0x21 0x67 0x8d                   .T!g.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 Ian3F 2013-09-07T01:20:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2013-09-07T01:20:42)
    0000   0xaa 0x54 0xc1 0x67 0x0d                   .T.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 BolusWizard 2013-09-07T01:20:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 145,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 15.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x91                                  [.
    decimal
             91  145
    datetime (2013-09-07T01:20:55)
    0000   0xb7 0x54 0x01 0x67 0x0d                   .T.g.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x9c 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x40 0x00 0x5c 0x36         ...@.\6
    decimal
              0  144    0  110   23   54  156    0
              0    0    0   64    0   92   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 2.0, 'curve': 4},
 {'age': 162, 'amount': 2.4, 'curve': 4},
 {'age': 156, 'amount': 3.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x70 0x04 0x60 0xa2 0x04    \.Pp.`..
    0008   0x9c 0x9c 0x14                             ...
    decimal
             92   11   80  112    4   96  162    4
            156  156   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-09-07T01:20:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x40 0x00    ..p.p.@.
    decimal
              1    0  112    0  112    0   64    0
    datetime (2013-09-07T01:20:56)
    0000   0xb8 0x54 0x41 0x67 0x0d                   .TAg.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 CalBGForPH 2013-09-07T03:43:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-09-07T03:43:44)
    0000   0xac 0x6b 0x23 0x67 0x0d                   .k#g.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 Ian3F 2013-09-07T03:43:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2013-09-07T03:43:44)
    0000   0xac 0x6b 0xe3 0x67 0x0d                   .k.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BasalProfileStart 2013-09-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-07T04:00:00)
    0000   0x80 0x40 0x04 0x07 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 27 BolusWizard 2013-09-07T06:18:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T06:18:37)
    0000   0xa5 0x52 0x06 0x67 0x0d                   .R.g.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.8, 'curve': 20},
 {'age': 154, 'amount': 2.0, 'curve': 20},
 {'age': 204, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x2c 0x14 0x50 0x9a 0x14    \.p,.P..
    0008   0x60 0xcc 0x14                             `..
    decimal
             92   11  112   44   20   80  154   20
             96  204   20
    datetime (unknown)

    body (0)

#### RECORD 29 BolusWizard 2013-09-07T06:18:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T06:18:52)
    0000   0xb4 0x52 0x06 0x67 0x0d                   .R.g.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.8, 'curve': 20},
 {'age': 154, 'amount': 2.0, 'curve': 20},
 {'age': 204, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x2c 0x14 0x50 0x9a 0x14    \.p,.P..
    0008   0x60 0xcc 0x14                             `..
    decimal
             92   11  112   44   20   80  154   20
             96  204   20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-09-07T06:18:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2013-09-07T06:18:52)
    0000   0xb4 0x52 0x46 0x67 0x0d                   .RFg.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 BasalProfileStart 2013-09-07T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-07T09:30:00)
    0000   0x80 0x5e 0x09 0x07 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 33 BolusWizard 2013-09-07T09:36:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T09:36:20)
    0000   0x94 0x64 0x09 0x67 0x0d                   .d.g.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 198, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0xc6 0x04                   \.h..
    decimal
             92    5  104  198    4
    datetime (unknown)

    body (0)

#### RECORD 35 Ian69 2013-09-07T09:36:20 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-07T09:36:20)
    0000   0x94 0x64 0x09 0x07 0x0d                   .d...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 1]
#### RECORD 36 Bolus 2013-09-07T09:36:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x10 0x00    ..$.$...
    decimal
              1    0   36    0   36    0   16    0
    datetime (2013-09-07T09:36:20)
    0000   0x94 0x64 0x49 0x67 0x0d                   .dIg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 ChangeTimeDisplay 2013-09-07T10:14:17 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x01                                  d.
    decimal
            100    1
    datetime (2013-09-07T10:14:17)
    0000   0x91 0x4e 0x0a 0x07 0x0d                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 ChangeTime 2013-09-07T10:14:41 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-09-07T10:14:41)
    0000   0xa9 0x4e 0x0a 0x07 0x0d                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 NewTimeSet 2013-09-07T01:14:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-09-07T01:14:00)
    0000   0x80 0x4e 0x01 0x07 0x0d                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 40 BasalProfileStart 2013-09-07T01:14:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-07T01:14:00)
    0000   0x80 0x4e 0x01 0x07 0x0d                   .N...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 41 CalBGForPH 2013-09-07T02:40:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-09-07T02:40:37)
    0000   0xa5 0x68 0x22 0x67 0x0d                   .h"g.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 Ian3F 2013-09-07T02:40:37 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-09-07T02:40:37)
    0000   0xa5 0x68 0xa2 0x67 0x0d                   .h.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2013-09-07T02:47:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 65,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 1.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 128}
```
    op hex (2)
    0000   0x5b 0x41                                  [A
    decimal
             91   65
    datetime (2013-09-07T02:47:25)
    0000   0x99 0x6f 0x02 0x67 0x0d                   .o.g.
    body (15)
    hex
    0000   0x24 0x90 0x00 0x6e 0x17 0x36 0x10 0x00    $..n.6..
    0008   0x80 0x00 0x00 0x10 0x00 0x80 0x36         ......6
    decimal
             36  144    0  110   23   54   16    0
            128    0    0   16    0  128   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 0.9, 'curve': 4},
 {'age': 73, 'amount': 2.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x8b 0x04 0x68 0x49 0x14    \.$..hI.
    decimal
             92    8   36  139    4  104   73   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-09-07T02:47:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x10 0x00    ........
    decimal
              1    0  128    0  128    0   16    0
    datetime (2013-09-07T02:47:26)
    0000   0x9a 0x6f 0x42 0x67 0x0d                   .oBg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2013-09-07T02:54:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 6,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 20}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T02:54:43)
    0000   0xab 0x76 0x02 0x67 0x0d                   .v.g.
    body (15)
    hex
    0000   0x06 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x14 0x00 0x00 0x00 0x00 0x14 0x36         ......6
    decimal
              6  144    0  110   23   54    0    0
             20    0    0    0    0   20   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 2.35, 'curve': 4},
 {'age': 16, 'amount': 0.85, 'curve': 4},
 {'age': 146, 'amount': 0.9, 'curve': 4},
 {'age': 80, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x5e 0x06 0x04 0x22 0x10 0x04    \.^.."..
    0008   0x24 0x92 0x04 0x68 0x50 0x14              $..hP.
    decimal
             92   14   94    6    4   34   16    4
             36  146    4  104   80   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-09-07T02:54:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x8c 0x00    ........
    decimal
              1    0   20    0   20    0  140    0
    datetime (2013-09-07T02:54:43)
    0000   0xab 0x76 0x42 0x67 0x0d                   .vBg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BasalProfileStart 2013-09-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-07T04:00:00)
    0000   0x80 0x40 0x04 0x07 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 50 BasalProfileStart 2013-09-07T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-07T09:30:00)
    0000   0x80 0x5e 0x09 0x07 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 51 BolusWizard 2013-09-07T10:23:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T10:23:55)
    0000   0xb7 0x57 0x0a 0x67 0x0d                   .W.g.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 199, 'amount': 2.85, 'curve': 20},
 {'age': 209, 'amount': 0.85, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x72 0xc7 0x14 0x22 0xd1 0x14    \.r.."..
    decimal
             92    8  114  199   20   34  209   20
    datetime (unknown)

    body (0)

#### RECORD 53 Ian69 2013-09-07T10:23:55 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-07T10:23:55)
    0000   0xb7 0x57 0x0a 0x07 0x0d                   .W...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 0]
#### RECORD 54 Bolus 2013-09-07T10:23:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x00 0x00    ..|.|...
    decimal
              1    0  124    0  124    0    0    0
    datetime (2013-09-07T10:23:55)
    0000   0xb7 0x57 0x4a 0x67 0x0d                   .WJg.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 CalBGForPH 2013-09-07T11:32:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 285}
```
    op hex (2)
    0000   0x0a 0x1d                                  ..
    decimal
             10   29
    datetime (2013-09-07T11:32:53)
    0000   0xb5 0x60 0x2b 0x67 0x8d                   .`+g.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 Ian3F 2013-09-07T11:32:53 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2013-09-07T11:32:53)
    0000   0xb5 0x60 0xab 0x67 0x0d                   .`.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2013-09-07T11:33:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 158,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 9.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 18.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9e                                  [.
    decimal
             91  158
    datetime (2013-09-07T11:33:26)
    0000   0x9a 0x61 0x0b 0x67 0x0d                   .a.g.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xb4 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x5c 0x00 0x58 0x36         ...\.X6
    decimal
              0  144    0  110   23   54  180    0
              0    0    0   92    0   88   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 3.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x4b 0x04                   \.|K.
    decimal
             92    5  124   75    4
    datetime (unknown)

    body (0)

#### RECORD 59 Ian69 2013-09-07T11:33:26 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-07T11:33:26)
    0000   0x9a 0x61 0x0b 0x07 0x0d                   .a...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 1, 1]
#### RECORD 60 Bolus 2013-09-07T11:33:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x5c 0x00    ..h.h.\.
    decimal
              1    0  104    0  104    0   92    0
    datetime (2013-09-07T11:33:26)
    0000   0x9a 0x61 0x4b 0x67 0x0d                   .aKg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 BasalProfileStart 2013-09-07T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-07T13:00:00)
    0000   0x80 0x40 0x0d 0x07 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 62 CalBGForPH 2013-09-07T15:27:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-09-07T15:27:49)
    0000   0xb1 0x5b 0x2f 0x67 0x0d                   .[/g.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2013-09-07T15:27:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2013-09-07T15:27:49)
    0000   0xb1 0x5b 0x0f 0x67 0x0d                   .[.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 BolusWizard 2013-09-07T15:56:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T15:56:49)
    0000   0xb1 0x78 0x0f 0x67 0x0d                   .x.g.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 2.6, 'curve': 20},
 {'age': 82, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0x0c 0x14 0x7c 0x52 0x14    \.h..|R.
    decimal
             92    8  104   12   20  124   82   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-09-07T15:56:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-09-07T15:56:49)
    0000   0xb1 0x78 0x4f 0x67 0x0d                   .xOg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 CalBGForPH 2013-09-07T17:10:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 65}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2013-09-07T17:10:39)
    0000   0xa7 0x4a 0x31 0x67 0x0d                   .J1g.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 Ian3F 2013-09-07T17:10:39 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2013-09-07T17:10:39)
    0000   0xa7 0x4a 0x31 0x67 0x0d                   .J1g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 69 CalBGForPH 2013-09-07T18:15:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-09-07T18:15:57)
    0000   0xb9 0x4f 0x32 0x67 0x0d                   .O2g.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 70 Ian3F 2013-09-07T18:15:57 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-09-07T18:15:57)
    0000   0xb9 0x4f 0x92 0x67 0x0d                   .O.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 71 CalBGForPH 2013-09-07T19:52:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 279}
```
    op hex (2)
    0000   0x0a 0x17                                  ..
    decimal
             10   23
    datetime (2013-09-07T19:52:39)
    0000   0xa7 0x74 0x33 0x67 0x8d                   .t3g.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 72 Ian3F 2013-09-07T19:52:39 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2013-09-07T19:52:39)
    0000   0xa7 0x74 0xf3 0x67 0x0d                   .t.g.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 BolusWizard 2013-09-07T19:52:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 155,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 17.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2013-09-07T19:52:54)
    0000   0xb6 0x74 0x13 0x67 0x0d                   .t.g.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xac 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x04 0x00 0xa8 0x36         ......6
    decimal
              0  144    0  110   23   54  172    0
              0    0    0    4    0  168   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 0.95, 'curve': 4},
 {'age': 244, 'amount': 1.75, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x26 0xea 0x04 0x46 0xf4 0x04    \.&..F..
    decimal
             92    8   38  234    4   70  244    4
    datetime (unknown)

    body (0)

#### RECORD 75 Ian69 2013-09-07T19:52:55 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-07T19:52:55)
    0000   0xb7 0x74 0x73 0x07 0x0d                   .ts..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 1]
#### RECORD 76 Bolus 2013-09-07T19:52:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x04 0x00    ........
    decimal
              1    0  168    0  168    0    4    0
    datetime (2013-09-07T19:52:55)
    0000   0xb7 0x74 0x53 0x67 0x0d                   .tSg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 77 BolusWizard 2013-09-07T23:47:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T23:47:11)
    0000   0x8b 0x6f 0x17 0x67 0x0d                   .o.g.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 4.2, 'curve': 4},
 {'age': 213, 'amount': 0.95, 'curve': 20},
 {'age': 223, 'amount': 1.75, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa8 0xef 0x04 0x26 0xd5 0x14    \....&..
    0008   0x46 0xdf 0x14                             F..
    decimal
             92   11  168  239    4   38  213   20
             70  223   20
    datetime (unknown)

    body (0)

#### RECORD 79 BasalProfileStart 2013-09-08T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-08T00:00:00)
    0000   0x80 0x40 0x00 0x08 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 80 ResultTotals (2000, 10, 0, 0, 13, 7) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x7e                   ....~
    decimal
              7    0    0    8  126
    datetime ((2000, 10, 0, 0, 13, 7))
    0000   0x87 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
`end analysis/ianj/raw//ReadHistoryData-page-5.data: 81 records`
