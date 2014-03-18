## START logs/ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd0 0xce                                  ..
##### DEBUG DECIMAL
            208  206
#### RECORD 0 BolusWizard 2014-03-02T10:10:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-02T10:10:20)
    0000   0x14 0xca 0x0a 0x62 0x0e                   ...b.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    (P.n(P..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x64         ......d
    decimal
             40   80    0  110   40   80    0    0
            144    0    0    0    0  144  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 4.0, 'curve': 128},
 {'age': 68, 'amount': 2.0, 'curve': 128},
 {'age': 92, 'amount': 3.5, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa0 0x12 0x80 0x50 0x44 0x80    \....PD.
    0008   0x8c 0x5c 0x90                             .\.
    decimal
             92   11  160   18  128   80   68  128
            140   92  144
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2014-03-02T10:10:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xb4 0x00    ........
    decimal
              1    0  144    0  144    0  180    0
    datetime (2014-03-02T10:10:20)
    0000   0x14 0xca 0x4a 0x62 0x0e                   ..Jb.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 BasalProfileStart 2014-03-02T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-02T10:30:00)
    0000   0x00 0xde 0x0a 0x02 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2014-03-02T13:25:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2014-03-02T13:25:35)
    0000   0x23 0xd9 0x2d 0x62 0x0e                   #.-b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2014-03-02T13:25:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-03-02T13:25:35)
    0000   0x23 0xd9 0x2d 0x62 0x0e                   #.-b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2014-03-02T13:26:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2014-03-02T13:26:23)
    0000   0x17 0xda 0x2d 0x62 0x0e                   ..-b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2014-03-02T13:26:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2014-03-02T13:26:23)
    0000   0x17 0xda 0x0d 0x62 0x0e                   ...b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2014-03-02T13:26:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 184,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2014-03-02T13:26:47)
    0000   0x2f 0xda 0x0d 0x02 0x0e                   /....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x40 0x00    .P.x2P@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x64         .....@d
    decimal
              0   80    0  120   50   80   64    0
              0    0    0    0    0   64  100
    HOUR BITS: [1, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 194, 'amount': 1.1, 'curve': 128},
 {'age': 204, 'amount': 2.5, 'curve': 128},
 {'age': 214, 'amount': 4.0, 'curve': 128},
 {'age': 8, 'amount': 2.0, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x2c 0xc2 0x80 0x64 0xcc 0x80    \.,..d..
    0008   0xa0 0xd6 0x80 0x50 0x08 0x90              ...P..
    decimal
             92   14   44  194  128  100  204  128
            160  214  128   80    8  144
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2014-03-02T13:26:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2014-03-02T13:26:47)
    0000   0x2f 0xda 0x4d 0x02 0x0e                   /.M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BolusWizard 2014-03-02T14:00:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 0,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 110,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-02T14:00:09)
    0000   0x09 0xc0 0x0e 0x62 0x0e                   ...b.
    body (15)
    hex
    0000   0x6e 0x50 0x00 0x78 0x32 0x50 0x00 0x01    nP.x2P..
    0008   0x6c 0x00 0x00 0x00 0x01 0x6c 0x64         l....ld
    decimal
            110   80    0  120   50   80    0    1
            108    0    0    0    1  108  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 1.6, 'curve': 128},
 {'age': 228, 'amount': 1.1, 'curve': 128},
 {'age': 238, 'amount': 2.5, 'curve': 128},
 {'age': 248, 'amount': 4.0, 'curve': 128},
 {'age': 42, 'amount': 2.0, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x26 0x80 0x2c 0xe4 0x80    \.@&.,..
    0008   0x64 0xee 0x80 0xa0 0xf8 0x80 0x50 0x2a    d.....P*
    0010   0x90                                       .
    decimal
             92   17   64   38  128   44  228  128
            100  238  128  160  248  128   80   42
            144
    datetime (unknown)

    body (0)

#### RECORD 13 LowReservoir 2014-03-02T14:00:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-03-02T14:00:37)
    0000   0x25 0xc0 0x0e 0x02 0x0e                   %....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 Bolus 2014-03-02T14:00:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x6c 0x01 0x6c 0x00 0x30 0x00    ..l.l.0.
    decimal
              1    1  108    1  108    0   48    0
    datetime (2014-03-02T14:00:09)
    0000   0x09 0xc0 0x4e 0x62 0x0e                   ..Nb.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 BolusWizard 2014-03-02T15:15:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 24,
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
    datetime (2014-03-02T15:15:27)
    0000   0x1b 0xcf 0x0f 0x62 0x0e                   ...b.
    body (15)
    hex
    0000   0x18 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             24   80    0  120   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 4.7, 'curve': 128},
 {'age': 83, 'amount': 4.4, 'curve': 128},
 {'age': 113, 'amount': 1.6, 'curve': 128},
 {'age': 47, 'amount': 1.1, 'curve': 144},
 {'age': 57, 'amount': 2.5, 'curve': 144},
 {'age': 67, 'amount': 4.0, 'curve': 144},
 {'age': 117, 'amount': 2.0, 'curve': 144}]
