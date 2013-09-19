## START analysis/ianj/raw//ReadHistoryData-page-32.data
#### RECORD 0 BolusWizard 2013-07-29T14:12:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T14:12:39)
    0000   0x67 0xcc 0x0e 0x7d 0x0d                   g..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 2.9, 'curve': 4},
 {'age': 157, 'amount': 3.0, 'curve': 4},
 {'age': 81, 'amount': 2.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x89 0x04 0x78 0x9d 0x04    \.t..x..
    0008   0x70 0x51 0x14                             pQ.
    decimal
             92   11  116  137    4  120  157    4
            112   81   20
    datetime (unknown)

    body (0)

#### RECORD 2 BolusWizard 2013-07-29T14:12:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T14:12:41)
    0000   0x69 0xcc 0x0e 0x7d 0x0d                   i..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 2.9, 'curve': 4},
 {'age': 157, 'amount': 3.0, 'curve': 4},
 {'age': 81, 'amount': 2.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x89 0x04 0x78 0x9d 0x04    \.t..x..
    0008   0x70 0x51 0x14                             pQ.
    decimal
             92   11  116  137    4  120  157    4
            112   81   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-07-29T14:12:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x4c 0x00    ..H.H.L.
    decimal
              1    0   72    0   72    0   76    0
    datetime (2013-07-29T14:12:41)
    0000   0x69 0xcc 0x4e 0x7d 0x0d                   i.N}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 CalBGForPH 2013-07-29T14:51:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-07-29T14:51:04)
    0000   0x44 0xf3 0x2e 0x7d 0x0d                   D..}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Ian3F 2013-07-29T14:51:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2013-07-29T14:51:04)
    0000   0x44 0xf3 0x0e 0x7d 0x0d                   D..}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH 2013-07-29T16:06:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-07-29T16:06:32)
    0000   0x60 0xc6 0x30 0x7d 0x0d                   `.0}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2013-07-29T16:06:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2013-07-29T16:06:32)
    0000   0x60 0xc6 0x10 0x7d 0x0d                   `..}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2013-07-29T16:06:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 3.6,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 11.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-07-29T16:06:45)
    0000   0x6d 0xc6 0x10 0x7d 0x0d                   m..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x70 0x00    ...n.6p.
    0008   0x48 0x00 0x00 0x24 0x00 0x94 0x36         H..$..6
    decimal
             20  144    0  110   23   54  112    0
             72    0    0   36    0  148   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.8, 'curve': 4},
 {'age': 251, 'amount': 2.9, 'curve': 4},
 {'age': 15, 'amount': 3.0, 'curve': 20},
 {'age': 195, 'amount': 2.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x79 0x04 0x74 0xfb 0x04    \.Hy.t..
    0008   0x78 0x0f 0x14 0x70 0xc3 0x14              x..p..
    decimal
             92   14   72  121    4  116  251    4
            120   15   20  112  195   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-07-29T16:06:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x24 0x00    ......$.
    decimal
              1    0  180    0  180    0   36    0
    datetime (2013-07-29T16:06:45)
    0000   0x6d 0xc6 0x50 0x7d 0x0d                   m.P}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2013-07-29T19:13:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-07-29T19:13:04)
    0000   0x44 0xcd 0x33 0x7d 0x0d                   D.3}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian3F 2013-07-29T19:13:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-07-29T19:13:04)
    0000   0x44 0xcd 0x93 0x7d 0x0d                   D..}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 BolusWizard 2013-07-29T19:21:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 42,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.4,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 23.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x2a                                  [*
    decimal
             91   42
    datetime (2013-07-29T19:21:04)
    0000   0x44 0xd5 0x13 0x7d 0x0d                   D..}.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0xec 0x00    ...n.6..
    0008   0x64 0xf8 0x00 0x18 0x00 0x50 0x36         d....P6
    decimal
             28  144    0  110   23   54  236    0
            100  248    0   24    0   80   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 196, 'amount': 4.5, 'curve': 4},
 {'age': 60, 'amount': 1.8, 'curve': 20},
 {'age': 190, 'amount': 2.9, 'curve': 20},
 {'age': 210, 'amount': 3.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xb4 0xc4 0x04 0x48 0x3c 0x14    \....H<.
    0008   0x74 0xbe 0x14 0x78 0xd2 0x14              t..x..
    decimal
             92   14  180  196    4   72   60   20
            116  190   20  120  210   20
    datetime (unknown)

    body (0)

#### RECORD 16 Ian69 2013-07-29T19:21:04 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-29T19:21:04)
    0000   0x44 0xd5 0x73 0x1d 0x0d                   D.s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [1, 1, 0]
#### RECORD 17 Bolus 2013-07-29T19:21:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x18 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   24    0
    datetime (2013-07-29T19:21:04)
    0000   0x44 0xd5 0x53 0x7d 0x0d                   D.S}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 BolusWizard 2013-07-29T19:44:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T19:44:52)
    0000   0x74 0xec 0x13 0x7d 0x0d                   t..}.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 2.0, 'curve': 4},
 {'age': 219, 'amount': 4.5, 'curve': 4},
 {'age': 83, 'amount': 1.8, 'curve': 20},
 {'age': 213, 'amount': 2.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x1d 0x04 0xb4 0xdb 0x04    \.P.....
    0008   0x48 0x53 0x14 0x74 0xd5 0x14              HS.t..
    decimal
             92   14   80   29    4  180  219    4
             72   83   20  116  213   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-07-29T19:44:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x5c 0x00    ..L.L.\.
    decimal
              1    0   76    0   76    0   92    0
    datetime (2013-07-29T19:44:52)
    0000   0x74 0xec 0x53 0x7d 0x0d                   t.S}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 BolusWizard 2013-07-29T20:39:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T20:39:45)
    0000   0x6d 0xe7 0x14 0x7d 0x0d                   m..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 1.7, 'curve': 4},
 {'age': 64, 'amount': 0.2, 'curve': 4},
 {'age': 84, 'amount': 2.0, 'curve': 4},
 {'age': 18, 'amount': 4.5, 'curve': 20},
 {'age': 138, 'amount': 1.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x36 0x04 0x08 0x40 0x04    \.D6..@.
    0008   0x50 0x54 0x04 0xb4 0x12 0x14 0x48 0x8a    PT....H.
    0010   0x14                                       .
    decimal
             92   17   68   54    4    8   64    4
             80   84    4  180   18   20   72  138
             20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-07-29T20:39:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x78 0x00    ..X.X.x.
    decimal
              1    0   88    0   88    0  120    0
    datetime (2013-07-29T20:39:45)
    0000   0x6d 0xe7 0x54 0x7d 0x0d                   m.T}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-07-29T22:27:35 head[2], body[15] op[0x5b]
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
    datetime (2013-07-29T22:27:35)
    0000   0x63 0xdb 0x16 0x7d 0x0d                   c..}.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 2.2, 'curve': 4},
 {'age': 162, 'amount': 1.7, 'curve': 4},
 {'age': 172, 'amount': 0.2, 'curve': 4},
 {'age': 192, 'amount': 2.0, 'curve': 4},
 {'age': 126, 'amount': 4.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x70 0x04 0x44 0xa2 0x04    \.Xp.D..
    0008   0x08 0xac 0x04 0x50 0xc0 0x04 0xb4 0x7e    ...P...~
    0010   0x14                                       .
    decimal
             92   17   88  112    4   68  162    4
              8  172    4   80  192    4  180  126
             20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-07-29T22:27:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x4c 0x00    ..d.d.L.
    decimal
              1    0  100    0  100    0   76    0
    datetime (2013-07-29T22:27:35)
    0000   0x63 0xdb 0x56 0x7d 0x0d                   c.V}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2013-07-29T23:57:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-29T23:57:16)
    0000   0x50 0xf9 0x37 0x7d 0x0d                   P.7}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2013-07-29T23:57:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2013-07-29T23:57:16)
    0000   0x50 0xf9 0x57 0x7d 0x0d                   P.W}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2013-07-30T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-30T00:00:00)
    0000   0x40 0xc0 0x00 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 30 ResultTotals (2000, 6, 0, 0, 13, 61) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xcd                   .....
    decimal
              7    0    0    7  205
    datetime ((2000, 6, 0, 0, 13, 61))
    0000   0x7d 0x8d 0x00 0x00 0x00                   }....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7d 0x8d 0x06 0x10 0x8d 0x49 0x18    n}....I.
    0008   0x08 0x00 0x00 0x07 0xcd 0x03 0x89 0x2d    .......-
    0010   0x04 0x44 0x37 0x00 0xfa 0x02 0x98 0x00    .D7.....
    0018   0x2c 0x01 0x80 0x00 0x00 0x07 0x01 0x03    ,.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x63 0x63 0x00 0x00 0x00         ..cc...
    decimal
            110  125  141    6   16  141   73   24
              8    0    0    7  205    3  137   45
              4   68   55    0  250    2  152    0
             44    1  128    0    0    7    1    3
              0    0    0    0    0    0    0    0
              0    0   99   99    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 32 BasalProfileStart 2013-07-30T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-30T04:00:00)
    0000   0x40 0xc0 0x04 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 33 CalBGForPH 2013-07-30T08:04:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 238}
