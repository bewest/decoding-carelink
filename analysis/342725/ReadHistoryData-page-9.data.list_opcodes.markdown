## START logs/ReadHistoryData-page-9.data
#### RECORD 0 MResultTotals 2014-03-04T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd0                   .....
    decimal
              7    0    0    4  208
    datetime (2014-03-04T00:00:00)
    0000   0x23 0x8e                                  #.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 Sara6E 2014-03-04T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-04T00:00:00)
    0000   0x23 0x8e                                  #.
    body (49)
    hex
    0000   0x05 0x00 0x96 0x51 0xc5 0x07 0x00 0x00    ...Q....
    0008   0x04 0xd0 0x01 0xd4 0x26 0x02 0xfc 0x3e    ....&..>
    0010   0x00 0x89 0x01 0xb4 0x00 0xf4 0x00 0x54    .......T
    0018   0x00 0x00 0x04 0x04 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x84    ........
    0028   0xbc 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  150   81  197    7    0    0
              4  208    1  212   38    2  252   62
              0  137    1  180    0  244    0   84
              0    0    4    4    1    0    0    0
              0    0    0    0    0    0    0  132
            188    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 2 CalBGForPH 2014-03-04T00:27:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2014-03-04T00:27:40)
    0000   0x28 0xdb 0x20 0x04 0x0e                   (. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2014-03-04T00:27:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2014-03-04T00:27:47)
    0000   0x2f 0xdb 0x00 0x64 0x0e                   /..d.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x34 0x00    .P.n7P4.
    0008   0x00 0x00 0x00 0x20 0x00 0x14 0x64         ... ..d
    decimal
              0   80    0  110   55   80   52    0
              0    0    0   32    0   20  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 1.3, 'curve': 128},
 {'age': 105, 'amount': 1.3, 'curve': 128},
 {'age': 235, 'amount': 6.3, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x37 0x80 0x34 0x69 0x80    \.47.4i.
    0008   0xfc 0xeb 0x80                             ...
    decimal
             92   11   52   55  128   52  105  128
            252  235  128
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2014-03-04T00:27:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x20 0x00    ..,.,. .
    decimal
              1    0   44    0   44    0   32    0
    datetime (2014-03-04T00:27:47)
    0000   0x2f 0xdb 0x40 0x64 0x0e                   /.@d.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 BasalProfileStart 2014-03-04T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-04T02:00:00)
    0000   0x00 0xc0 0x02 0x04 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2014-03-04T02:26:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 65}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2014-03-04T02:26:27)
    0000   0x1b 0xda 0x22 0x64 0x0e                   .."d.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2014-03-04T02:26:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-04T02:26:27)
    0000   0x1b 0xda 0x22 0x64 0x0e                   .."d.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 BasalProfileStart 2014-03-04T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-04T04:00:00)
    0000   0x00 0xc0 0x04 0x04 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 10 BasalProfileStart 2014-03-04T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-04T06:00:00)
    0000   0x00 0xc0 0x06 0x04 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 11 CalBGForPH 2014-03-04T08:27:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2014-03-04T08:27:15)
    0000   0x0f 0xdb 0x28 0x64 0x0e                   ..(d.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2014-03-04T08:27:15 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-04T08:27:15)
    0000   0x0f 0xdb 0x68 0x64 0x0e                   ..hd.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2014-03-04T08:27:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2014-03-04T08:27:32)
    0000   0x20 0xdb 0x08 0x04 0x0e                    ....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x24 0x00    .P.n(P$.
    0008   0x00 0x00 0x00 0x00 0x00 0x24 0x64         .....$d
    decimal
              0   80    0  110   40   80   36    0
              0    0    0    0    0   36  100
    HOUR BITS: [1, 1, 0]
#### RECORD 14 Bolus 2014-03-04T08:27:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2014-03-04T08:27:32)
    0000   0x20 0xdb 0x48 0x04 0x0e                    .H..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 BolusWizard 2014-03-04T08:38:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 3.6,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2014-03-04T08:38:24)
    0000   0x18 0xe6 0x08 0x64 0x0e                   ...d.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x6e 0x28 0x50 0x24 0x00    .P.n(P$.
    0008   0x24 0x00 0x00 0x24 0x00 0x24 0x64         $..$.$d
    decimal
             10   80    0  110   40   80   36    0
             36    0    0   36    0   36  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 0.9, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0x10 0x80                   \.$..
    decimal
             92    5   36   16  128
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2014-03-04T08:38:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x24 0x00    ..$.$.$.
    decimal
              1    0   36    0   36    0   36    0
    datetime (2014-03-04T08:38:24)
    0000   0x18 0xe6 0x48 0x64 0x0e                   ..Hd.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 BasalProfileStart 2014-03-04T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-04T10:30:00)
    0000   0x00 0xde 0x0a 0x04 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 19 CalBGForPH 2014-03-04T13:50:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2014-03-04T13:50:07)
    0000   0x07 0xf2 0x2d 0x04 0x0e                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 BolusWizard 2014-03-04T13:50:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 65,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 216}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2014-03-04T13:50:18)
    0000   0x12 0xf2 0x0d 0x64 0x0e                   ...d.
    body (15)
    hex
    0000   0x41 0x50 0x00 0x78 0x32 0x50 0x14 0x00    AP.x2P..
    0008   0xd8 0x00 0x00 0x00 0x00 0xec 0x64         ......d
    decimal
             65   80    0  120   50   80   20    0
            216    0    0    0    0  236  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 0.9, 'curve': 144},
 {'age': 72, 'amount': 0.9, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x3e 0x90 0x24 0x48 0x90    \.$>.$H.
    decimal
             92    8   36   62  144   36   72  144
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2014-03-04T13:50:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 23.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xec 0x00 0xec 0x00 0x00 0x00    ........
    decimal
              1    0  236    0  236    0    0    0
    datetime (2014-03-04T13:50:18)
    0000   0x12 0xf2 0x4d 0x64 0x0e                   ..Md.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 CalBGForPH 2014-03-04T15:37:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 237}
