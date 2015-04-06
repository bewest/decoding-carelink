## START analysis/736868/logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 1015, found 7 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x60 0x9d                                  `.
##### DEBUG DECIMAL
             96  157
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 3.0, 'curve': 4},
 {'age': 25, 'amount': 3.8, 'curve': 4},
 {'age': 19, 'amount': 5.6, 'curve': 20},
 {'age': 79, 'amount': 1.25, 'curve': 20},
 {'age': 89, 'amount': 2.2, 'curve': 20},
 {'age': 99, 'amount': 0.15, 'curve': 21}]
```
    op hex (20)
    0000   0x5c 0x14 0x78 0x05 0x04 0x98 0x19 0x04    \.x.....
    0008   0xe0 0x13 0x14 0x32 0x4f 0x14 0x58 0x59    ...2O.XY
    0010   0x14 0x06 0x63 0x15                        ..c.
    decimal
             92   20  120    5    4  152   25    4
            224   19   20   50   79   20   88   89
             20    6   99   21
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-02-18T16:31:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x01 0x0c 0x00    ........
    decimal
              1    0  180    0  180    1   12    0
    datetime (2015-02-18T16:31:22)
    0000   0x16 0x9f 0x50 0x72 0x0f                   ..Pr.
    body (0)

#### RECORD 2 Ian0B 2015-02-18T19:05:23 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-18T19:05:23)
    0000   0x17 0x85 0x33 0xb2 0x0f                   ..3..
    body (0)

#### RECORD 3 Ian0B 2015-02-18T19:18:47 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xbd                             .e.
    decimal
             11  101  189
    datetime (2015-02-18T19:18:47)
    0000   0x2f 0x92 0x33 0xb2 0x0f                   /.3..
    body (0)

#### RECORD 4 LowReservoir 2015-02-18T19:28:07 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-18T19:28:07)
    0000   0x07 0x9c 0x13 0x12 0x0f                   .....
    body (0)

#### RECORD 5 Bolus 2015-02-18T19:30:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x44 0x00    ......D.
    decimal
              1    0  160    0  160    0   68    0
    datetime (2015-02-18T19:30:34)
    0000   0x22 0x9e 0x53 0x72 0x0f                   ".Sr.
    body (0)

#### RECORD 6 Ian0B 2015-02-18T21:05:23 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-18T21:05:23)
    0000   0x17 0x85 0x35 0xb2 0x0f                   ..5..
    body (0)

#### RECORD 7 Ian0B 2015-02-18T21:18:47 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-18T21:18:47)
    0000   0x2f 0x92 0x35 0xb2 0x0f                   /.5..
    body (0)

#### RECORD 8 Ian0B 2015-02-18T21:39:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-18T21:39:00)
    0000   0x00 0xa7 0x35 0xb2 0x0f                   ..5..
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-18T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-18T22:00:00)
    0000   0x00 0x80 0x16 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 10 Ian0B 2015-02-18T22:39:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-18T22:39:00)
    0000   0x00 0xa7 0x36 0xb2 0x0f                   ..6..
    body (0)

#### RECORD 11 CalBGForPH 2015-02-18T22:40:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 369}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2015-02-18T22:40:16)
    0000   0x10 0xa8 0x36 0x72 0x8f                   ..6r.
    body (0)

#### RECORD 12 Ian3F 2015-02-18T22:40:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2e                                  ?.
    decimal
             63   46
    datetime (2015-02-18T22:40:16)
    0000   0x10 0xa8 0x36 0x72 0x0f                   ..6r.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 13 BolusWizard 2015-02-18T22:40:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 369,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 3.2,
 'carb_input': 40,
 'carb_ratio': 12.0,
 'correction_estimate': -0.2,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2015-02-18T22:40:41)
    0000   0x29 0xa8 0x16 0x12 0x0f                   )....
    body (15)
    hex
    0000   0x28 0x51 0x00 0x64 0x28 0x5a 0xf8 0x00    (Q.d(Z..
    0008   0xa0 0x00 0x00 0x18 0x01 0x80 0x78         ......x
    decimal
             40   81    0  100   40   90  248    0
            160    0    0   24    1  128  120

#### RECORD 14 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 194, 'amount': 4.0, 'curve': 4},
 {'age': 118, 'amount': 1.1, 'curve': 21},
 {'age': 138, 'amount': 3.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa0 0xc2 0x04 0x2c 0x76 0x15    \....,v.
    0008   0x98 0x8a 0x14                             ...
    decimal
             92   11  160  194    4   44  118   21
            152  138   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2015-02-18T22:45:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 120,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x18 0x04    ..P.P...
    decimal
              1    0   80    0   80    0   24    4
    datetime (2015-02-18T22:45:46)
    0000   0x2e 0xad 0xb6 0x12 0x0f                   .....
    body (0)

#### RECORD 16 LowReservoir 2015-02-18T22:42:52 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-18T22:42:52)
    0000   0x34 0xaa 0x16 0x12 0x0f                   4....
    body (0)

#### RECORD 17 Bolus 2015-02-18T22:40:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2,
 'duration': 0,
 'programmed': 1.2,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x01 0x30 0x01 0x30 0x00 0x18 0x00    ..0.0...
    decimal
              1    1   48    1   48    0   24    0
    datetime (2015-02-18T22:40:41)
    0000   0x29 0xa8 0x96 0x12 0x0f                   )....
    body (0)

#### RECORD 18 Ian0B 2015-02-18T22:54:06 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x72                             .er
    decimal
             11  101  114
    datetime (2015-02-18T22:54:06)
    0000   0x06 0xb6 0x36 0xb2 0x8f                   ..6..
    body (0)

#### RECORD 19 BasalProfileStart 2015-02-19T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-19T00:00:00)
    0000   0x00 0x80 0x00 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 20 MResultTotals 2015-02-19T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0b 0xd5                   .....
    decimal
              7    0    0   11  213
    datetime (2015-02-19T00:00:00)
    0000   0x32 0x0f                                  2.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 21 Sara6E 2015-02-19T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-19T00:00:00)
    0000   0x32 0x0f                                  2.
    body (49)
    hex
    0000   0x05 0x15 0x67 0x5c 0x71 0x02 0x00 0x00    ..g\q...
    0008   0x0b 0xd5 0x03 0x21 0x1a 0x08 0xb4 0x4a    ...!...J
    0010   0x00 0xe3 0x03 0x6a 0x00 0xb4 0x01 0x62    ...j...b
    0018   0x03 0x34 0x04 0x01 0x01 0x06 0x00 0xc9    .4......
    0020   0x38 0x2c 0x00 0x1b 0x4a 0x04 0x00 0x00    8,..J...
    0028   0x00 0x00 0x0b 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   21  103   92  113    2    0    0
             11  213    3   33   26    8  180   74
              0  227    3  106    0  180    1   98
              3   52    4    1    1    6    0  201
             56   44    0   27   74    4    0    0
              0    0   11    1    0    0    0    0
              0

#### RECORD 22 Ian0B 2015-02-19T00:25:23 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xde                             .e.
    decimal
             11  101  222
    datetime (2015-02-19T00:25:23)
    0000   0x17 0x99 0x20 0xb3 0x0f                   .. ..
    body (0)

#### RECORD 23 BolusWizard 2015-02-19T01:01:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 36,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-19T01:01:41)
    0000   0x29 0x81 0x01 0x73 0x0f                   )..s.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    $P.d(Z..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x78         ......x
    decimal
             36   80    0  100   40   90    0    0
            144    0    0    0    0  144  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 0.15, 'curve': 4},
 {'age': 35, 'amount': 0.2, 'curve': 4},
 {'age': 45, 'amount': 0.15, 'curve': 4},
 {'age': 55, 'amount': 0.15, 'curve': 4},
 {'age': 65, 'amount': 0.2, 'curve': 4},
 {'age': 75, 'amount': 0.15, 'curve': 4},
 {'age': 85, 'amount': 0.15, 'curve': 4},
 {'age': 95, 'amount': 0.2, 'curve': 4},
 {'age': 105, 'amount': 0.15, 'curve': 4},
 {'age': 115, 'amount': 0.15, 'curve': 4},
 {'age': 125, 'amount': 0.2, 'curve': 4},
 {'age': 135, 'amount': 0.15, 'curve': 4},
 {'age': 145, 'amount': 1.2, 'curve': 5},
 {'age': 79, 'amount': 4.0, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x06 0x19 0x04 0x08 0x23 0x04    \,....#.
    0008   0x06 0x2d 0x04 0x06 0x37 0x04 0x08 0x41    .-..7..A
    0010   0x04 0x06 0x4b 0x04 0x06 0x55 0x04 0x08    ..K..U..
    0018   0x5f 0x04 0x06 0x69 0x04 0x06 0x73 0x04    _..i..s.
    0020   0x08 0x7d 0x04 0x06 0x87 0x04 0x30 0x91    .}....0.
    0028   0x05 0xa0 0x4f 0x14                        ..O.
    decimal
             92   44    6   25    4    8   35    4
              6   45    4    6   55    4    8   65
              4    6   75    4    6   85    4    8
             95    4    6  105    4    6  115    4
              8  125    4    6  135    4   48  145
              5  160   79   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2015-02-19T01:01:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 0,
 'programmed': 3.6,
 'type': 'normal',
 'unabsorbed': 3.9}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x9c 0x00    ........
    decimal
              1    0  144    0  144    0  156    0
    datetime (2015-02-19T01:01:41)
    0000   0x29 0x81 0x41 0x73 0x0f                   ).As.
    body (0)

#### RECORD 26 BasalProfileStart 2015-02-19T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-19T04:00:00)
    0000   0x00 0x80 0x04 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 27 Ian0B 2015-02-19T04:08:49 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-19T04:08:49)
    0000   0x31 0x88 0x24 0xb3 0x0f                   1.$..
    body (0)

#### RECORD 28 Bolus 2015-02-19T04:21:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x14 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   20    0
    datetime (2015-02-19T04:21:33)
    0000   0x21 0x95 0x44 0x73 0x0f                   !.Ds.
    body (0)

#### RECORD 29 Ian0B 2015-02-19T04:25:23 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-19T04:25:23)
    0000   0x17 0x99 0x24 0xb3 0x0f                   ..$..
    body (0)

#### RECORD 30 Bolus 2015-02-19T06:31:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x20 0x00    ..(.(. .
    decimal
              1    0   40    0   40    0   32    0
    datetime (2015-02-19T06:31:17)
    0000   0x11 0x9f 0x46 0x73 0x0f                   ..Fs.
    body (0)

#### RECORD 31 Ian0B 2015-02-19T06:44:55 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-19T06:44:55)
    0000   0x37 0xac 0x26 0xb3 0x0f                   7.&..
    body (0)

#### RECORD 32 BolusWizard 2015-02-19T06:56:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 56,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-19T06:56:57)
    0000   0x39 0xb8 0x06 0x73 0x0f                   9..s.
    body (15)
    hex
    0000   0x38 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    8P.d(Z..
    0008   0xe0 0x00 0x00 0x00 0x00 0xe0 0x78         ......x
    decimal
             56   80    0  100   40   90    0    0
            224    0    0    0    0  224  120

#### RECORD 33 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.0, 'curve': 4},
 {'age': 160, 'amount': 2.0, 'curve': 4},
 {'age': 104, 'amount': 3.6, 'curve': 20},
 {'age': 124, 'amount': 0.15, 'curve': 20},
 {'age': 134, 'amount': 0.2, 'curve': 20},
 {'age': 144, 'amount': 0.15, 'curve': 20},
 {'age': 154, 'amount': 0.15, 'curve': 20},
 {'age': 164, 'amount': 0.2, 'curve': 20},
 {'age': 174, 'amount': 0.15, 'curve': 20},
 {'age': 184, 'amount': 0.15, 'curve': 20},
 {'age': 194, 'amount': 0.2, 'curve': 20},
 {'age': 204, 'amount': 0.15, 'curve': 20},
 {'age': 214, 'amount': 0.15, 'curve': 20}]
```
    op hex (41)
    0000   0x5c 0x29 0x28 0x1e 0x04 0x50 0xa0 0x04    \)(..P..
    0008   0x90 0x68 0x14 0x06 0x7c 0x14 0x08 0x86    .h..|...
    0010   0x14 0x06 0x90 0x14 0x06 0x9a 0x14 0x08    ........
    0018   0xa4 0x14 0x06 0xae 0x14 0x06 0xb8 0x14    ........
    0020   0x08 0xc2 0x14 0x06 0xcc 0x14 0x06 0xd6    ........
    0028   0x14                                       .
    decimal
             92   41   40   30    4   80  160    4
            144  104   20    6  124   20    8  134
             20    6  144   20    6  154   20    8
            164   20    6  174   20    6  184   20
              8  194   20    6  204   20    6  214
             20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2015-02-19T06:56:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3,
 'duration': 0,
 'programmed': 5.6,
 'type': 'normal',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0xe0 0x00 0x0c 0x00 0x3c 0x00    ......<.
    decimal
              1    0  224    0   12    0   60    0
    datetime (2015-02-19T06:56:57)
    0000   0x39 0xb8 0x46 0x73 0x0f                   9.Fs.
    body (0)

#### RECORD 35 NoDelivery 2015-02-19T06:57:09 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-19T06:57:09)
    0000   0x09 0xb9 0x46 0x53 0x0f                   ..FS.
    body (0)

#### RECORD 36 ClearAlarm 2015-02-19T06:57:18 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-19T06:57:18)
    0000   0x12 0xb9 0x06 0x13 0x0f                   .....
    body (0)

#### RECORD 37 Rewind 2015-02-19T06:57:35 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-19T06:57:35)
    0000   0x23 0xb9 0x06 0x13 0x0f                   #....
    body (0)

#### RECORD 38 Ian0B 2015-02-19T07:10:16 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-19T07:10:16)
    0000   0x10 0x8a 0x27 0xb3 0x0f                   ..'..
    body (0)

#### RECORD 39 Prime 2015-02-19T07:17:58 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 7.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x4c                   ....L
    decimal
              3    0    0    0   76
    datetime (2015-02-19T07:17:58)
    0000   0x3a 0x91 0x27 0x13 0x0f                   :.'..
    body (0)

#### RECORD 40 BasalProfileStart 2015-02-19T07:18:36 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-19T07:18:36)
    0000   0x24 0x92 0x07 0x13 0x0f                   $....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 41 Prime 2015-02-19T07:18:22 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-19T07:18:22)
    0000   0x16 0x92 0x07 0x13 0x0f                   .....
    body (0)

