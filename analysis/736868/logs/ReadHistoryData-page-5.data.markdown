## START analysis/736868/logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x66 0xd0                                  f.
##### DEBUG DECIMAL
            102  208
#### RECORD 0 Sara6E 2015-03-21T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-21T00:00:00)
    0000   0x34 0x8f                                  4.
    body (49)
    hex
    0000   0x05 0x10 0xe9 0x8f 0x43 0x02 0x00 0x00    ....C...
    0008   0x07 0xf1 0x03 0x17 0x27 0x04 0xda 0x3d    ....'..=
    0010   0x00 0xa5 0x02 0xfe 0x00 0x88 0x00 0x00    ........
    0018   0x01 0x54 0x03 0x01 0x00 0x06 0x00 0xa5    .T......
    0020   0x1f 0x3e 0x06 0x0e 0x2f 0x04 0x01 0x00    .>../...
    0028   0x00 0x03 0x07 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  233  143   67    2    0    0
              7  241    3   23   39    4  218   61
              0  165    2  254    0  136    0    0
              1   84    3    1    0    6    0  165
             31   62    6   14   47    4    1    0
              0    3    7    1    0    0    0    0
              0

#### RECORD 1 BolusWizard 2015-03-21T00:03:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-21T00:03:25)
    0000   0x19 0xc3 0x00 0x75 0x0f                   ...u.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 2 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 3.4, 'curve': 4},
 {'age': 184, 'amount': 1.0, 'curve': 4},
 {'age': 194, 'amount': 2.4, 'curve': 4},
 {'age': 204, 'amount': 0.1, 'curve': 4},
 {'age': 254, 'amount': 0.05, 'curve': 4},
 {'age': 8, 'amount': 0.4, 'curve': 20},
 {'age': 18, 'amount': 0.4, 'curve': 20},
 {'age': 28, 'amount': 0.4, 'curve': 20},
 {'age': 38, 'amount': 0.4, 'curve': 20},
 {'age': 48, 'amount': 0.4, 'curve': 20},
 {'age': 58, 'amount': 0.4, 'curve': 20},
 {'age': 68, 'amount': 0.4, 'curve': 20},
 {'age': 78, 'amount': 0.4, 'curve': 20},
 {'age': 88, 'amount': 1.85, 'curve': 20},
 {'age': 98, 'amount': 3.9, 'curve': 20},
 {'age': 158, 'amount': 1.0, 'curve': 20}]
```
    op hex (50)
    0000   0x5c 0x32 0x88 0x40 0x04 0x28 0xb8 0x04    \2.@.(..
    0008   0x60 0xc2 0x04 0x04 0xcc 0x04 0x02 0xfe    `.......
    0010   0x04 0x10 0x08 0x14 0x10 0x12 0x14 0x10    ........
    0018   0x1c 0x14 0x10 0x26 0x14 0x10 0x30 0x14    ...&..0.
    0020   0x10 0x3a 0x14 0x10 0x44 0x14 0x10 0x4e    .:..D..N
    0028   0x14 0x4a 0x58 0x14 0x9c 0x62 0x14 0x28    .JX..b.(
    0030   0x9e 0x14                                  ..
    decimal
             92   50  136   64    4   40  184    4
             96  194    4    4  204    4    2  254
              4   16    8   20   16   18   20   16
             28   20   16   38   20   16   48   20
             16   58   20   16   68   20   16   78
             20   74   88   20  156   98   20   40
            158   20
    datetime (unknown)

    body (0)

#### RECORD 3 LowReservoir 2015-03-21T00:03:29 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-21T00:03:29)
    0000   0x1d 0xc3 0x00 0x15 0x0f                   .....
    body (0)

#### RECORD 4 Bolus 2015-03-21T00:03:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.3}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x84 0x00    ........
    decimal
              1    0  160    0  160    0  132    0
    datetime (2015-03-21T00:03:25)
    0000   0x19 0xc3 0x40 0x75 0x0f                   ..@u.
    body (0)

#### RECORD 5 Ian0B 2015-03-21T00:45:53 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-03-21T00:45:53)
    0000   0x35 0xed 0x20 0xb5 0x0f                   5. ..
    body (0)

#### RECORD 6 Ian0B 2015-03-21T02:15:44 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xe7                             .e.
    decimal
             11  101  231
    datetime (2015-03-21T02:15:44)
    0000   0x2c 0xcf 0x22 0xb5 0x0f                   ,."..
    body (0)

#### RECORD 7 Ian0B 2015-03-21T03:44:55 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x66                             .ef
    decimal
             11  101  102
    datetime (2015-03-21T03:44:55)
    0000   0x37 0xec 0x23 0xb5 0x8f                   7.#..
    body (0)

#### RECORD 8 BasalProfileStart 2015-03-21T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-21T04:00:00)
    0000   0x00 0xc0 0x04 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 9 Ian0B 2015-03-21T05:16:12 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x57                             .eW
    decimal
             11  101   87
    datetime (2015-03-21T05:16:12)
    0000   0x0c 0xd0 0x25 0xb5 0x8f                   ..%..
    body (0)

#### RECORD 10 Bolus 2015-03-21T05:29:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1,
 'duration': 0,
 'programmed': 0.1,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x04 0x01 0x04 0x00 0x00 0x00    ........
    decimal
              1    1    4    1    4    0    0    0
    datetime (2015-03-21T05:29:37)
    0000   0x25 0xdd 0x45 0x75 0x0f                   %.Eu.
    body (0)

#### RECORD 11 Ian0B 2015-03-21T06:45:53 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xbe                             .e.
    decimal
             11  101  190
    datetime (2015-03-21T06:45:53)
    0000   0x35 0xed 0x26 0xb5 0x0f                   5.&..
    body (0)

#### RECORD 12 BasalProfileStart 2015-03-21T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-21T07:00:00)
    0000   0x00 0xc0 0x07 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 13 BasalProfileStart 2015-03-21T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-21T10:00:00)
    0000   0x00 0xc0 0x0a 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 14 Ian0B 2015-03-21T10:00:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-21T10:00:00)
    0000   0x00 0xc0 0x2a 0xb5 0x0f                   ..*..
    body (0)