```
    op hex (23)
    0000   0x5c 0x17 0xbc 0x49 0x80 0xb0 0x53 0x80    \..I..S.
    0008   0x40 0x71 0x80 0x2c 0x2f 0x90 0x64 0x39    @q.,/.d9
    0010   0x90 0xa0 0x43 0x90 0x50 0x75 0x90         ..C.Pu.
    decimal
             92   23  188   73  128  176   83  128
             64  113  128   44   47  144  100   57
            144  160   67  144   80  117  144
    datetime (unknown)

    body (0)

#### RECORD 17 LowReservoir 2014-03-02T15:16:42 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-03-02T15:16:42)
    0000   0x2a 0xd0 0x0f 0x02 0x0e                   *....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 Bolus 2014-03-02T15:15:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x68 0x00    ..P.P.h.
    decimal
              1    0   80    0   80    0  104    0
    datetime (2014-03-02T15:15:27)
    0000   0x1b 0xcf 0x4f 0x62 0x0e                   ..Ob.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 CalBGForPH 2014-03-02T21:23:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2014-03-02T21:23:21)
    0000   0x15 0xd7 0x35 0x62 0x0e                   ..5b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 Ian3F 2014-03-02T21:23:21 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2014-03-02T21:23:21)
    0000   0x15 0xd7 0x55 0x62 0x0e                   ..Ub.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 BolusWizard 2014-03-02T21:28:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 74,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x4a                                  [J
    decimal
             91   74
    datetime (2014-03-02T21:28:55)
    0000   0x37 0xdc 0x15 0x62 0x0e                   7..b.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x32 0x50 0xfc 0x00    #P.n2P..
    0008   0x7c 0xf8 0x00 0x00 0x00 0x78 0x64         |....xd
    decimal
             35   80    0  110   50   80  252    0
            124  248    0    0    0  120  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 2.0, 'curve': 144},
 {'age': 190, 'amount': 4.7, 'curve': 144},
 {'age': 200, 'amount': 4.4, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x78 0x90 0xbc 0xbe 0x90    \.Px....
    0008   0xb0 0xc8 0x90                             ...
    decimal
             92   11   80  120  144  188  190  144
            176  200  144
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2014-03-02T21:28:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2014-03-02T21:28:55)
    0000   0x37 0xdc 0x55 0x62 0x0e                   7.Ub.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 BasalProfileStart 2014-03-02T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-02T22:30:00)
    0000   0x00 0xde 0x16 0x02 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BasalProfileStart 2014-03-03T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-03T00:00:00)
    0000   0x00 0xc0 0x00 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 MResultTotals 2014-03-03T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x64                   ....d
    decimal
              7    0    0    6  100
    datetime (2014-03-03T00:00:00)
    0000   0x22 0x8e                                  ".
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 27 Sara6E 2014-03-03T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-03T00:00:00)
    0000   0x22 0x8e                                  ".
    body (49)
    hex
    0000   0x05 0x00 0xa0 0x4a 0xc5 0x05 0x00 0x00    ...J....
    0008   0x06 0x64 0x01 0xe4 0x1e 0x04 0x80 0x46    .d.....F
    0010   0x00 0xfe 0x03 0x64 0x01 0x1c 0x00 0x00    ...d....
    0018   0x00 0x00 0x05 0x03 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xb7    ........
    0028   0xb7 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  160   74  197    5    0    0
              6  100    1  228   30    4  128   70
              0  254    3  100    1   28    0    0
              0    0    5    3    0    0    0    0
              0    0    0    0    0    0    0  183
            183    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 28 CalBGForPH 2014-03-03T00:30:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2014-03-03T00:30:23)
    0000   0x17 0xde 0x20 0x03 0x0e                   .. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 BolusWizard 2014-03-03T00:30:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 0,
 'bg_target_low': 55,
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
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2014-03-03T00:30:28)
    0000   0x1c 0xde 0x00 0x63 0x0e                   ...c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x14 0x00    .P.n7P..
    0008   0x00 0x00 0x00 0x00 0x00 0x14 0x64         ......d
    decimal
              0   80    0  110   55   80   20    0
              0    0    0    0    0   20  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 3.0, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0xbc 0x80                   \.x..
    decimal
             92    5  120  188  128
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2014-03-03T00:30:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x00 0x00    .. . ...
    decimal
              1    0   32    0   32    0    0    0
    datetime (2014-03-03T00:30:28)
    0000   0x1c 0xde 0x40 0x63 0x0e                   ..@c.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 BasalProfileStart 2014-03-03T00:35:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-03T00:35:32)
    0000   0x20 0xe3 0x00 0x03 0x0e                    ....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Prime 2014-03-03T00:35:22 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-03-03T00:35:22)
    0000   0x16 0xe3 0x00 0x03 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 Rewind 2014-03-03T00:35:47 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-03-03T00:35:47)
    0000   0x2f 0xe3 0x00 0x03 0x0e                   /....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 Prime 2014-03-03T00:36:28 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 9.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x5b                   ....[
    decimal
              3    0    0    0   91
    datetime (2014-03-03T00:36:28)
    0000   0x1c 0xe4 0x20 0x03 0x0e                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 BasalProfileStart 2014-03-03T00:36:46 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-03T00:36:46)
    0000   0x2e 0xe4 0x00 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 1]
#### RECORD 37 BasalProfileStart 2014-03-03T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-03T02:00:00)
    0000   0x00 0xc0 0x02 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 BasalProfileStart 2014-03-03T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-03T04:00:00)
    0000   0x00 0xc0 0x04 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 39 CalBGForPH 2014-03-03T05:06:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2014-03-03T05:06:17)
    0000   0x11 0xc6 0x25 0x03 0x0e                   ..%..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 BolusWizard 2014-03-03T05:06:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 188,
 'bg_target_high': 0,
 'bg_target_low': 30,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 11.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2014-03-03T05:06:21)
    0000   0x15 0xc6 0x05 0x63 0x0e                   ...c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x74 0x00    .P.n.Pt.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x64         .....td
    decimal
              0   80    0  110   30   80  116    0
              0    0    0    0    0  116  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 0.8, 'curve': 144},
 {'age': 208, 'amount': 3.0, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x1c 0x90 0x78 0xd0 0x90    \. ..x..
    decimal
             92    8   32   28  144  120  208  144
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2014-03-03T05:06:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2014-03-03T05:06:21)
    0000   0x15 0xc6 0x45 0x63 0x0e                   ..Ec.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 BasalProfileStart 2014-03-03T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-03T06:00:00)
    0000   0x00 0xc0 0x06 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 44 CalBGForPH 2014-03-03T07:44:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2014-03-03T07:44:55)
    0000   0x37 0xec 0x27 0x03 0x0e                   7.'..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2014-03-03T07:44:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 141,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8d                                  [.
    decimal
             91  141
    datetime (2014-03-03T07:44:58)
    0000   0x3a 0xec 0x07 0x63 0x0e                   :..c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x28 0x00    .P.n(P(.
    0008   0x00 0x00 0x00 0x00 0x00 0x28 0x64         .....(d
    decimal
              0   80    0  110   40   80   40    0
              0    0    0    0    0   40  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 2.9, 'curve': 128},
 {'age': 186, 'amount': 0.8, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0xa2 0x80 0x20 0xba 0x90    \.t.. ..
    decimal
             92    8  116  162  128   32  186  144
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2014-03-03T07:44:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2014-03-03T07:44:58)
    0000   0x3a 0xec 0x47 0x63 0x0e                   :.Gc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BasalProfileStart 2014-03-03T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-03T10:30:00)
    0000   0x00 0xde 0x0a 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 49 CalBGForPH 2014-03-03T11:33:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2014-03-03T11:33:43)
    0000   0x2b 0xe1 0x2b 0x63 0x0e                   +.+c.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 Ian3F 2014-03-03T11:33:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-03-03T11:33:43)
    0000   0x2b 0xe1 0x8b 0x63 0x0e                   +..c.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2014-03-03T11:34:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2014-03-03T11:34:19)
    0000   0x13 0xe2 0x0b 0x03 0x0e                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x32 0x50 0x2c 0x00    .P.x2P,.
    0008   0x28 0x00 0x00 0x00 0x00 0x54 0x64         (....Td
    decimal
             12   80    0  120   50   80   44    0
             40    0    0    0    0   84  100
    HOUR BITS: [1, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 232, 'amount': 1.0, 'curve': 128},
 {'age': 136, 'amount': 2.9, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0xe8 0x80 0x74 0x88 0x90    \.(..t..
    decimal
             92    8   40  232  128  116  136  144
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2014-03-03T11:34:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2014-03-03T11:34:19)
    0000   0x13 0xe2 0x4b 0x03 0x0e                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 54 CalBGForPH 2014-03-03T12:06:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2014-03-03T12:06:25)
    0000   0x19 0xc6 0x2c 0x63 0x0e                   ..,c.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 Ian3F 2014-03-03T12:06:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-03-03T12:06:25)
    0000   0x19 0xc6 0x6c 0x63 0x0e                   ..lc.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2014-03-03T12:56:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 197}
```
    op hex (2)
    0000   0x0a 0xc5                                  ..
    decimal
             10  197
    datetime (2014-03-03T12:56:35)
    0000   0x23 0xf8 0x2c 0x63 0x0e                   #.,c.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 Ian3F 2014-03-03T12:56:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2014-03-03T12:56:35)
    0000   0x23 0xf8 0xac 0x63 0x0e                   #..c.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2014-03-03T12:57:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 197,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 7.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc5                                  [.
    decimal
             91  197
    datetime (2014-03-03T12:57:04)
    0000   0x04 0xf9 0x0c 0x03 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x4c 0x00    .P.x2PL.
    0008   0x00 0x00 0x00 0x14 0x00 0x38 0x64         .....8d
    decimal
              0   80    0  120   50   80   76    0
              0    0    0   20    0   56  100
    HOUR BITS: [1, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 2.1, 'curve': 128},
 {'age': 59, 'amount': 1.0, 'curve': 144},
 {'age': 219, 'amount': 2.9, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x54 0x55 0x80 0x28 0x3b 0x90    \.TU.(;.
    0008   0x74 0xdb 0x90                             t..
    decimal
             92   11   84   85  128   40   59  144
            116  219  144
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2014-03-03T12:57:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x14 0x00    ..8.8...
    decimal
              1    0   56    0   56    0   20    0
    datetime (2014-03-03T12:57:04)
    0000   0x04 0xf9 0x4c 0x03 0x0e                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 61 BolusWizard 2014-03-03T13:58:15 head[2], body[15] op[0x5b]
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
    datetime (2014-03-03T13:58:15)
    0000   0x0f 0xfa 0x0d 0x63 0x0e                   ...c.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             25   80    0  120   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 1.4, 'curve': 128},
 {'age': 146, 'amount': 2.1, 'curve': 128},
 {'age': 120, 'amount': 1.0, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x42 0x80 0x54 0x92 0x80    \.8B.T..
    0008   0x28 0x78 0x90                             (x.
    decimal
             92   11   56   66  128   84  146  128
             40  120  144
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2014-03-03T13:58:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x18 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   24    0
    datetime (2014-03-03T13:58:15)
    0000   0x0f 0xfa 0x4d 0x63 0x0e                   ..Mc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2014-03-03T18:25:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 81}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2014-03-03T18:25:47)
    0000   0x2f 0xd9 0x32 0x63 0x0e                   /.2c.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 Ian3F 2014-03-03T18:25:47 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-03-03T18:25:47)
    0000   0x2f 0xd9 0x32 0x63 0x0e                   /.2c.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 TempBasal 2014-03-03T18:26:25 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-03T18:26:25)
    0000   0x19 0xda 0x12 0x03 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 67 TempBasalDuration 2014-03-03T18:26:25 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-03T18:26:25)
    0000   0x19 0xda 0x12 0x03 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 BasalProfileStart 2014-03-03T19:26:25 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-03T19:26:25)
    0000   0x19 0xda 0x13 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BolusWizard 2014-03-03T20:34:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 70,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 252}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-03T20:34:17)
    0000   0x11 0xe2 0x14 0x63 0x0e                   ...c.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    FP.n2P..
    0008   0xfc 0x00 0x00 0x00 0x00 0xfc 0x64         ......d
    decimal
             70   80    0  110   50   80    0    0
            252    0    0    0    0  252  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 2.0, 'curve': 144},
 {'age': 206, 'amount': 1.4, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x92 0x90 0x38 0xce 0x90    \.P..8..
    decimal
             92    8   80  146  144   56  206  144
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2014-03-03T20:34:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 25.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xfc 0x00 0xfc 0x00 0x00 0x00    ........
    decimal
              1    0  252    0  252    0    0    0
    datetime (2014-03-03T20:34:17)
    0000   0x11 0xe2 0x54 0x63 0x0e                   ..Tc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 BasalProfileStart 2014-03-03T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-03T22:30:00)
    0000   0x00 0xde 0x16 0x03 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 73 BolusWizard 2014-03-03T22:49:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 55,
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
    datetime (2014-03-03T22:49:02)
    0000   0x02 0xf1 0x16 0x63 0x0e                   ...c.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x37 0x50 0x00 0x00    .P.n7P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   55   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 6.3, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0xfc 0x89 0x80                   \....
    decimal
             92    5  252  137  128
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2014-03-03T22:49:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2014-03-03T22:49:02)
    0000   0x02 0xf1 0x56 0x63 0x0e                   ..Vc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 BolusWizard 2014-03-03T23:33:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 55,
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
    datetime (2014-03-03T23:33:40)
    0000   0x28 0xe1 0x17 0x63 0x0e                   (..c.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x37 0x50 0x00 0x00    .P.n7P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   55   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 1.3, 'curve': 128},
 {'age': 181, 'amount': 6.3, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x33 0x80 0xfc 0xb5 0x80    \.43....
    decimal
             92    8   52   51  128  252  181  128
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2014-03-03T23:33:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x20 0x00    ..4.4. .
    decimal
              1    0   52    0   52    0   32    0
    datetime (2014-03-03T23:33:40)
    0000   0x28 0xe1 0x57 0x63 0x0e                   (.Wc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 79 BasalProfileStart 2014-03-04T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-04T00:00:00)
    0000   0x00 0xc0 0x00 0x04 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-10.data: 80 records`