#### RECORD 42 BolusWizard 2015-02-19T07:18:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 4.2,
 'carb_input': 42,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-19T07:18:54)
    0000   0x36 0x92 0x07 0x73 0x0f                   6..s.
    body (15)
    hex
    0000   0x2a 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    *P.d(Z..
    0008   0xa8 0x00 0x00 0x00 0x00 0xa8 0x78         ......x
    decimal
             42   80    0  100   40   90    0    0
            168    0    0    0    0  168  120

#### RECORD 43 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 0.3, 'curve': 4},
 {'age': 52, 'amount': 1.0, 'curve': 4},
 {'age': 182, 'amount': 2.0, 'curve': 4},
 {'age': 126, 'amount': 3.6, 'curve': 20},
 {'age': 146, 'amount': 0.15, 'curve': 20},
 {'age': 156, 'amount': 0.2, 'curve': 20},
 {'age': 166, 'amount': 0.15, 'curve': 20},
 {'age': 176, 'amount': 0.15, 'curve': 20},
 {'age': 186, 'amount': 0.2, 'curve': 20},
 {'age': 196, 'amount': 0.15, 'curve': 20},
 {'age': 206, 'amount': 0.15, 'curve': 20},
 {'age': 216, 'amount': 0.2, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x0c 0x16 0x04 0x28 0x34 0x04    \&...(4.
    0008   0x50 0xb6 0x04 0x90 0x7e 0x14 0x06 0x92    P...~...
    0010   0x14 0x08 0x9c 0x14 0x06 0xa6 0x14 0x06    ........
    0018   0xb0 0x14 0x08 0xba 0x14 0x06 0xc4 0x14    ........
    0020   0x06 0xce 0x14 0x08 0xd8 0x14              ......
    decimal
             92   38   12   22    4   40   52    4
             80  182    4  144  126   20    6  146
             20    8  156   20    6  166   20    6
            176   20    8  186   20    6  196   20
              6  206   20    8  216   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2015-02-19T07:18:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x3c 0x00    ......<.
    decimal
              1    0  200    0  200    0   60    0
    datetime (2015-02-19T07:18:54)
    0000   0x36 0x92 0x47 0x73 0x0f                   6.Gs.
    body (0)

#### RECORD 45 PumpSuspend 2015-02-19T07:24:26 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-19T07:24:26)
    0000   0x1a 0x98 0x07 0x13 0x0f                   .....
    body (0)

#### RECORD 46 BasalProfileStart 2015-02-19T07:47:33 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-19T07:47:33)
    0000   0x21 0xaf 0x07 0x13 0x0f                   !....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 47 PumpResume 2015-02-19T07:47:34 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-19T07:47:34)
    0000   0x22 0xaf 0x07 0x13 0x0f                   "....
    body (0)

#### RECORD 48 Ian0B 2015-02-19T08:38:47 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x10                             .e.
    decimal
             11  101   16
    datetime (2015-02-19T08:38:47)
    0000   0x2f 0xa6 0x28 0xb3 0x8f                   /.(..
    body (0)

#### RECORD 49 Bolus 2015-02-19T08:43:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 3.9}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x9c 0x00    ........
    decimal
              1    0  180    0  180    0  156    0
    datetime (2015-02-19T08:43:37)
    0000   0x25 0xab 0x48 0x73 0x0f                   %.Hs.
    body (0)

#### RECORD 50 Ian0B 2015-02-19T09:40:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-19T09:40:00)
    0000   0x00 0xa8 0x29 0xb3 0x0f                   ..)..
    body (0)

#### RECORD 51 BasalProfileStart 2015-02-19T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-19T10:00:00)
    0000   0x00 0x80 0x0a 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 52 Ian0B 2015-02-19T10:08:49 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-19T10:08:49)
    0000   0x31 0x88 0x2a 0xb3 0x0f                   1.*..
    body (0)

#### RECORD 53 Ian0B 2015-02-19T10:40:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-19T10:40:00)
    0000   0x00 0xa8 0x2a 0xb3 0x0f                   ..*..
    body (0)

#### RECORD 54 CalBGForPH 2015-02-19T10:40:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2015-02-19T10:40:52)
    0000   0x34 0xa8 0x2a 0x73 0x0f                   4.*s.
    body (0)

#### RECORD 55 Ian3F 2015-02-19T10:40:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-02-19T10:40:52)
    0000   0x34 0xa8 0xea 0x73 0x0f                   4..s.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 56 BolusWizard 2015-02-19T10:41:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 167,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.6}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2015-02-19T10:41:13)
    0000   0x0d 0xa9 0x0a 0x73 0x0f                   ...s.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x2c 0x00    .P.d(Z,.
    0008   0x00 0x00 0x00 0x68 0x00 0x00 0x78         ...h..x
    decimal
              0   80    0  100   40   90   44    0
              0    0    0  104    0    0  120

#### RECORD 57 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 115, 'amount': 1.0, 'curve': 4},
 {'age': 125, 'amount': 3.5, 'curve': 4},
 {'age': 205, 'amount': 5.0, 'curve': 4},
 {'age': 225, 'amount': 0.3, 'curve': 4},
 {'age': 255, 'amount': 1.0, 'curve': 4},
 {'age': 129, 'amount': 2.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x28 0x73 0x04 0x8c 0x7d 0x04    \.(s..}.
    0008   0xc8 0xcd 0x04 0x0c 0xe1 0x04 0x28 0xff    ......(.
    0010   0x04 0x50 0x81 0x14                        .P..
    decimal
             92   20   40  115    4  140  125    4
            200  205    4   12  225    4   40  255
              4   80  129   20
    datetime (unknown)

    body (0)

#### RECORD 58 Ian0B 2015-02-19T10:54:06 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-19T10:54:06)
    0000   0x06 0xb6 0x2a 0xb3 0x0f                   ..*..
    body (0)

#### RECORD 59 Ian0B 2015-02-19T10:59:28 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-19T10:59:28)
    0000   0x1c 0xbb 0x2a 0xb3 0x0f                   ..*..
    body (0)

#### RECORD 60 BasalProfileStart 2015-02-19T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-19T12:00:00)
    0000   0x00 0x80 0x0c 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 61 Ian0B 2015-02-19T12:19:28 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-02-19T12:19:28)
    0000   0x1c 0x93 0x2c 0xb3 0x0f                   ..,..
    body (0)

#### RECORD 62 CalBGForPH 2015-02-19T12:20:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2015-02-19T12:20:48)
    0000   0x30 0x94 0x2c 0x73 0x0f                   0.,s.
    body (0)

#### RECORD 63 Ian3F 2015-02-19T12:20:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-19T12:20:48)
    0000   0x30 0x94 0x0c 0x73 0x0f                   0..s.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 64 BolusWizard 2015-02-19T12:21:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 184,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 1.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2015-02-19T12:21:06)
    0000   0x06 0x95 0x0c 0x13 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x40 0x00    .P.P(Z@.
    0008   0x00 0x00 0x00 0x10 0x00 0x30 0x78         .....0x
    decimal
              0   80    0   80   40   90   64    0
              0    0    0   16    0   48  120

#### RECORD 65 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 215, 'amount': 1.0, 'curve': 4},
 {'age': 225, 'amount': 3.5, 'curve': 4},
 {'age': 49, 'amount': 5.0, 'curve': 20},
 {'age': 69, 'amount': 0.3, 'curve': 20},
 {'age': 99, 'amount': 1.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0xd7 0x04 0x8c 0xe1 0x04    \.(.....
    0008   0xc8 0x31 0x14 0x0c 0x45 0x14 0x28 0x63    .1..E.(c
    0010   0x14                                       .
    decimal
             92   17   40  215    4  140  225    4
            200   49   20   12   69   20   40   99
             20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2015-02-19T12:21:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2,
 'duration': 0,
 'programmed': 1.2,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x10 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   16    0
    datetime (2015-02-19T12:21:06)
    0000   0x06 0x95 0x4c 0x13 0x0f                   ..L..
    body (0)

#### RECORD 67 Ian0B 2015-02-19T12:25:23 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-19T12:25:23)
    0000   0x17 0x99 0x2c 0xb3 0x0f                   ..,..
    body (0)

#### RECORD 68 Ian0B 2015-02-19T12:38:47 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-19T12:38:47)
    0000   0x2f 0xa6 0x2c 0xb3 0x0f                   /.,..
    body (0)

#### RECORD 69 BolusWizard 2015-02-19T13:15:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 5.2,
 'carb_input': 42,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-19T13:15:39)
    0000   0x27 0x8f 0x0d 0x73 0x0f                   '..s.
    body (15)
    hex
    0000   0x2a 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    *P.P(Z..
    0008   0xd0 0x00 0x00 0x00 0x00 0xd0 0x78         ......x
    decimal
             42   80    0   80   40   90    0    0
            208    0    0    0    0  208  120

#### RECORD 70 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 1.2, 'curve': 4},
 {'age': 13, 'amount': 1.0, 'curve': 20},
 {'age': 23, 'amount': 3.5, 'curve': 20},
 {'age': 103, 'amount': 5.0, 'curve': 20},
 {'age': 123, 'amount': 0.3, 'curve': 20},
 {'age': 153, 'amount': 1.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x30 0x3b 0x04 0x28 0x0d 0x14    \.0;.(..
    0008   0x8c 0x17 0x14 0xc8 0x67 0x14 0x0c 0x7b    ....g..{
    0010   0x14 0x28 0x99 0x14                        .(..
    decimal
             92   20   48   59    4   40   13   20
            140   23   20  200  103   20   12  123
             20   40  153   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2015-02-19T13:17:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6,
 'duration': 30,
 'programmed': 2.6,
 'type': 'square',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x28 0x01    ..h.h.(.
    decimal
              1    0  104    0  104    0   40    1
    datetime (2015-02-19T13:17:23)
    0000   0x17 0x91 0xad 0x73 0x0f                   ...s.
    body (0)

#### RECORD 72 Bolus 2015-02-19T13:15:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6,
 'duration': 0,
 'programmed': 2.6,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x28 0x00    ..h.h.(.
    decimal
              1    0  104    0  104    0   40    0
    datetime (2015-02-19T13:15:39)
    0000   0x27 0x8f 0x8d 0x73 0x0f                   '..s.
    body (0)

#### RECORD 73 Ian0B 2015-02-19T14:08:48 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xc9                             .e.
    decimal
             11  101  201
    datetime (2015-02-19T14:08:48)
    0000   0x30 0x88 0x2e 0xb3 0x0f                   0....
    body (0)

#### RECORD 74 BasalProfileStart 2015-02-19T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-19T15:00:00)
    0000   0x00 0x80 0x0f 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 75 Ian0B 2015-02-19T15:55:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-19T15:55:03)
    0000   0x03 0xb7 0x2f 0xb3 0x0f                   ../..
    body (0)

#### RECORD 76 Ian0B 2015-02-19T15:58:46 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-19T15:58:46)
    0000   0x2e 0xba 0x2f 0xb3 0x0f                   ../..
    body (0)

#### RECORD 77 Ian0B 2015-02-19T17:25:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-19T17:25:00)
    0000   0x00 0x99 0x31 0xb3 0x0f                   ..1..
    body (0)

#### RECORD 78 Ian0B 2015-02-19T17:28:48 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xeb                             .e.
    decimal
             11  101  235
    datetime (2015-02-19T17:28:48)
    0000   0x30 0x9c 0x31 0xb3 0x0f                   0.1..
    body (0)

#### RECORD 79 CalBGForPH 2015-02-19T17:48:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2015-02-19T17:48:45)
    0000   0x2d 0xb0 0x31 0x73 0x0f                   -.1s.
    body (0)

`end analysis/736868/logs/ReadHistoryData-page-25.data: 80 records`