#### RECORD 15 Ian0B 2015-03-21T10:05:53 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-21T10:05:53)
    0000   0x35 0xc5 0x2a 0xb5 0x0f                   5.*..
    body (0)

#### RECORD 16 BolusWizard 2015-03-21T10:06:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 3.8,
 'carb_input': 38,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-21T10:06:59)
    0000   0x3b 0xc6 0x0a 0x75 0x0f                   ;..u.
    body (15)
    hex
    0000   0x26 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    &P.d(Z..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x78         ......x
    decimal
             38   80    0  100   40   90    0    0
            152    0    0    0    0  152  120

#### RECORD 17 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 0.1, 'curve': 21}]
```
    op hex (5)
    0000   0x5c 0x05 0x04 0x15 0x15                   \....
    decimal
             92    5    4   21   21
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2015-03-21T10:06:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 3.8,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x64 0x00 0x00 0x00    ....d...
    decimal
              1    0  152    0  100    0    0    0
    datetime (2015-03-21T10:06:59)
    0000   0x3b 0xc6 0x4a 0x75 0x0f                   ;.Ju.
    body (0)

#### RECORD 19 NoDelivery 2015-03-21T10:08:41 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-21T10:08:41)
    0000   0x29 0xc8 0x4a 0x55 0x0f                   ).JU.
    body (0)

#### RECORD 20 ClearAlarm 2015-03-21T10:09:55 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-21T10:09:55)
    0000   0x37 0xc9 0x0a 0x15 0x0f                   7....
    body (0)

#### RECORD 21 Rewind 2015-03-21T10:09:59 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-21T10:09:59)
    0000   0x3b 0xc9 0x0a 0x15 0x0f                   ;....
    body (0)

#### RECORD 22 Ian0B 2015-03-21T10:15:44 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xbb                             .e.
    decimal
             11  101  187
    datetime (2015-03-21T10:15:44)
    0000   0x2c 0xcf 0x2a 0xb5 0x0f                   ,.*..
    body (0)

#### RECORD 23 Prime 2015-03-21T10:19:21 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 7.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x47                   ....G
    decimal
              3    0    0    0   71
    datetime (2015-03-21T10:19:21)
    0000   0x15 0xd3 0x2a 0x15 0x0f                   ..*..
    body (0)

#### RECORD 24 BasalProfileStart 2015-03-21T10:20:09 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-21T10:20:09)
    0000   0x09 0xd4 0x0a 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 25 Prime 2015-03-21T10:19:55 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-21T10:19:55)
    0000   0x37 0xd3 0x0a 0x15 0x0f                   7....
    body (0)

#### RECORD 26 Bolus 2015-03-21T10:20:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 2.5}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x64 0x00    ..(.(.d.
    decimal
              1    0   40    0   40    0  100    0
    datetime (2015-03-21T10:20:45)
    0000   0x2d 0xd4 0x4a 0x75 0x0f                   -.Ju.
    body (0)

#### RECORD 27 PumpSuspend 2015-03-21T10:21:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-21T10:21:31)
    0000   0x1f 0xd5 0x0a 0x15 0x0f                   .....
    body (0)

#### RECORD 28 BasalProfileStart 2015-03-21T10:43:36 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-21T10:43:36)
    0000   0x24 0xeb 0x0a 0x15 0x0f                   $....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 29 PumpResume 2015-03-21T10:43:36 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-21T10:43:36)
    0000   0x24 0xeb 0x0a 0x15 0x0f                   $....
    body (0)

#### RECORD 30 CalBGForPH 2015-03-21T10:57:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 278}
```
    op hex (2)
    0000   0x0a 0x16                                  ..
    decimal
             10   22
    datetime (2015-03-21T10:57:57)
    0000   0x39 0xf9 0x2a 0x75 0x8f                   9.*u.
    body (0)

#### RECORD 31 Ian3F 2015-03-21T10:57:57 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2015-03-21T10:57:57)
    0000   0x39 0xf9 0xca 0x75 0x0f                   9..u.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 32 BolusWizard 2015-03-21T10:58:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 278,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 4.9,
 'carb_input': 40,
 'carb_ratio': 12.0,
 'correction_estimate': -2.5,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 3.0}
