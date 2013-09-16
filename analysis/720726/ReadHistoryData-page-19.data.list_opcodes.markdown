## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 762, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x74 0x00 0x00 0x00 0x00 0x74 0x36 0x5c    t....t6\
    0008   0x0b 0x68 0x29 0x04 0x7c 0x83 0x04 0x6c    .h).|..l
    0010   0x97 0x04 0x01 0x00 0x74 0x00 0x74 0x00    ....t.t.
    0018   0xb0 0x00 0xad 0x37 0x4c 0x73 0x0c 0x7b    ...7Ls.{
##### DEBUG DECIMAL
            116    0    0    0    0  116   54   92
             11  104   41    4  124  131    4  108
            151    4    1    0  116    0  116    0
            176    0  173   55   76  115   12  123
#### RECORD 0 Bolus 2013-08-18T18:48:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x7c 0x00    ..p.p.|.
    decimal
              1    0  112    0  112    0  124    0
    datetime (2013-08-18T18:48:02)
    0000   0x82 0x30 0x52 0x72 0x0d                   .0Rr.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 LowReservoir 2013-08-18T19:34:44 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.1}
```
    op hex (2)
    0000   0x34 0x01                                  4.
    decimal
             52    1
    datetime (2013-08-18T19:34:44)
    0000   0xac 0x22 0x13 0x12 0x8d                   ."...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-08-18T20:49:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-18T20:49:05)
    0000   0x85 0x31 0x14 0x72 0x0d                   .1.r.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 2.8, 'curve': 4},
 {'age': 234, 'amount': 2.3, 'curve': 4},
 {'age': 244, 'amount': 3.3, 'curve': 4},
 {'age': 38, 'amount': 2.0, 'curve': 20},
 {'age': 178, 'amount': 3.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x70 0x7c 0x04 0x5c 0xea 0x04    \.p|.\..
    0008   0x84 0xf4 0x04 0x50 0x26 0x14 0x7c 0xb2    ...P&.|.
    0010   0x14                                       .
    decimal
             92   17  112  124    4   92  234    4
            132  244    4   80   38   20  124  178
             20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-18T20:49:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x38 0x00    ..p.p.8.
    decimal
              1    0  112    0  112    0   56    0
    datetime (2013-08-18T20:49:05)
    0000   0x85 0x31 0x54 0x72 0x0d                   .1Tr.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2013-08-18T22:24:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 42,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 152}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-18T22:24:18)
    0000   0x92 0x18 0x16 0x72 0x0d                   ...r.
    body (15)
    hex
    0000   0x2a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    *..n.6..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x36         ......6
    decimal
             42  144    0  110   23   54    0    0
            152    0    0    0    0  152   54
    DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 2.8, 'curve': 4},
 {'age': 219, 'amount': 2.8, 'curve': 4},
 {'age': 73, 'amount': 2.3, 'curve': 20},
 {'age': 83, 'amount': 3.3, 'curve': 20},
 {'age': 133, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x70 0x63 0x04 0x70 0xdb 0x04    \.pc.p..
    0008   0x5c 0x49 0x14 0x84 0x53 0x14 0x50 0x85    \I..S.P.
    0010   0x14                                       .
    decimal
             92   17  112   99    4  112  219    4
             92   73   20  132   83   20   80  133
             20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-08-18T22:24:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x4c 0x00    ......L.
    decimal
              1    0  152    0  152    0   76    0
    datetime (2013-08-18T22:24:18)
    0000   0x92 0x18 0x56 0x72 0x0d                   ..Vr.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2013-08-18T23:13:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-18T23:13:10)
    0000   0x8a 0x0d 0x17 0x72 0x0d                   ...r.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    DAY BITS: [0, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.75, 'curve': 4},
 {'age': 58, 'amount': 1.05, 'curve': 4},
 {'age': 148, 'amount': 2.8, 'curve': 4},
 {'age': 12, 'amount': 2.8, 'curve': 20},
 {'age': 122, 'amount': 2.3, 'curve': 20},
 {'age': 132, 'amount': 3.3, 'curve': 20},
 {'age': 182, 'amount': 2.0, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x6e 0x30 0x04 0x2a 0x3a 0x04    \.n0.*:.
    0008   0x70 0x94 0x04 0x70 0x0c 0x14 0x5c 0x7a    p..p..\z
    0010   0x14 0x84 0x84 0x14 0x50 0xb6 0x14         ....P..
    decimal
             92   23  110   48    4   42   58    4
            112  148    4  112   12   20   92  122
             20  132  132   20   80  182   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-08-18T23:13:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x50 0x00 0xa8 0x00    ..d.P...
    decimal
              1    0  100    0   80    0  168    0
    datetime (2013-08-18T23:13:10)
    0000   0x8a 0x0d 0x57 0x72 0x0d                   ..Wr.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 11 NoDelivery 2013-08-18T23:14:32 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xfc                        ....
    decimal
              6    4   11  252
    datetime (2013-08-18T23:14:32)
    0000   0xa0 0x0e 0x57 0x52 0x0d                   ..WR.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 ClearAlarm 2013-08-18T23:17:11 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-08-18T23:17:11)
    0000   0x8b 0x11 0x17 0x12 0x0d                   .....
    body (0)

#### RECORD 13 Rewind 2013-08-18T23:17:16 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-18T23:17:16)
    0000   0x90 0x11 0x17 0x12 0x0d                   .....
    body (0)

#### RECORD 14 ResultTotals (2000, 8, 0, 0, 13, 18) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xb6                   .....
    decimal
              7    0    0    7  182
    datetime ((2000, 8, 0, 0, 13, 18))
    0000   0x92 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 15 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x92 0x0d 0x06 0x00 0x7f 0x6a 0x94    n.....j.
    0008   0x02 0x00 0x00 0x07 0xb6 0x03 0x62 0x2c    ......b,
    0010   0x04 0x54 0x38 0x01 0x23 0x03 0x38 0x00    .T8.#.8.
    0018   0x30 0x00 0xec 0x00 0x00 0x08 0x01 0x02    0.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  146   13    6    0  127  106  148
              2    0    0    7  182    3   98   44
              4   84   56    1   35    3   56    0
             48    0  236    0    0    8    1    2
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 16 LowBattery 2013-08-19T00:02:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-08-19T00:02:00)
    0000   0x80 0x02 0x00 0x13 0x0d                   .....
    body (0)

#### RECORD 17 Prime 2013-08-19T02:38:40 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x09                   .....
    decimal
              3    0    0    0    9
    datetime (2013-08-19T02:38:40)
    0000   0xa8 0x26 0x22 0x13 0x0d                   .&"..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 BasalProfileStart 2013-08-19T02:38:49 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-19T02:38:49)
    0000   0xb1 0x26 0x02 0x13 0x0d                   .&...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BolusWizard 2013-08-19T02:39:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 7,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 24}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-19T02:39:08)
    0000   0x88 0x27 0x02 0x73 0x0d                   .'.s.
    body (15)
    hex
    0000   0x07 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x18 0x00 0x00 0x00 0x00 0x18 0x36         ......6
    decimal
              7  144    0  110   23   54    0    0
             24    0    0    0    0   24   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 214, 'amount': 2.0, 'curve': 4},
 {'age': 254, 'amount': 2.75, 'curve': 4},
 {'age': 8, 'amount': 1.05, 'curve': 20},
 {'age': 98, 'amount': 2.8, 'curve': 20},
 {'age': 218, 'amount': 2.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0xd6 0x04 0x6e 0xfe 0x04    \.P..n..
    0008   0x2a 0x08 0x14 0x70 0x62 0x14 0x70 0xda    *..pb.p.
    0010   0x14                                       .
    decimal
             92   17   80  214    4  110  254    4
             42    8   20  112   98   20  112  218
             20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-19T02:39:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 21.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xd8 0x00 0xd8 0x00 0x08 0x00    ........
    decimal
              1    0  216    0  216    0    8    0
    datetime (2013-08-19T02:39:09)
    0000   0x89 0x27 0x42 0x73 0x0d                   .'Bs.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BasalProfileStart 2013-08-19T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-19T04:00:00)
    0000   0x80 0x00 0x04 0x13 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 23 BolusWizard 2013-08-19T07:55:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 42,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 152}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-19T07:55:59)
    0000   0xbb 0x37 0x07 0x73 0x0d                   .7.s.
    body (15)
    hex
    0000   0x2a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    *..n.6..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x36         ......6
    decimal
             42  144    0  110   23   54    0    0
            152    0    0    0    0  152   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 5.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xd8 0x40 0x14                   \..@.
    decimal
             92    5  216   64   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-08-19T07:55:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x00 0x00    ........
    decimal
              1    0  152    0  152    0    0    0
    datetime (2013-08-19T07:55:59)
    0000   0xbb 0x37 0x47 0x73 0x0d                   .7Gs.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 NoDelivery 2013-08-19T08:01:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x05 0x20 0x44                        .. D
    decimal
              6    5   32   68
    datetime (2013-08-19T08:01:00)
    0000   0x80 0x01 0x68 0x13 0x0d                   ..h..
    body (0)

#### RECORD 27 Battery 2013-08-19T08:01:34 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-08-19T08:01:34)
    0000   0xa2 0x01 0x08 0x13 0x0d                   .....
    body (0)

#### RECORD 28 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x03 0x04 0x08                        ....
    decimal
              6    3    4    8
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x08                   .@@..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 29 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x15 0x03 0x62                        ...b
    decimal
              6   21    3   98
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x60 0x01 0x08                   .@`..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 30 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x37 0x02 0xb2                        .7..
    decimal
              6   55    2  178
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x08                   .@@..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 31 Battery 2008-01-01T00:01:29 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2008-01-01T00:01:29)
    0000   0x1d 0x41 0x00 0x01 0x08                   .A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x03 0x04 0x08                        ....
    decimal
              6    3    4    8
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x08                   .@@..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 33 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x15 0x03 0x62                        ...b
    decimal
              6   21    3   98
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x60 0x01 0x08                   .@`..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 34 NoDelivery 2008-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x56 0x02 0xcd                        .V..
    decimal
              6   86    2  205
    datetime (2008-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x08                   .@@..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 35 ClearAlarm 2008-01-01T00:00:11 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x03                                  ..
    decimal
             12    3
    datetime (2008-01-01T00:00:11)
    0000   0x0b 0x40 0x00 0x01 0x08                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 ClearAlarm 2008-01-01T00:00:17 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x15                                  ..
    decimal
             12   21
    datetime (2008-01-01T00:00:17)
    0000   0x11 0x40 0x00 0x01 0x08                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 ChangeTimeDisplay 2008-01-01T00:00:44 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x01                                  d.
    decimal
            100    1
    datetime (2008-01-01T00:00:44)
    0000   0x2c 0x40 0x00 0x01 0x08                   ,@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 ChangeTime 2008-01-01T00:01:11 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2008-01-01T00:01:11)
    0000   0x0b 0x41 0x00 0x01 0x08                   .A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 NewTimeSet 2012-08-19T08:05:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2012-08-19T08:05:00)
    0000   0x80 0x05 0x08 0x13 0x0c                   .....
    body (0)

#### RECORD 40 ResultTotals (2000, 2, 0, 0, 8, 1) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime ((2000, 2, 0, 0, 8, 1))
    0000   0x01 0x88 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 41 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x01 0x88 0x06 0x00 0x00 0x00 0x00    n.......
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110    1  136    6    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 42 Rewind 2012-08-19T08:05:07 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-19T08:05:07)
    0000   0x87 0x05 0x08 0x13 0x0c                   .....
    body (0)

#### RECORD 43 Prime 2012-08-19T08:05:21 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2012-08-19T08:05:21)
    0000   0x95 0x05 0x28 0x13 0x0c                   ..(..
    body (0)

#### RECORD 44 BasalProfileStart 2012-08-19T08:05:35 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-19T08:05:35)
    0000   0xa3 0x05 0x08 0x13 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 45 BasalProfileStart 2012-08-19T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-19T09:30:00)
    0000   0x80 0x1e 0x09 0x13 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 46 BolusWizard 2012-08-19T10:27:54 head[2], body[15] op[0x5b]
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
    datetime (2012-08-19T10:27:54)
    0000   0xb6 0x1b 0x0a 0x73 0x0c                   ...s.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 47 Bolus 2012-08-19T10:27:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2012-08-19T10:27:54)
    0000   0xb6 0x1b 0x4a 0x73 0x0c                   ..Js.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2012-08-19T10:45:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-19T10:45:58)
    0000   0xba 0x2d 0x0a 0x73 0x0c                   .-.s.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x15 0x04                   \.l..
    decimal
             92    5  108   21    4
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2012-08-19T10:45:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x6c 0x00    ..T.T.l.
    decimal
              1    0   84    0   84    0  108    0
    datetime (2012-08-19T10:45:58)
    0000   0xba 0x2d 0x4a 0x73 0x0c                   .-Js.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 Bolus 2012-08-19T10:47:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xc0 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  192    0
    datetime (2012-08-19T10:47:42)
    0000   0xaa 0x2f 0x4a 0x73 0x0c                   ./Js.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 BolusWizard 2012-08-19T12:18:01 head[2], body[15] op[0x5b]
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
    datetime (2012-08-19T12:18:01)
    0000   0x81 0x12 0x0c 0x73 0x0c                   ...s.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 3.1, 'curve': 4},
 {'age': 114, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x7c 0x5e 0x04 0x6c 0x72 0x04    \.|^.lr.
    decimal
             92    8  124   94    4  108  114    4
    datetime (unknown)

    body (0)

#### RECORD 54 Base (2012, 8, 19, 12, 18, 1) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime ((2012, 8, 19, 12, 18, 1))
    0000   0x81 0x12 0x0c 0x13 0x0c                   .....
    body (0)

#### RECORD 55 Base (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0x68 0x00 0x68                   ..h.h
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 56 Base (2003, 2, 12, 18, 1, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x88                                  ..
    decimal
              0  136
    datetime ((2003, 2, 12, 18, 1, 0))
    0000   0x00 0x81 0x12 0x4c 0x73                   ...Ls
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 57 ClearAlarm 2003-02-12T23:45:00 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x5b                                  .[
    decimal
             12   91
    datetime (2003-02-12T23:45:00)
    0000   0x00 0xad 0x37 0x0c 0x73                   ..7.s
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 58 ClearAlarm 2006-08-23T14:00:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x20                                  . 
    decimal
             12   32
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-19.data: 59 records`