```
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2014-03-04T15:37:27)
    0000   0x1b 0xe5 0x2f 0x64 0x0e                   ../d.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 Ian3F 2014-03-04T15:37:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2014-03-04T15:37:27)
    0000   0x1b 0xe5 0xaf 0x64 0x0e                   ...d.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 BolusWizard 2014-03-04T15:37:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 237,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 10.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2014-03-04T15:37:51)
    0000   0x33 0xe5 0x0f 0x04 0x0e                   3....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x6c 0x00    .P.x2Pl.
    0008   0x00 0x00 0x00 0x14 0x00 0x58 0x64         .....Xd
    decimal
              0   80    0  120   50   80  108    0
              0    0    0   20    0   88  100
    HOUR BITS: [1, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 3.35, 'curve': 128},
 {'age': 115, 'amount': 2.55, 'curve': 128},
 {'age': 169, 'amount': 0.9, 'curve': 144},
 {'age': 179, 'amount': 0.9, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x86 0x69 0x80 0x66 0x73 0x80    \..i.fs.
    0008   0x24 0xa9 0x90 0x24 0xb3 0x90              $..$..
    decimal
             92   14  134  105  128  102  115  128
             36  169  144   36  179  144
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2014-03-04T15:37:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x14 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   20    0
    datetime (2014-03-04T15:37:51)
    0000   0x33 0xe5 0x4f 0x04 0x0e                   3.O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 CalBGForPH 2014-03-04T16:59:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 237}
```
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2014-03-04T16:59:23)
    0000   0x17 0xfb 0x30 0x04 0x0e                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 BolusWizard 2014-03-04T16:59:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 237,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 10.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2014-03-04T16:59:26)
    0000   0x1a 0xfb 0x10 0x64 0x0e                   ...d.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x6c 0x00    .P.x2Pl.
    0008   0x00 0x00 0x00 0x14 0x00 0x58 0x64         .....Xd
    decimal
              0   80    0  120   50   80  108    0
              0    0    0   20    0   88  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 2.2, 'curve': 128},
 {'age': 187, 'amount': 3.35, 'curve': 128},
 {'age': 197, 'amount': 2.55, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x57 0x80 0x86 0xbb 0x80    \.XW....
    0008   0x66 0xc5 0x80                             f..
    decimal
             92   11   88   87  128  134  187  128
            102  197  128
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2014-03-04T16:59:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x14 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   20    0
    datetime (2014-03-04T16:59:27)
    0000   0x1b 0xfb 0x50 0x64 0x0e                   ..Pd.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2014-03-04T17:16:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-04T17:16:51)
    0000   0x33 0xd0 0x11 0x64 0x0e                   3..d.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x64          .... d
    decimal
             10   80    0  120   50   80    0    0
             32    0    0    0    0   32  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.2, 'curve': 128},
 {'age': 104, 'amount': 2.2, 'curve': 128},
 {'age': 204, 'amount': 3.35, 'curve': 128},
 {'age': 214, 'amount': 2.55, 'curve': 128}]