```
    op hex (2)
    0000   0x5b 0x16                                  [.
    decimal
             91   22
    datetime (2015-03-21T10:58:17)
    0000   0x11 0xfa 0x0a 0x15 0x0f                   .....
    body (15)
    hex
    0000   0x28 0x51 0x00 0x64 0x28 0x5a 0x9c 0x00    (Q.d(Z..
    0008   0xa0 0x00 0x00 0x78 0x00 0xc4 0x78         ...x..x
    decimal
             40   81    0  100   40   90  156    0
            160    0    0  120    0  196  120

#### RECORD 33 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 1.0, 'curve': 4},
 {'age': 59, 'amount': 2.5, 'curve': 4},
 {'age': 73, 'amount': 0.1, 'curve': 21}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x27 0x04 0x64 0x3b 0x04    \.('.d;.
    0008   0x04 0x49 0x15                             .I.
    decimal
             92   11   40   39    4  100   59    4
              4   73   21
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2015-03-21T10:58:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9,
 'duration': 0,
 'programmed': 4.9,
 'type': 'normal',
 'unabsorbed': 3.0}
```
    op hex (8)
    0000   0x01 0x00 0xc4 0x00 0xc4 0x00 0x78 0x00    ......x.
    decimal
              1    0  196    0  196    0  120    0
    datetime (2015-03-21T10:58:18)
    0000   0x12 0xfa 0x4a 0x15 0x0f                   ..J..
    body (0)

#### RECORD 35 Ian0B 2015-03-21T11:44:55 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x38                             .e8
    decimal
             11  101   56
    datetime (2015-03-21T11:44:55)
    0000   0x37 0xec 0x2b 0xb5 0x8f                   7.+..
    body (0)

#### RECORD 36 Bolus 2015-03-21T11:45:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x01 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    1    0    0
    datetime (2015-03-21T11:45:15)
    0000   0x0f 0xed 0x4b 0x75 0x0f                   ..Ku.
    body (0)

#### RECORD 37 BasalProfileStart 2015-03-21T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-21T12:00:00)
    0000   0x00 0xc0 0x0c 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 38 Bolus 2015-03-21T12:17:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 5.8}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xe8 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  232    0
    datetime (2015-03-21T12:17:48)
    0000   0x30 0xd1 0x4c 0x75 0x0f                   0.Lu.
    body (0)

#### RECORD 39 Ian0B 2015-03-21T13:16:12 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xff                             .e.
    decimal
             11  101  255
    datetime (2015-03-21T13:16:12)
    0000   0x0c 0xd0 0x2d 0xb5 0x0f                   ..-..
    body (0)

#### RECORD 40 Bolus 2015-03-21T13:16:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x94 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  148    0
    datetime (2015-03-21T13:16:31)
    0000   0x1f 0xd0 0x4d 0x75 0x0f                   ..Mu.
    body (0)

