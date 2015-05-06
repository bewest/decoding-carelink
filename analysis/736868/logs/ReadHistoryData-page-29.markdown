## START analysis/736868/logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x71 0x1d                                  q.
##### DEBUG DECIMAL
            113   29
#### RECORD 0 BolusWizard 2015-02-13T20:53:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 245,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 3.1,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.7}
```
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2015-02-13T20:53:34)
    0000   0x22 0xb5 0x14 0x0d 0x0f                   "....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x7c 0x00    .P.<(Z|.
    0008   0x00 0x00 0x00 0x1c 0x00 0x60 0x78         .....`x
    decimal
              0   80    0   60   40   90  124    0
              0    0    0   28    0   96  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 0.05, 'curve': 4},
 {'age': 187, 'amount': 1.95, 'curve': 4},
 {'age': 207, 'amount': 0.3, 'curve': 4},
 {'age': 217, 'amount': 3.7, 'curve': 4},
 {'age': 151, 'amount': 0.1, 'curve': 20},
 {'age': 161, 'amount': 0.35, 'curve': 20},
 {'age': 171, 'amount': 0.3, 'curve': 20},
 {'age': 181, 'amount': 0.35, 'curve': 20},
 {'age': 191, 'amount': 0.35, 'curve': 20},
 {'age': 201, 'amount': 0.3, 'curve': 20},
 {'age': 211, 'amount': 0.35, 'curve': 20},
 {'age': 221, 'amount': 0.35, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x02 0xb1 0x04 0x4e 0xbb 0x04    \&...N..
    0008   0x0c 0xcf 0x04 0x94 0xd9 0x04 0x04 0x97    ........
    0010   0x14 0x0e 0xa1 0x14 0x0c 0xab 0x14 0x0e    ........
    0018   0xb5 0x14 0x0e 0xbf 0x14 0x0c 0xc9 0x14    ........
    0020   0x0e 0xd3 0x14 0x0e 0xdd 0x14              ......
    decimal
             92   38    2  177    4   78  187    4
             12  207    4  148  217    4    4  151
             20   14  161   20   12  171   20   14
            181   20   14  191   20   12  201   20
             14  211   20   14  221   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-02-13T20:53:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4,
 'duration': 0,
 'programmed': 2.4,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x1c 0x00    ..`.`...
    decimal
              1    0   96    0   96    0   28    0
    datetime (2015-02-13T20:53:35)
    0000   0x23 0xb5 0x54 0x0d 0x0f                   #.T..
    body (0)

#### RECORD 3 SensorAlert 2015-02-13T21:09:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 243}
```
    op hex (3)
    0000   0x0b 0x65 0xf3                             .e.
    decimal
             11  101  243
    datetime (2015-02-13T21:09:35)
    0000   0x23 0x89 0x35 0xad 0x0f                   #.5..
    body (0)

#### RECORD 4 BolusWizard 2015-02-13T21:10:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-13T21:10:05)
    0000   0x05 0x8a 0x15 0x6d 0x0f                   ...m.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    <P.<(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             60   80    0   60   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.4, 'curve': 4},
 {'age': 194, 'amount': 0.05, 'curve': 4},
 {'age': 204, 'amount': 1.95, 'curve': 4},
 {'age': 224, 'amount': 0.3, 'curve': 4},
 {'age': 234, 'amount': 3.7, 'curve': 4},
 {'age': 168, 'amount': 0.1, 'curve': 20},
 {'age': 178, 'amount': 0.35, 'curve': 20},
 {'age': 188, 'amount': 0.3, 'curve': 20},
 {'age': 198, 'amount': 0.35, 'curve': 20},
 {'age': 208, 'amount': 0.35, 'curve': 20},
 {'age': 218, 'amount': 0.3, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x60 0x18 0x04 0x02 0xc2 0x04    \#`.....
    0008   0x4e 0xcc 0x04 0x0c 0xe0 0x04 0x94 0xea    N.......
    0010   0x04 0x04 0xa8 0x14 0x0e 0xb2 0x14 0x0c    ........
    0018   0xbc 0x14 0x0e 0xc6 0x14 0x0e 0xd0 0x14    ........
    0020   0x0c 0xda 0x14                             ...
    decimal
             92   35   96   24    4    2  194    4
             78  204    4   12  224    4  148  234
              4    4  168   20   14  178   20   12
            188   20   14  198   20   14  208   20
             12  218   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-02-13T21:13:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 150,
 'programmed': 5.0,
 'type': 'square',
 'unabsorbed': 2.8}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x70 0x05    ......p.
    decimal
              1    0  200    0  200    0  112    5
    datetime (2015-02-13T21:13:27)
    0000   0x1b 0x8d 0xb5 0x6d 0x0f                   ...m.
    body (0)