```
    op hex (14)
    0000   0x5c 0x0e 0x58 0x18 0x80 0x58 0x68 0x80    \.X..Xh.
    0008   0x86 0xcc 0x80 0x66 0xd6 0x80              ...f..
    decimal
             92   14   88   24  128   88  104  128
            134  204  128  102  214  128
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2014-03-04T17:16:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x58 0x00    .. . .X.
    decimal
              1    0   32    0   32    0   88    0
    datetime (2014-03-04T17:16:51)
    0000   0x33 0xd0 0x51 0x64 0x0e                   3.Qd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2014-03-04T18:02:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-04T18:02:50)
    0000   0x32 0xc2 0x12 0x64 0x0e                   2..d.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             25   80    0  120   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.8, 'curve': 128},
 {'age': 70, 'amount': 2.2, 'curve': 128},
 {'age': 150, 'amount': 2.2, 'curve': 128},
 {'age': 250, 'amount': 3.35, 'curve': 128},
 {'age': 4, 'amount': 2.55, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x32 0x80 0x58 0x46 0x80    \. 2.XF.
    0008   0x58 0x96 0x80 0x86 0xfa 0x80 0x66 0x04    X.....f.
    0010   0x90                                       .
    decimal
             92   17   32   50  128   88   70  128
             88  150  128  134  250  128  102    4
            144
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2014-03-04T18:02:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x34 0x00    ..P.P.4.
    decimal
              1    0   80    0   80    0   52    0
    datetime (2014-03-04T18:02:50)
    0000   0x32 0xc2 0x52 0x64 0x0e                   2.Rd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2014-03-04T18:07:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-04T18:07:46)
    0000   0x2e 0xc7 0x12 0x64 0x0e                   ...d.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             25   80    0  120   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 2.0, 'curve': 128},
 {'age': 55, 'amount': 0.8, 'curve': 128},
 {'age': 75, 'amount': 2.2, 'curve': 128},
 {'age': 155, 'amount': 2.2, 'curve': 128},
 {'age': 255, 'amount': 3.35, 'curve': 128},
 {'age': 9, 'amount': 2.55, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x50 0x05 0x80 0x20 0x37 0x80    \.P.. 7.
    0008   0x58 0x4b 0x80 0x58 0x9b 0x80 0x86 0xff    XK.X....
    0010   0x80 0x66 0x09 0x90                        .f..
    decimal
             92   20   80    5  128   32   55  128
             88   75  128   88  155  128  134  255
            128  102    9  144
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2014-03-04T18:07:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x7c 0x00    ..P.P.|.
    decimal
              1    0   80    0   80    0  124    0
    datetime (2014-03-04T18:07:46)
    0000   0x2e 0xc7 0x52 0x64 0x0e                   ..Rd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2014-03-04T18:33:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-04T18:33:11)
    0000   0x0b 0xe1 0x12 0x64 0x0e                   ...d.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x64          .... d
    decimal
             10   80    0  120   50   80    0    0
             32    0    0    0    0   32  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 4.0, 'curve': 128},
 {'age': 81, 'amount': 0.8, 'curve': 128},
 {'age': 101, 'amount': 2.2, 'curve': 128},
 {'age': 181, 'amount': 2.2, 'curve': 128},
 {'age': 25, 'amount': 3.35, 'curve': 144},
 {'age': 35, 'amount': 2.55, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0xa0 0x1f 0x80 0x20 0x51 0x80    \.... Q.
    0008   0x58 0x65 0x80 0x58 0xb5 0x80 0x86 0x19    Xe.X....
    0010   0x90 0x66 0x23 0x90                        .f#.
    decimal
             92   20  160   31  128   32   81  128
             88  101  128   88  181  128  134   25
            144  102   35  144
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2014-03-04T18:33:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x94 0x00    .. . ...
    decimal
              1    0   32    0   32    0  148    0
    datetime (2014-03-04T18:33:11)
    0000   0x0b 0xe1 0x52 0x64 0x0e                   ..Rd.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 PumpSuspend 2014-03-04T19:31:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-04T19:31:38)
    0000   0x26 0xdf 0x13 0x04 0x0e                   &....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 CalBGForPH 2014-03-04T23:12:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2014-03-04T23:12:47)
    0000   0x2f 0xcc 0x37 0x64 0x0e                   /.7d.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2014-03-04T23:12:47 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-03-04T23:12:47)
    0000   0x2f 0xcc 0x77 0x64 0x0e                   /.wd.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 47 BasalProfileStart 2014-03-04T23:12:59 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-04T23:12:59)
    0000   0x3b 0xcc 0x17 0x04 0x0e                   ;....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 48 PumpResume 2014-03-04T23:12:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-04T23:12:59)
    0000   0x3b 0xcc 0x17 0x04 0x0e                   ;....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2014-03-04T23:13:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 4.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2014-03-04T23:13:10)
    0000   0x0a 0xcd 0x17 0x04 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x2c 0x00    .P.n7P,.
    0008   0x00 0x00 0x00 0x00 0x00 0x2c 0x64         .....,d
    decimal
              0   80    0  110   55   80   44    0
              0    0    0    0    0   44  100
    HOUR BITS: [1, 1, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 0.8, 'curve': 144},
 {'age': 55, 'amount': 4.0, 'curve': 144},
 {'age': 105, 'amount': 0.8, 'curve': 144},
 {'age': 125, 'amount': 2.2, 'curve': 144},
 {'age': 205, 'amount': 2.2, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x19 0x90 0xa0 0x37 0x90    \. ...7.
    0008   0x20 0x69 0x90 0x58 0x7d 0x90 0x58 0xcd     i.X}.X.
    0010   0x90                                       .
    decimal
             92   17   32   25  144  160   55  144
             32  105  144   88  125  144   88  205
            144
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2014-03-04T23:13:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2014-03-04T23:13:10)
    0000   0x0a 0xcd 0x57 0x04 0x0e                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 BasalProfileStart 2014-03-05T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-05T00:00:00)
    0000   0x00 0xc0 0x00 0x05 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 53 MResultTotals 2014-03-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime (2014-03-05T00:00:00)
    0000   0x24 0x8e                                  $.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 54 Sara6E 2014-03-05T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-05T00:00:00)
    0000   0x24 0x8e                                  $.
    body (49)
    hex
    0000   0x05 0x00 0xa3 0x41 0xed 0x07 0x00 0x00    ...A....
    0008   0x04 0xd2 0x01 0xa6 0x22 0x03 0x2c 0x42    ....".,B
    0010   0x00 0x91 0x01 0x04 0x01 0x3c 0x00 0xec    .....<..
    0018   0x00 0x00 0x05 0x05 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x7e    .......~
    0028   0xed 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  163   65  237    7    0    0
              4  210    1  166   34    3   44   66
              0  145    1    4    1   60    0  236
              0    0    5    5    1    0    0    0
              0    0    0    0    0    0    0  126
            237    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 55 CalBGForPH 2014-03-05T00:57:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2014-03-05T00:57:27)
    0000   0x1b 0xf9 0x20 0x65 0x0e                   .. e.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 Ian3F 2014-03-05T00:57:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-03-05T00:57:27)
    0000   0x1b 0xf9 0x00 0x65 0x0e                   ...e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2014-03-05T00:57:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2014-03-05T00:57:41)
    0000   0x29 0xf9 0x00 0x05 0x0e                   )....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x34 0x00    .P.n7P4.
    0008   0x00 0x00 0x00 0x08 0x00 0x2c 0x64         .....,d
    decimal
              0   80    0  110   55   80   52    0
              0    0    0    8    0   44  100
    HOUR BITS: [1, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 1.5, 'curve': 128},
 {'age': 129, 'amount': 0.8, 'curve': 144},
 {'age': 159, 'amount': 4.0, 'curve': 144},
 {'age': 209, 'amount': 0.8, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x69 0x80 0x20 0x81 0x90    \.<i. ..
    0008   0xa0 0x9f 0x90 0x20 0xd1 0x90              ... ..
    decimal
             92   14   60  105  128   32  129  144
            160  159  144   32  209  144
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2014-03-05T00:57:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x08 0x00    ..L.L...
    decimal
              1    0   76    0   76    0    8    0
    datetime (2014-03-05T00:57:41)
    0000   0x29 0xf9 0x40 0x05 0x0e                   ).@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 60 CalBGForPH 2014-03-05T01:16:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2014-03-05T01:16:41)
    0000   0x29 0xd0 0x21 0x65 0x0e                   ).!e.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 61 Ian3F 2014-03-05T01:16:41 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-03-05T01:16:41)
    0000   0x29 0xd0 0xe1 0x65 0x0e                   )..e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2014-03-05T01:17:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2014-03-05T01:17:11)
    0000   0x0b 0xd1 0x21 0x65 0x0e                   ..!e.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2014-03-05T01:17:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-03-05T01:17:11)
    0000   0x0b 0xd1 0x01 0x65 0x0e                   ...e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 BasalProfileStart 2014-03-05T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-05T02:00:00)
    0000   0x00 0xc0 0x02 0x05 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 65 BasalProfileStart 2014-03-05T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-05T04:00:00)
    0000   0x00 0xc0 0x04 0x05 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 66 BasalProfileStart 2014-03-05T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-05T06:00:00)
    0000   0x00 0xc0 0x06 0x05 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 67 CalBGForPH 2014-03-05T07:11:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2014-03-05T07:11:11)
    0000   0x0b 0xcb 0x27 0x65 0x0e                   ..'e.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 Ian3F 2014-03-05T07:11:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2014-03-05T07:11:11)
    0000   0x0b 0xcb 0x47 0x65 0x0e                   ..Ge.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 69 BolusWizard 2014-03-05T07:11:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2014-03-05T07:11:38)
    0000   0x26 0xcb 0x07 0x05 0x0e                   &....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x14 0x00    .P.n(P..
    0008   0x00 0x00 0x00 0x00 0x00 0x14 0x64         ......d
    decimal
              0   80    0  110   40   80   20    0
              0    0    0    0    0   20  100
    HOUR BITS: [1, 1, 0]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 1.9, 'curve': 144},
 {'age': 223, 'amount': 1.5, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x7b 0x90 0x3c 0xdf 0x90    \.L{.<..
    decimal
             92    8   76  123  144   60  223  144
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2014-03-05T07:11:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x00 0x00    ........
    decimal
              1    0   20    0   20    0    0    0
    datetime (2014-03-05T07:11:38)
    0000   0x26 0xcb 0x47 0x05 0x0e                   &.G..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 BolusWizard 2014-03-05T09:18:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-05T09:18:33)
    0000   0x21 0xd2 0x09 0x65 0x0e                   !..e.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    .P.n(P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   40   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 73 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x91                                  ..
    decimal
              0  145
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-9.data: 74 records`