```
    op hex (2)
    0000   0x0a 0xee                                  ..
    decimal
             10  238
    datetime (2013-07-30T08:04:42)
    0000   0x6a 0xc4 0x28 0x7e 0x0d                   j.(~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 Ian3F 2013-07-30T08:04:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2013-07-30T08:04:42)
    0000   0x6a 0xc4 0xc8 0x7e 0x0d                   j..~.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2013-07-30T08:04:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 13.2,
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
    datetime (2013-07-30T08:04:50)
    0000   0x72 0xc4 0x08 0x7e 0x0d                   r..~.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x84 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x84 0x36         ......6
    decimal
              0  144    0  110   23   54  132    0
              0    0    0    0    0  132   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 Ian69 2013-07-30T08:04:50 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-30T08:04:50)
    0000   0x72 0xc4 0x08 0x1e 0x0d                   r....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [1, 1, 0]
#### RECORD 37 Bolus 2013-07-30T08:04:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x00 0x00    ........
    decimal
              1    0  132    0  132    0    0    0
    datetime (2013-07-30T08:04:50)
    0000   0x72 0xc4 0x48 0x7e 0x0d                   r.H~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2013-07-30T08:25:47 head[2], body[15] op[0x5b]
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
    datetime (2013-07-30T08:25:47)
    0000   0x6f 0xd9 0x08 0x7e 0x0d                   o..~.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 3.05, 'curve': 4},
 {'age': 30, 'amount': 0.25, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x7a 0x14 0x04 0x0a 0x1e 0x04    \.z.....
    decimal
             92    8  122   20    4   10   30    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-07-30T08:25:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x84 0x00    ..X.X...
    decimal
              1    0   88    0   88    0  132    0
    datetime (2013-07-30T08:25:47)
    0000   0x6f 0xd9 0x48 0x7e 0x0d                   o.H~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 BasalProfileStart 2013-07-30T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-30T09:30:00)
    0000   0x40 0xde 0x09 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 42 PumpSuspend 2013-07-30T09:57:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-07-30T09:57:59)
    0000   0x7b 0xf9 0x09 0x1e 0x0d                   {....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 BasalProfileStart 2013-07-30T11:00:10 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-30T11:00:10)
    0000   0x4a 0xc0 0x0b 0x1e 0x0d                   J....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 44 PumpResume 2013-07-30T11:00:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-07-30T11:00:10)
    0000   0x4a 0xc0 0x0b 0x1e 0x0d                   J....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 CalBGForPH 2013-07-30T11:42:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 326}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-07-30T11:42:52)
    0000   0x74 0xea 0x2b 0x7e 0x8d                   t.+~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 46 Ian3F 2013-07-30T11:42:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x28                                  ?(
    decimal
             63   40
    datetime (2013-07-30T11:42:52)
    0000   0x74 0xea 0xcb 0x7e 0x0d                   t..~.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-07-30T11:43:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 181,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 22.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2013-07-30T11:43:00)
    0000   0x40 0xeb 0x0b 0x7e 0x0d                   @..~.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xdc 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x18 0x00 0xc4 0x36         ......6
    decimal
              0  144    0  110   23   54  220    0
              0    0    0   24    0  196   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 198, 'amount': 2.2, 'curve': 4},
 {'age': 218, 'amount': 3.05, 'curve': 4},
 {'age': 228, 'amount': 0.25, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0xc6 0x04 0x7a 0xda 0x04    \.X..z..
    0008   0x0a 0xe4 0x04                             ...
    decimal
             92   11   88  198    4  122  218    4
             10  228    4
    datetime (unknown)

    body (0)

#### RECORD 49 Ian69 2013-07-30T11:43:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-07-30T11:43:00)
    0000   0x40 0xeb 0x0b 0x1e 0x0d                   @....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [1, 1, 1]
#### RECORD 50 Bolus 2013-07-30T11:43:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 19.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc4 0x00 0xc4 0x00 0x18 0x00    ........
    decimal
              1    0  196    0  196    0   24    0
    datetime (2013-07-30T11:43:00)
    0000   0x40 0xeb 0x4b 0x7e 0x0d                   @.K~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2013-07-30T12:21:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-30T12:21:47)
    0000   0x6f 0xd5 0x0c 0x7e 0x0d                   o..~.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 1.95, 'curve': 4},
 {'age': 46, 'amount': 2.95, 'curve': 4},
 {'age': 236, 'amount': 2.2, 'curve': 4},
 {'age': 0, 'amount': 3.05, 'curve': 20},
 {'age': 10, 'amount': 0.25, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x4e 0x24 0x04 0x76 0x2e 0x04    \.N$.v..
    0008   0x58 0xec 0x04 0x7a 0x00 0x14 0x0a 0x0a    X..z....
    0010   0x14                                       .
    decimal
             92   17   78   36    4  118   46    4
             88  236    4  122    0   20   10   10
             20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-07-30T12:21:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xb8 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  184    0
    datetime (2013-07-30T12:21:47)
    0000   0x6f 0xd5 0x4c 0x7e 0x0d                   o.L~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 54 BasalProfileStart 2013-07-30T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-30T13:00:00)
    0000   0x40 0xc0 0x0d 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
#### RECORD 55 BolusWizard 2013-07-30T15:32:55 head[2], body[15] op[0x5b]
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
    datetime (2013-07-30T15:32:55)
    0000   0x77 0xe0 0x0f 0x7e 0x0d                   w..~.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 3.0, 'curve': 4},
 {'age': 227, 'amount': 1.95, 'curve': 4},
 {'age': 237, 'amount': 2.95, 'curve': 4},
 {'age': 171, 'amount': 2.2, 'curve': 20},
 {'age': 191, 'amount': 3.05, 'curve': 20},
 {'age': 201, 'amount': 0.25, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x78 0xc5 0x04 0x4e 0xe3 0x04    \.x..N..
    0008   0x76 0xed 0x04 0x58 0xab 0x14 0x7a 0xbf    v..X..z.
    0010   0x14 0x0a 0xc9 0x14                        ....
    decimal
             92   20  120  197    4   78  227    4
            118  237    4   88  171   20  122  191
             20   10  201   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2013-07-30T15:32:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x1c 0x00    ..h.h...
    decimal
              1    0  104    0  104    0   28    0
    datetime (2013-07-30T15:32:55)
    0000   0x77 0xe0 0x4f 0x7e 0x0d                   w.O~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2013-07-30T15:43:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2013-07-30T15:43:24)
    0000   0x58 0xeb 0x2f 0x7e 0x0d                   X./~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 Ian3F 2013-07-30T15:43:24 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2013-07-30T15:43:24)
    0000   0x58 0xeb 0xef 0x7e 0x0d                   X..~.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 BolusWizard 2013-07-30T18:51:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 39,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 140}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-30T18:51:49)
    0000   0x71 0xf3 0x12 0x7e 0x0d                   q..~.
    body (15)
    hex
    0000   0x27 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    '..n.6..
    0008   0x8c 0x00 0x00 0x00 0x00 0x8c 0x36         ......6
    decimal
             39  144    0  110   23   54    0    0
            140    0    0    0    0  140   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 2.6, 'curve': 4},
 {'age': 140, 'amount': 3.0, 'curve': 20},
 {'age': 170, 'amount': 1.95, 'curve': 20},
 {'age': 180, 'amount': 2.95, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0xce 0x04 0x78 0x8c 0x14    \.h..x..
    0008   0x4e 0xaa 0x14 0x76 0xb4 0x14              N..v..
    decimal
             92   14  104  206    4  120  140   20
             78  170   20  118  180   20
    datetime (unknown)

    body (0)

#### RECORD 62 Ian69 2013-07-30T18:51:50 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-30T18:51:50)
    0000   0x72 0xf3 0x72 0x1e 0x0d                   r.r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [1, 1, 1]
#### RECORD 63 Bolus 2013-07-30T18:51:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x0c 0x00    ........
    decimal
              1    0  140    0  140    0   12    0
    datetime (2013-07-30T18:51:50)
    0000   0x72 0xf3 0x52 0x7e 0x0d                   r.R~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 LowReservoir 2013-07-30T20:45:47 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2013-07-30T20:45:47)
    0000   0x6f 0xed 0x14 0x1e 0x8d                   o....
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 65 CalBGForPH 2013-07-30T20:51:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-07-30T20:51:42)
    0000   0x6a 0xf3 0x34 0x7e 0x0d                   j.4~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 Ian3F 2013-07-30T20:51:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2013-07-30T20:51:42)
    0000   0x6a 0xf3 0x74 0x7e 0x0d                   j.t~.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 BolusWizard 2013-07-30T21:42:23 head[2], body[15] op[0x5b]
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
    datetime (2013-07-30T21:42:23)
    0000   0x57 0xea 0x15 0x7e 0x0d                   W..~.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 3.5, 'curve': 4},
 {'age': 121, 'amount': 2.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x8c 0xb1 0x04 0x68 0x79 0x14    \....hy.
    decimal
             92    8  140  177    4  104  121   20
    datetime (unknown)

    body (0)

#### RECORD 69 CalBGForPH 2013-07-30T22:41:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 322}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-07-30T22:41:54)
    0000   0x76 0xe9 0x36 0x7e 0x8d                   v.6~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 Ian3F 2013-07-30T22:41:54 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x28                                  ?(
    decimal
             63   40
    datetime (2013-07-30T22:41:54)
    0000   0x76 0xe9 0x56 0x7e 0x0d                   v.V~.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 71 BolusWizard 2013-07-30T22:42:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 179,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 21.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0xb3                                  [.
    decimal
             91  179
    datetime (2013-07-30T22:42:07)
    0000   0x47 0xea 0x16 0x7e 0x0d                   G..~.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0xd8 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x08 0x01 0x18 0x36         H.....6
    decimal
             20  144    0  110   23   54  216    0
             72    0    0    8    1   24   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 237, 'amount': 3.5, 'curve': 4},
 {'age': 181, 'amount': 2.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x8c 0xed 0x04 0x68 0xb5 0x14    \....h..
    decimal
             92    8  140  237    4  104  181   20
    datetime (unknown)

    body (0)

#### RECORD 73 LowReservoir 2013-07-30T22:42:07 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 19.2}
```
    op hex (2)
    0000   0x34 0xc0                                  4.
    decimal
             52  192
    datetime (2013-07-30T22:42:07)
    0000   0x47 0xea 0x96 0x1e 0x8d                   G....
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 74 Bolus 2013-07-30T22:42:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x08 0x00    ........
    decimal
              1    1   24    1   24    0    8    0
    datetime (2013-07-30T22:42:07)
    0000   0x47 0xea 0x56 0x7e 0x0d                   G.V~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 BasalProfileStart 2013-07-31T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-31T00:00:00)
    0000   0x40 0xc0 0x00 0x1f 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 76 Base unknown head[2], body[0] op[0xe4]

    op hex (2)
    0000   0xe4 0x62                                  .b
    decimal
            228   98
    datetime (unknown)

    body (0)

`end analysis/ianj/raw//ReadHistoryData-page-32.data: 77 records`