#### RECORD 7 Bolus 2015-02-13T21:10:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 2.8}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x70 0x00    ......p.
    decimal
              1    0  200    0  200    0  112    0
    datetime (2015-02-13T21:10:05)
    0000   0x05 0x8a 0x95 0x6d 0x0f                   ...m.
    body (0)

#### RECORD 8 BolusWizard 2015-02-13T21:20:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.1,
 'carb_input': 25,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-13T21:20:30)
    0000   0x1e 0x94 0x15 0x6d 0x0f                   ...m.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xa4 0x00 0x00 0x00 0x00 0xa4 0x78         ......x
    decimal
             25   80    0   60   40   90    0    0
            164    0    0    0    0  164  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.15, 'curve': 4},
 {'age': 14, 'amount': 5.1, 'curve': 4},
 {'age': 34, 'amount': 2.4, 'curve': 4},
 {'age': 204, 'amount': 0.05, 'curve': 4},
 {'age': 214, 'amount': 1.95, 'curve': 4},
 {'age': 234, 'amount': 0.3, 'curve': 4},
 {'age': 244, 'amount': 3.7, 'curve': 4},
 {'age': 178, 'amount': 0.1, 'curve': 20},
 {'age': 188, 'amount': 0.35, 'curve': 20},
 {'age': 198, 'amount': 0.3, 'curve': 20},
 {'age': 208, 'amount': 0.35, 'curve': 20},
 {'age': 218, 'amount': 0.35, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x06 0x04 0x04 0xcc 0x0e 0x04    \&......
    0008   0x60 0x22 0x04 0x02 0xcc 0x04 0x4e 0xd6    `"....N.
    0010   0x04 0x0c 0xea 0x04 0x94 0xf4 0x04 0x04    ........
    0018   0xb2 0x14 0x0e 0xbc 0x14 0x0c 0xc6 0x14    ........
    0020   0x0e 0xd0 0x14 0x0e 0xda 0x14              ......
    decimal
             92   38    6    4    4  204   14    4
             96   34    4    2  204    4   78  214
              4   12  234    4  148  244    4    4
            178   20   14  188   20   12  198   20
             14  208   20   14  218   20
    datetime (unknown)

    body (0)

#### RECORD 10 BasalProfileStart 2015-02-13T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-13T22:00:00)
    0000   0x00 0x80 0x16 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 11 BasalProfileStart 2015-02-14T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-14T00:00:00)
    0000   0x00 0x80 0x00 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 12 MResultTotals 2015-02-14T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0b 0x54                   ....T
    decimal
              7    0    0   11   84
    datetime (2015-02-14T00:00:00)
    0000   0x2d 0x0f                                  -.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 13 Sara6E 2015-02-14T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-14T00:00:00)
    0000   0x2d 0x0f                                  -.
    body (49)
    hex
    0000   0x05 0x00 0xac 0x63 0xf5 0x02 0x00 0x00    ...c....
    0008   0x0b 0x54 0x03 0x24 0x1c 0x08 0x30 0x48    .T.$..0H
    0010   0x00 0xa9 0x03 0x98 0x00 0x60 0x00 0x00    .....`..
    0018   0x04 0x38 0x03 0x01 0x00 0x08 0x00 0xad    .8......
    0020   0x35 0x2b 0x03 0x0e 0x2b 0x04 0x01 0x00    5+..+...
    0028   0x00 0x02 0x09 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  172   99  245    2    0    0
             11   84    3   36   28    8   48   72
              0  169    3  152    0   96    0    0
              4   56    3    1    0    8    0  173
             53   43    3   14   43    4    1    0
              0    2    9    1    0    0    0    0
              0

#### RECORD 14 SensorAlert 2015-02-14T00:34:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-14T00:34:27)
    0000   0x1b 0xa2 0x20 0xae 0x0f                   .. ..
    body (0)

#### RECORD 15 SensorAlert 2015-02-14T00:42:58 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-14T00:42:58)
    0000   0x3a 0xaa 0x20 0xae 0x0f                   :. ..
    body (0)

#### RECORD 16 SensorAlert 2015-02-14T03:43:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 117}
```
    op hex (3)
    0000   0x0b 0x65 0x75                             .eu
    decimal
             11  101  117
    datetime (2015-02-14T03:43:39)
    0000   0x27 0xab 0x23 0xae 0x8f                   '.#..
    body (0)

#### RECORD 17 BasalProfileStart 2015-02-14T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-14T04:00:00)
    0000   0x00 0x80 0x04 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 18 NoDelivery 2015-02-14T04:06:18 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-14T04:06:18)
    0000   0x12 0x86 0x44 0x4e 0x0f                   ..DN.
    body (0)

#### RECORD 19 ClearAlarm 2015-02-14T04:15:10 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-14T04:15:10)
    0000   0x0a 0x8f 0x04 0x0e 0x0f                   .....
    body (0)

#### RECORD 20 Rewind 2015-02-14T04:15:55 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-14T04:15:55)
    0000   0x37 0x8f 0x04 0x0e 0x0f                   7....
    body (0)

#### RECORD 21 Prime 2015-02-14T04:16:37 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 10.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x67                   ....g
    decimal
              3    0    0    0  103
    datetime (2015-02-14T04:16:37)
    0000   0x25 0x90 0x24 0x0e 0x0f                   %.$..
    body (0)

#### RECORD 22 BasalProfileStart 2015-02-14T04:17:26 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-14T04:17:26)
    0000   0x1a 0x91 0x04 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 23 Prime 2015-02-14T04:17:12 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-14T04:17:12)
    0000   0x0c 0x91 0x04 0x0e 0x0f                   .....
    body (0)

#### RECORD 24 BolusWizard 2015-02-14T04:19:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-14T04:19:21)
    0000   0x15 0x93 0x04 0x6e 0x0f                   ...n.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0  100   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 25 UnabsorbedInsulinBolus unknown head[53], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 0.25, 'curve': 20},
 {'age': 37, 'amount': 0.35, 'curve': 20},
 {'age': 47, 'amount': 0.3, 'curve': 20},
 {'age': 57, 'amount': 0.35, 'curve': 20},
 {'age': 67, 'amount': 0.35, 'curve': 20},
 {'age': 77, 'amount': 0.3, 'curve': 20},
 {'age': 87, 'amount': 0.35, 'curve': 20},
 {'age': 97, 'amount': 0.35, 'curve': 20},
 {'age': 107, 'amount': 0.3, 'curve': 20},
 {'age': 117, 'amount': 0.35, 'curve': 20},
 {'age': 127, 'amount': 0.35, 'curve': 20},
 {'age': 137, 'amount': 0.3, 'curve': 20},
 {'age': 147, 'amount': 0.35, 'curve': 20},
 {'age': 157, 'amount': 0.35, 'curve': 20},
 {'age': 167, 'amount': 0.3, 'curve': 20},
 {'age': 177, 'amount': 5.1, 'curve': 20},
 {'age': 197, 'amount': 2.4, 'curve': 20}]
```
    op hex (53)
    0000   0x5c 0x35 0x0a 0x1b 0x14 0x0e 0x25 0x14    \5....%.
    0008   0x0c 0x2f 0x14 0x0e 0x39 0x14 0x0e 0x43    ./..9..C
    0010   0x14 0x0c 0x4d 0x14 0x0e 0x57 0x14 0x0e    ..M..W..
    0018   0x61 0x14 0x0c 0x6b 0x14 0x0e 0x75 0x14    a..k..u.
    0020   0x0e 0x7f 0x14 0x0c 0x89 0x14 0x0e 0x93    ........
    0028   0x14 0x0e 0x9d 0x14 0x0c 0xa7 0x14 0xcc    ........
    0030   0xb1 0x14 0x60 0xc5 0x14                   ..`..
    decimal
             92   53   10   27   20   14   37   20
             12   47   20   14   57   20   14   67
             20   12   77   20   14   87   20   14
             97   20   12  107   20   14  117   20
             14  127   20   12  137   20   14  147
             20   14  157   20   12  167   20  204
            177   20   96  197   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2015-02-14T04:19:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6,
 'duration': 0,
 'programmed': 1.6,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x40 0x01 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    1   64    1   64    0    0    0
    datetime (2015-02-14T04:19:21)
    0000   0x15 0x93 0x44 0x6e 0x0f                   ..Dn.
    body (0)

#### RECORD 27 SensorAlert 2015-02-14T05:14:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 130}
```
    op hex (3)
    0000   0x0b 0x65 0x82                             .e.
    decimal
             11  101  130
    datetime (2015-02-14T05:14:27)
    0000   0x1b 0x8e 0x25 0xae 0x8f                   ..%..
    body (0)

#### RECORD 28 SensorAlert 2015-02-14T06:42:58 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 17}
```
    op hex (3)
    0000   0x0b 0x65 0x11                             .e.
    decimal
             11  101   17
    datetime (2015-02-14T06:42:58)
    0000   0x3a 0xaa 0x26 0xae 0x8f                   :.&..
    body (0)

#### RECORD 29 CalBGForPH 2015-02-14T06:50:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 229}
```
    op hex (2)
    0000   0x0a 0xe5                                  ..
    decimal
             10  229
    datetime (2015-02-14T06:50:08)
    0000   0x08 0xb2 0x26 0x6e 0x0f                   ..&n.
    body (0)

#### RECORD 30 BGReceived 2015-02-14T06:50:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2015-02-14T06:50:08)
    0000   0x08 0xb2 0xa6 0x6e 0x0f                   ...n.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 31 BolusWizard 2015-02-14T06:50:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 229,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 2.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.2}