#### RECORD 41 Ian0B 2015-03-21T14:45:53 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xda                             .e.
    decimal
             11  101  218
    datetime (2015-03-21T14:45:53)
    0000   0x35 0xed 0x2e 0xb5 0x0f                   5....
    body (0)

#### RECORD 42 BasalProfileStart 2015-03-21T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-21T15:00:00)
    0000   0x00 0xc0 0x0f 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 43 BolusWizard 2015-03-21T15:15:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 66,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-21T15:15:20)
    0000   0x14 0xcf 0x0f 0x75 0x0f                   ...u.
    body (15)
    hex
    0000   0x42 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    BP.P(Z..
    0008   0x48 0x00 0x00 0x00 0x01 0x48 0x78         H....Hx
    decimal
             66   80    0   80   40   90    0    1
             72    0    0    0    1   72  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.5, 'curve': 4},
 {'age': 186, 'amount': 1.0, 'curve': 4},
 {'age': 216, 'amount': 1.0, 'curve': 4},
 {'age': 0, 'amount': 3.85, 'curve': 20},
 {'age': 10, 'amount': 1.05, 'curve': 20},
 {'age': 40, 'amount': 1.0, 'curve': 20},
 {'age': 60, 'amount': 2.5, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x3c 0x7e 0x04 0x28 0xba 0x04    \.<~.(..
    0008   0x28 0xd8 0x04 0x9a 0x00 0x14 0x2a 0x0a    (.....*.
    0010   0x14 0x28 0x28 0x14 0x64 0x3c 0x14         .((.d<.
    decimal
             92   23   60  126    4   40  186    4
             40  216    4  154    0   20   42   10
             20   40   40   20  100   60   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-03-21T15:18:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 120,
 'programmed': 3.7,
 'type': 'square',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x24 0x04    ......$.
    decimal
              1    0  148    0  148    0   36    4
    datetime (2015-03-21T15:18:21)
    0000   0x15 0xd2 0xaf 0x75 0x0f                   ...u.
    body (0)

#### RECORD 46 Bolus 2015-03-21T15:15:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x24 0x00    ......$.
    decimal
              1    0  180    0  180    0   36    0
    datetime (2015-03-21T15:15:21)
    0000   0x15 0xcf 0x8f 0x75 0x0f                   ...u.
    body (0)

#### RECORD 47 Ian0B 2015-03-21T16:15:44 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xcc                             .e.
    decimal
             11  101  204
    datetime (2015-03-21T16:15:44)
    0000   0x2c 0xcf 0x30 0xb5 0x0f                   ,.0..
    body (0)

#### RECORD 48 Ian0B 2015-03-21T17:56:11 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-21T17:56:11)
    0000   0x0b 0xf8 0x31 0xb5 0x0f                   ..1..
    body (0)

#### RECORD 49 Ian0B 2015-03-21T18:05:52 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-03-21T18:05:52)
    0000   0x34 0xc5 0x32 0xb5 0x0f                   4.2..
    body (0)

#### RECORD 50 PumpSuspend 2015-03-21T18:35:28 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-21T18:35:28)
    0000   0x1c 0xe3 0x12 0x15 0x0f                   .....
    body (0)

#### RECORD 51 Ian0B 2015-03-21T18:36:11 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-03-21T18:36:11)
    0000   0x0b 0xe4 0x32 0xb5 0x0f                   ..2..
    body (0)

#### RECORD 52 BasalProfileStart 2015-03-21T19:13:18 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-21T19:13:18)
    0000   0x12 0xcd 0x13 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 53 PumpResume 2015-03-21T19:13:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-21T19:13:18)
    0000   0x12 0xcd 0x13 0x15 0x0f                   .....
    body (0)

#### RECORD 54 BolusWizard 2015-03-21T19:13:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 60,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 30,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-21T19:13:31)
    0000   0x1f 0xcd 0x13 0x75 0x0f                   ...u.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             30   80    0   60   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 55 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 0.3, 'curve': 4},
 {'age': 134, 'amount': 0.3, 'curve': 4},
 {'age': 144, 'amount': 0.3, 'curve': 4},
 {'age': 154, 'amount': 0.3, 'curve': 4},
 {'age': 164, 'amount': 0.3, 'curve': 4},
 {'age': 174, 'amount': 0.35, 'curve': 4},
 {'age': 184, 'amount': 0.3, 'curve': 4},
 {'age': 194, 'amount': 0.3, 'curve': 4},
 {'age': 204, 'amount': 0.3, 'curve': 4},
 {'age': 214, 'amount': 0.3, 'curve': 4},
 {'age': 224, 'amount': 0.3, 'curve': 4},
 {'age': 234, 'amount': 0.35, 'curve': 4},
 {'age': 244, 'amount': 4.5, 'curve': 4},
 {'age': 108, 'amount': 1.5, 'curve': 20},
 {'age': 168, 'amount': 1.0, 'curve': 20},
 {'age': 198, 'amount': 1.0, 'curve': 20}]
```
    op hex (50)
    0000   0x5c 0x32 0x0c 0x7c 0x04 0x0c 0x86 0x04    \2.|....
    0008   0x0c 0x90 0x04 0x0c 0x9a 0x04 0x0c 0xa4    ........
    0010   0x04 0x0e 0xae 0x04 0x0c 0xb8 0x04 0x0c    ........
    0018   0xc2 0x04 0x0c 0xcc 0x04 0x0c 0xd6 0x04    ........
    0020   0x0c 0xe0 0x04 0x0e 0xea 0x04 0xb4 0xf4    ........
    0028   0x04 0x3c 0x6c 0x14 0x28 0xa8 0x14 0x28    .<l.(..(
    0030   0xc6 0x14                                  ..
    decimal
             92   50   12  124    4   12  134    4
             12  144    4   12  154    4   12  164
              4   14  174    4   12  184    4   12
            194    4   12  204    4   12  214    4
             12  224    4   14  234    4  180  244
              4   60  108   20   40  168   20   40
            198   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2015-03-21T19:13:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x20 0x00    ...... .
    decimal
              1    0  200    0  200    0   32    0
    datetime (2015-03-21T19:13:31)
    0000   0x1f 0xcd 0x53 0x75 0x0f                   ..Su.
    body (0)

#### RECORD 57 Ian0B 2015-03-21T19:50:16 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-21T19:50:16)
    0000   0x10 0xf2 0x33 0xb5 0x0f                   ..3..
    body (0)

#### RECORD 58 Ian0B 2015-03-21T20:05:52 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-03-21T20:05:52)
    0000   0x34 0xc5 0x34 0xb5 0x0f                   4.4..
    body (0)

#### RECORD 59 Ian0B 2015-03-21T21:35:43 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-03-21T21:35:43)
    0000   0x2b 0xe3 0x35 0xb5 0x0f                   +.5..
    body (0)

#### RECORD 60 BolusWizard 2015-03-21T21:36:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 60,
 'bg_target_low': 90,
 'bolus_estimate': 1.9,
 'carb_input': 50,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-21T21:36:15)
    0000   0x0f 0xe4 0x15 0x75 0x0f                   ...u.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    2P.<(Z..
    0008   0x4c 0x00 0x00 0x00 0x01 0x4c 0x78         L....Lx
    decimal
             50   80    0   60   40   90    0    1
             76    0    0    0    1   76  120

#### RECORD 61 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 147, 'amount': 5.0, 'curve': 4},
 {'age': 11, 'amount': 0.3, 'curve': 20},
 {'age': 21, 'amount': 0.3, 'curve': 20},
 {'age': 31, 'amount': 0.3, 'curve': 20},
 {'age': 41, 'amount': 0.3, 'curve': 20},
 {'age': 51, 'amount': 0.3, 'curve': 20},
 {'age': 61, 'amount': 0.35, 'curve': 20},
 {'age': 71, 'amount': 0.3, 'curve': 20},
 {'age': 81, 'amount': 0.3, 'curve': 20},
 {'age': 91, 'amount': 0.3, 'curve': 20},
 {'age': 101, 'amount': 0.3, 'curve': 20},
 {'age': 111, 'amount': 0.3, 'curve': 20},
 {'age': 121, 'amount': 0.35, 'curve': 20},
 {'age': 131, 'amount': 4.5, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0xc8 0x93 0x04 0x0c 0x0b 0x14    \,......
    0008   0x0c 0x15 0x14 0x0c 0x1f 0x14 0x0c 0x29    .......)
    0010   0x14 0x0c 0x33 0x14 0x0e 0x3d 0x14 0x0c    ..3..=..
    0018   0x47 0x14 0x0c 0x51 0x14 0x0c 0x5b 0x14    G..Q..[.
    0020   0x0c 0x65 0x14 0x0c 0x6f 0x14 0x0e 0x79    .e..o..y
    0028   0x14 0xb4 0x83 0x14                        ....
    decimal
             92   44  200  147    4   12   11   20
             12   21   20   12   31   20   12   41
             20   12   51   20   14   61   20   12
             71   20   12   81   20   12   91   20
             12  101   20   12  111   20   14  121
             20  180  131   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2015-03-21T21:39:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9,
 'duration': 90,
 'programmed': 2.9,
 'type': 'square',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x40 0x03    ..t.t.@.
    decimal
              1    0  116    0  116    0   64    3
    datetime (2015-03-21T21:39:00)
    0000   0x00 0xe7 0xb5 0x75 0x0f                   ...u.
    body (0)

#### RECORD 63 Bolus 2015-03-21T21:36:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1,
 'duration': 0,
 'programmed': 4.1,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x40 0x00    ......@.
    decimal
              1    0  164    0  164    0   64    0
    datetime (2015-03-21T21:36:15)
    0000   0x0f 0xe4 0x95 0x75 0x0f                   ...u.
    body (0)

#### RECORD 64 Ian0B 2015-03-21T21:58:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-21T21:58:00)
    0000   0x00 0xfa 0x35 0xb5 0x0f                   ..5..
    body (0)

#### RECORD 65 BasalProfileStart 2015-03-21T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-21T22:00:00)
    0000   0x00 0xc0 0x16 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 66 Ian0B 2015-03-21T22:58:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-21T22:58:00)
    0000   0x00 0xfa 0x36 0xb5 0x0f                   ..6..
    body (0)

#### RECORD 67 Ian0B 2015-03-21T23:28:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-21T23:28:00)
    0000   0x00 0xdc 0x37 0xb5 0x0f                   ..7..
    body (0)

#### RECORD 68 Ian0B 2015-03-21T23:58:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-21T23:58:00)
    0000   0x00 0xfa 0x37 0xb5 0x0f                   ..7..
    body (0)

#### RECORD 69 BasalProfileStart 2015-03-22T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-22T00:00:00)
    0000   0x00 0xc0 0x00 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 70 MResultTotals 2015-03-22T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0xb0                   .....
    decimal
              7    0    0    9  176
    datetime (2015-03-22T00:00:00)
    0000   0x35 0x8f                                  5.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 71 Sara6E 2015-03-22T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-22T00:00:00)
    0000   0x35 0x8f                                  5.
    body (49)
    hex
    0000   0x05 0x15 0x16 0x16 0x16 0x01 0x00 0x00    ........
    0008   0x09 0xb0 0x03 0x08 0x1f 0x06 0xa8 0x45    .......E
    0010   0x01 0x08 0x04 0x2c 0x00 0x00 0x00 0xc4    ...,....
    0018   0x01 0xb8 0x05 0x00 0x01 0x05 0x00 0xd2    ........
    0020   0x41 0x21 0x02 0x14 0x4f 0x02 0x01 0x00    A!..O...
    0028   0x00 0x02 0x0c 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   21   22   22   22    1    0    0
              9  176    3    8   31    6  168   69
              1    8    4   44    0    0    0  196
              1  184    5    0    1    5    0  210
             65   33    2   20   79    2    1    0
              0    2   12    1    0    0    0    0
              0

#### RECORD 72 Ian0B 2015-03-22T00:28:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-22T00:28:00)
    0000   0x00 0xdc 0x20 0xb6 0x0f                   .. ..
    body (0)

#### RECORD 73 CalBGForPH 2015-03-22T00:30:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2015-03-22T00:30:57)
    0000   0x39 0xde 0x20 0x76 0x0f                   9. v.
    body (0)

#### RECORD 74 Ian3F 2015-03-22T00:30:57 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2015-03-22T00:30:57)
    0000   0x39 0xde 0x60 0x76 0x0f                   9.`v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 75 Ian0B 2015-03-22T02:36:11 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-22T02:36:11)
    0000   0x0b 0xe4 0x22 0xb6 0x0f                   .."..
    body (0)

#### RECORD 76 Ian0B 2015-03-22T02:49:35 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-22T02:49:35)
    0000   0x23 0xf1 0x22 0xb6 0x0f                   #."..
    body (0)

#### RECORD 77 BasalProfileStart 2015-03-22T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-22T04:00:00)
    0000   0x00 0xc0 0x04 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

`end analysis/736868/logs/ReadHistoryData-page-5.data: 78 records`