```
    op hex (2)
    0000   0x5b 0xe5                                  [.
    decimal
             91  229
    datetime (2015-02-14T06:50:22)
    0000   0x16 0xb2 0x06 0x0e 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x6c 0x00    .P.d(Zl.
    0008   0x00 0x00 0x00 0x58 0x00 0x14 0x78         ...X..x
    decimal
              0   80    0  100   40   90  108    0
              0    0    0   88    0   20  120

#### RECORD 32 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 154, 'amount': 1.6, 'curve': 5},
 {'age': 178, 'amount': 0.25, 'curve': 20},
 {'age': 188, 'amount': 0.35, 'curve': 20},
 {'age': 198, 'amount': 0.3, 'curve': 20},
 {'age': 208, 'amount': 0.35, 'curve': 20},
 {'age': 218, 'amount': 0.35, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x40 0x9a 0x05 0x0a 0xb2 0x14    \.@.....
    0008   0x0e 0xbc 0x14 0x0c 0xc6 0x14 0x0e 0xd0    ........
    0010   0x14 0x0e 0xda 0x14                        ....
    decimal
             92   20   64  154    5   10  178   20
             14  188   20   12  198   20   14  208
             20   14  218   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2015-02-14T06:50:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x58 0x00    ......X.
    decimal
              1    0   20    0   20    0   88    0
    datetime (2015-02-14T06:50:22)
    0000   0x16 0xb2 0x46 0x0e 0x0f                   ..F..
    body (0)

#### RECORD 34 Bolus 2015-02-14T06:55:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x68 0x00    ......h.
    decimal
              1    0  160    0  160    0  104    0
    datetime (2015-02-14T06:55:19)
    0000   0x13 0xb7 0x46 0x6e 0x0f                   ..Fn.
    body (0)

#### RECORD 35 BasalProfileStart 2015-02-14T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-14T07:00:00)
    0000   0x00 0x80 0x07 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 36 SensorAlert 2015-02-14T08:13:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 254}
```
    op hex (3)
    0000   0x0b 0x65 0xfe                             .e.
    decimal
             11  101  254
    datetime (2015-02-14T08:13:00)
    0000   0x00 0x8d 0x28 0xae 0x0f                   ..(..
    body (0)

#### RECORD 37 Bolus 2015-02-14T09:27:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.3}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x34 0x00    ..x.x.4.
    decimal
              1    0  120    0  120    0   52    0
    datetime (2015-02-14T09:27:21)
    0000   0x15 0x9b 0x49 0x6e 0x0f                   ..In.
    body (0)

#### RECORD 38 SensorAlert 2015-02-14T09:43:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 242}
```
    op hex (3)
    0000   0x0b 0x65 0xf2                             .e.
    decimal
             11  101  242
    datetime (2015-02-14T09:43:39)
    0000   0x27 0xab 0x29 0xae 0x0f                   '.)..
    body (0)

#### RECORD 39 Bolus 2015-02-14T09:43:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 3.9}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x9c 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  156    0
    datetime (2015-02-14T09:43:59)
    0000   0x3b 0xab 0x49 0x6e 0x0f                   ;.In.
    body (0)

#### RECORD 40 BasalProfileStart 2015-02-14T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-14T10:00:00)
    0000   0x00 0x80 0x0a 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 41 SensorAlert 2015-02-14T11:22:58 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-14T11:22:58)
    0000   0x3a 0x96 0x2b 0xae 0x0f                   :.+..
    body (0)

#### RECORD 42 Bolus 2015-02-14T11:24:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x7c 0x00    ..<.<.|.
    decimal
              1    0   60    0   60    0  124    0
    datetime (2015-02-14T11:24:17)
    0000   0x11 0x98 0x4b 0x6e 0x0f                   ..Kn.
    body (0)

#### RECORD 43 BasalProfileStart 2015-02-14T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-14T12:00:00)
    0000   0x00 0x80 0x0c 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 44 SensorAlert 2015-02-14T14:10:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-14T14:10:13)
    0000   0x0d 0x8a 0x2e 0xae 0x0f                   .....
    body (0)

#### RECORD 45 SensorAlert 2015-02-14T14:40:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-14T14:40:00)
    0000   0x00 0xa8 0x2e 0xae 0x0f                   .....
    body (0)

#### RECORD 46 BasalProfileStart 2015-02-14T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-14T15:00:00)
    0000   0x00 0x80 0x0f 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 47 SensorAlert 2015-02-14T15:10:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-14T15:10:00)
    0000   0x00 0x8a 0x2f 0xae 0x0f                   ../..
    body (0)

#### RECORD 48 CalBGForPH 2015-02-14T15:36:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2015-02-14T15:36:36)
    0000   0x24 0xa4 0x2f 0x6e 0x0f                   $./n.
    body (0)

#### RECORD 49 BGReceived 2015-02-14T15:36:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-14T15:36:36)
    0000   0x24 0xa4 0xaf 0x6e 0x0f                   $..n.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 50 BolusWizard 2015-02-14T15:36:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 189,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.7,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 1.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2015-02-14T15:36:57)
    0000   0x39 0xa4 0x0f 0x0e 0x0f                   9....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x44 0x00    .P.P(ZD.
    0008   0x00 0x00 0x00 0x00 0x00 0x44 0x78         .....Dx
    decimal
              0   80    0   80   40   90   68    0
              0    0    0    0    0   68  120

#### RECORD 51 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 1.5, 'curve': 20},
 {'age': 94, 'amount': 0.05, 'curve': 20},
 {'age': 104, 'amount': 2.95, 'curve': 20},
 {'age': 114, 'amount': 3.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x04 0x14 0x02 0x5e 0x14    \.<...^.
    0008   0x76 0x68 0x14 0x78 0x72 0x14              vh.xr.
    decimal
             92   14   60    4   20    2   94   20
            118  104   20  120  114   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2015-02-14T15:36:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7,
 'duration': 0,
 'programmed': 1.7,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2015-02-14T15:36:58)
    0000   0x3a 0xa4 0x4f 0x0e 0x0f                   :.O..
    body (0)

#### RECORD 53 SensorAlert 2015-02-14T15:51:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 189}
```
    op hex (3)
    0000   0x0b 0x65 0xbd                             .e.
    decimal
             11  101  189
    datetime (2015-02-14T15:51:11)
    0000   0x0b 0xb3 0x2f 0xae 0x0f                   ../..
    body (0)

#### RECORD 54 BolusWizard 2015-02-14T15:51:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-14T15:51:27)
    0000   0x1b 0xb3 0x0f 0x6e 0x0f                   ...n.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    (P.P(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             40   80    0   80   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 55 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 1.7, 'curve': 4},
 {'age': 19, 'amount': 1.5, 'curve': 20},
 {'age': 109, 'amount': 0.05, 'curve': 20},
 {'age': 119, 'amount': 2.95, 'curve': 20},
 {'age': 129, 'amount': 3.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x0f 0x04 0x3c 0x13 0x14    \.D..<..
    0008   0x02 0x6d 0x14 0x76 0x77 0x14 0x78 0x81    .m.vw.x.
    0010   0x14                                       .
    decimal
             92   17   68   15    4   60   19   20
              2  109   20  118  119   20  120  129
             20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2015-02-14T15:51:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x44 0x00    ......D.
    decimal
              1    0  200    0  200    0   68    0
    datetime (2015-02-14T15:51:28)
    0000   0x1c 0xb3 0x4f 0x6e 0x0f                   ..On.
    body (0)

#### RECORD 57 PumpSuspend 2015-02-14T16:09:48 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-14T16:09:48)
    0000   0x30 0x89 0x10 0x0e 0x0f                   0....
    body (0)

#### RECORD 58 BasalProfileStart 2015-02-14T16:34:05 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-14T16:34:05)
    0000   0x05 0xa2 0x10 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 59 PumpResume 2015-02-14T16:34:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-14T16:34:05)
    0000   0x05 0xa2 0x10 0x0e 0x0f                   .....
    body (0)

#### RECORD 60 BolusWizard 2015-02-14T16:53:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.3,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 2.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-14T16:53:05)
    0000   0x05 0xb5 0x10 0x6e 0x0f                   ...n.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    FP.P(Z..
    0008   0x5c 0x00 0x00 0x00 0x01 0x5c 0x78         \....\x
    decimal
             70   80    0   80   40   90    0    1
             92    0    0    0    1   92  120

#### RECORD 61 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 5.0, 'curve': 4},
 {'age': 77, 'amount': 1.7, 'curve': 4},
 {'age': 81, 'amount': 1.5, 'curve': 20},
 {'age': 171, 'amount': 0.05, 'curve': 20},
 {'age': 181, 'amount': 2.95, 'curve': 20},
 {'age': 191, 'amount': 3.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0xc8 0x43 0x04 0x44 0x4d 0x04    \..C.DM.
    0008   0x3c 0x51 0x14 0x02 0xab 0x14 0x76 0xb5    <Q....v.
    0010   0x14 0x78 0xbf 0x14                        .x..
    decimal
             92   20  200   67    4   68   77    4
             60   81   20    2  171   20  118  181
             20  120  191   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2015-02-14T16:56:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9,
 'duration': 120,
 'programmed': 3.9,
 'type': 'square',
 'unabsorbed': 5.2}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0xd0 0x04    ........
    decimal
              1    0  156    0  156    0  208    4
    datetime (2015-02-14T16:56:19)
    0000   0x13 0xb8 0xb0 0x6e 0x0f                   ...n.
    body (0)

#### RECORD 63 Bolus 2015-02-14T16:53:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8,
 'duration': 0,
 'programmed': 4.8,
 'type': 'normal',
 'unabsorbed': 5.2}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0xd0 0x00    ........
    decimal
              1    0  192    0  192    0  208    0
    datetime (2015-02-14T16:53:05)
    0000   0x05 0xb5 0x90 0x6e 0x0f                   ...n.
    body (0)

#### RECORD 64 SensorAlert 2015-02-14T20:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-14T20:36:00)
    0000   0x00 0xa4 0x34 0xae 0x0f                   ..4..
    body (0)

#### RECORD 65 BolusWizard 2015-02-14T20:37:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.2,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 0.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-14T20:37:04)
    0000   0x04 0xa5 0x14 0x6e 0x0f                   ...n.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 66 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 0.35, 'curve': 4},
 {'age': 121, 'amount': 0.3, 'curve': 4},
 {'age': 131, 'amount': 0.35, 'curve': 4},
 {'age': 141, 'amount': 0.3, 'curve': 4},
 {'age': 151, 'amount': 0.35, 'curve': 4},
 {'age': 161, 'amount': 0.3, 'curve': 4},
 {'age': 171, 'amount': 0.35, 'curve': 4},
 {'age': 181, 'amount': 0.3, 'curve': 4},
 {'age': 191, 'amount': 0.35, 'curve': 4},
 {'age': 201, 'amount': 0.3, 'curve': 4},
 {'age': 211, 'amount': 0.35, 'curve': 4},
 {'age': 221, 'amount': 0.75, 'curve': 4},
 {'age': 231, 'amount': 4.35, 'curve': 4},
 {'age': 35, 'amount': 5.0, 'curve': 20},
 {'age': 45, 'amount': 1.7, 'curve': 20}]
```
    op hex (47)
    0000   0x5c 0x2f 0x0e 0x6f 0x04 0x0c 0x79 0x04    \/.o..y.
    0008   0x0e 0x83 0x04 0x0c 0x8d 0x04 0x0e 0x97    ........
    0010   0x04 0x0c 0xa1 0x04 0x0e 0xab 0x04 0x0c    ........
    0018   0xb5 0x04 0x0e 0xbf 0x04 0x0c 0xc9 0x04    ........
    0020   0x0e 0xd3 0x04 0x1e 0xdd 0x04 0xae 0xe7    ........
    0028   0x04 0xc8 0x23 0x14 0x44 0x2d 0x14         ..#.D-.
    decimal
             92   47   14  111    4   12  121    4
             14  131    4   12  141    4   14  151
              4   12  161    4   14  171    4   12
            181    4   14  191    4   12  201    4
             14  211    4   30  221    4  174  231
              4  200   35   20   68   45   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2015-02-14T20:39:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6,
 'duration': 90,
 'programmed': 2.6,
 'type': 'square',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x38 0x03    ..h.h.8.
    decimal
              1    0  104    0  104    0   56    3
    datetime (2015-02-14T20:39:47)
    0000   0x2f 0xa7 0xb4 0x6e 0x0f                   /..n.
    body (0)

`end analysis/736868/logs/ReadHistoryData-page-29.data: 68 records`
