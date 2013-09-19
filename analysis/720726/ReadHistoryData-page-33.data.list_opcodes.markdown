## START analysis/ianj/raw//ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 1016, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa2 0x5d                                  .]
##### DEBUG DECIMAL
            162   93
#### RECORD 0 BolusWizard 2013-07-27T22:33:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 20.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2013-07-27T22:33:03)
    0000   0x43 0xe1 0x16 0x7b 0x0d                   C..{.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0xcc 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  204    0    0   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.0, 'curve': 4},
 {'age': 58, 'amount': 0.7, 'curve': 4},
 {'age': 68, 'amount': 3.5, 'curve': 4},
 {'age': 102, 'amount': 1.8, 'curve': 20},
 {'age': 112, 'amount': 1.85, 'curve': 20},
 {'age': 122, 'amount': 1.55, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x50 0x30 0x04 0x1c 0x3a 0x04    \.P0..:.
    0008   0x8c 0x44 0x04 0x48 0x66 0x14 0x4a 0x70    .D.Hf.Jp
    0010   0x14 0x3e 0x7a 0x14                        .>z.
    decimal
             92   20   80   48    4   28   58    4
            140   68    4   72  102   20   74  112
             20   62  122   20
    datetime (unknown)

    body (0)

#### RECORD 2 BasalProfileStart 2013-07-28T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-28T00:00:00)
    0000   0x40 0xc0 0x00 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 ResultTotals (2000, 6, 0, 0, 13, 59) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xa0                   .....
    decimal
              7    0    0    6  160
    datetime ((2000, 6, 0, 0, 13, 59))
    0000   0x7b 0x8d 0x00 0x00 0x00                   {....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7b 0x8d 0x06 0x00 0xa3 0x6b 0xf8    n{....k.
    0008   0x04 0x00 0x00 0x06 0xa0 0x03 0x52 0x32    ......R2
    0010   0x03 0x4e 0x32 0x00 0xde 0x02 0x92 0x00    .N2.....
    0018   0x50 0x00 0x6c 0x00 0x00 0x08 0x01 0x01    P.l.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  123  141    6    0  163  107  248
              4    0    0    6  160    3   82   50
              3   78   50    0  222    2  146    0
             80    0  108    0    0    8    1    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 5 BasalProfileStart 2013-07-28T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-28T04:00:00)
    0000   0x40 0xc0 0x04 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 NoDelivery 2013-07-28T08:33:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2013-07-28T08:33:00)
    0000   0x40 0xe1 0x48 0xbc 0x0d                   @.H..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 7 ClearAlarm 2013-07-28T08:33:11 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2013-07-28T08:33:11)
    0000   0x4b 0xe1 0x08 0x1c 0x0d                   K....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BasalProfileStart 2013-07-28T08:33:11 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-28T08:33:11)
    0000   0x4b 0xe1 0x08 0x1c 0x0d                   K....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BasalProfileStart 2013-07-28T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-28T09:30:00)
    0000   0x40 0xde 0x09 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 10 Ian69 2013-07-28T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-28T10:30:00)
    0000   0x40 0xde 0x0a 0x1c 0x0d                   @....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BolusWizard 2013-07-28T10:50:07 head[2], body[15] op[0x5b]
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
    datetime (2013-07-28T10:50:07)
    0000   0x47 0xf2 0x0a 0x7c 0x0d                   G..|.
    body (15)
    hex
    0000   0x2a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    *..n.6..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x36         ......6
    decimal
             42  144    0  110   23   54    0    0
            152    0    0    0    0  152   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Bolus 2013-07-28T10:50:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x00 0x00    ........
    decimal
              1    0  152    0  152    0    0    0
    datetime (2013-07-28T10:50:07)
    0000   0x47 0xf2 0x4a 0x7c 0x0d                   G.J|.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-07-28T11:31:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-28T11:31:40)
    0000   0x68 0xdf 0x0b 0x7c 0x0d                   h..|.
    body (15)
    hex
    0000   0x0b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x36         (....(6
    decimal
             11  144    0  110   23   54    0    0
             40    0    0    0    0   40   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 3.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x98 0x2e 0x04                   \....
    decimal
             92    5  152   46    4
    datetime (unknown)

    body (0)

#### RECORD 15 Ian69 2013-07-28T11:31:40 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-07-28T11:31:40)
    0000   0x68 0xdf 0x0b 0x1c 0x0d                   h....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [1, 1, 0]
#### RECORD 16 Bolus 2013-07-28T11:31:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x88 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  136    0
    datetime (2013-07-28T11:31:40)
    0000   0x68 0xdf 0x4b 0x7c 0x0d                   h.K|.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 CalBGForPH 2013-07-28T12:19:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-07-28T12:19:32)
    0000   0x60 0xd3 0x2c 0x7c 0x0d                   `.,|.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 Ian3F 2013-07-28T12:19:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2013-07-28T12:19:32)
    0000   0x60 0xd3 0x0c 0x7c 0x0d                   `..|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2013-07-28T12:20:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 12.8,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 9.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-07-28T12:20:12)
    0000   0x4c 0xd4 0x0c 0x7c 0x0d                   L..|.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x60 0x00    ...n.6`.
    0008   0x6c 0x00 0x00 0x80 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54   96    0
            108    0    0  128    0  108   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 1.0, 'curve': 4},
 {'age': 95, 'amount': 3.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x37 0x04 0x98 0x5f 0x04    \.(7.._.
    decimal
             92    8   40   55    4  152   95    4
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-07-28T12:20:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x80 0x00    ..l.l...
    decimal
              1    0  108    0  108    0  128    0
    datetime (2013-07-28T12:20:12)
    0000   0x4c 0xd4 0x4c 0x7c 0x0d                   L.L|.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 BasalProfileStart 2013-07-28T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-28T13:00:00)
    0000   0x40 0xc0 0x0d 0x1c 0x0d                   @....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
#### RECORD 23 CalBGForPH 2013-07-28T16:20:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2013-07-28T16:20:00)
    0000   0x40 0xd4 0x30 0x7c 0x0d                   @.0|.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 Ian3F 2013-07-28T16:20:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2013-07-28T16:20:00)
    0000   0x40 0xd4 0xd0 0x7c 0x0d                   @..|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 BolusWizard 2013-07-28T18:23:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-28T18:23:49)
    0000   0x71 0xd7 0x12 0x7c 0x0d                   q..|.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 2.7, 'curve': 20},
 {'age': 162, 'amount': 1.0, 'curve': 20},
 {'age': 202, 'amount': 3.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x70 0x14 0x28 0xa2 0x14    \.lp.(..
    0008   0x98 0xca 0x14                             ...
    decimal
             92   11  108  112   20   40  162   20
            152  202   20
    datetime (unknown)

    body (0)

#### RECORD 27 Ian69 2013-07-28T18:23:49 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-28T18:23:49)
    0000   0x71 0xd7 0x72 0x1c 0x0d                   q.r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [1, 1, 0]
#### RECORD 28 Bolus 2013-07-28T18:23:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-07-28T18:23:49)
    0000   0x71 0xd7 0x52 0x7c 0x0d                   q.R|.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2013-07-28T19:43:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 388}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-07-28T19:43:08)
    0000   0x48 0xeb 0x33 0x7c 0x8d                   H.3|.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 Ian3F 2013-07-28T19:43:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x30                                  ?0
    decimal
             63   48
    datetime (2013-07-28T19:43:08)
    0000   0x48 0xeb 0x93 0x7c 0x0d                   H..|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-07-28T19:43:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 215,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 3.2,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0xd7                                  [.
    decimal
             91  215
    datetime (2013-07-28T19:43:21)
    0000   0x55 0xeb 0x13 0x7c 0x0d                   U..|.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x18 0x00    #..n.6..
    0008   0x7c 0x08 0x00 0x20 0x01 0x74 0x36         |.. .t6
    decimal
             35  144    0  110   23   54   24    0
            124    8    0   32    1  116   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.2, 'curve': 4},
 {'age': 192, 'amount': 2.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x58 0x04 0x6c 0xc0 0x14    \.0X.l..
    decimal
             92    8   48   88    4  108  192   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-07-28T19:43:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x74 0x01 0x74 0x00 0x20 0x00    ..t.t. .
    decimal
              1    1  116    1  116    0   32    0
    datetime (2013-07-28T19:43:21)
    0000   0x55 0xeb 0x53 0x7c 0x0d                   U.S|.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2013-07-28T21:25:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 34,
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
    datetime (2013-07-28T21:25:54)
    0000   0x76 0xd9 0x15 0x7c 0x0d                   v..|.
    body (15)
    hex
    0000   0x22 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    "..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             34  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 5.05, 'curve': 4},
 {'age': 110, 'amount': 4.25, 'curve': 4},
 {'age': 190, 'amount': 1.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0xca 0x64 0x04 0xaa 0x6e 0x04    \..d..n.
    0008   0x30 0xbe 0x04                             0..
    decimal
             92   11  202  100    4  170  110    4
             48  190    4
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-07-28T21:25:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xd8 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  216    0
    datetime (2013-07-28T21:25:54)
    0000   0x76 0xd9 0x55 0x7c 0x0d                   v.U|.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 BolusWizard 2013-07-28T21:44:38 head[2], body[15] op[0x5b]
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
    datetime (2013-07-28T21:44:38)
    0000   0x66 0xec 0x15 0x7c 0x0d                   f..|.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 3.0, 'curve': 4},
 {'age': 119, 'amount': 5.05, 'curve': 4},
 {'age': 129, 'amount': 4.25, 'curve': 4},
 {'age': 209, 'amount': 1.2, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x13 0x04 0xca 0x77 0x04    \.x...w.
    0008   0xaa 0x81 0x04 0x30 0xd1 0x04              ...0..
    decimal
             92   14  120   19    4  202  119    4
            170  129    4   48  209    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-07-28T21:44:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x01 0x20 0x00    ..H.H. .
    decimal
              1    0   72    0   72    1   32    0
    datetime (2013-07-28T21:44:38)
    0000   0x66 0xec 0x55 0x7c 0x0d                   f.U|.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 CalBGForPH 2013-07-28T23:34:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 158}
```
    op hex (2)
    0000   0x0a 0x9e                                  ..
    decimal
             10  158
    datetime (2013-07-28T23:34:56)
    0000   0x78 0xe2 0x37 0x7c 0x0d                   x.7|.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2013-07-28T23:34:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-07-28T23:34:56)
    0000   0x78 0xe2 0xd7 0x7c 0x0d                   x..|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BasalProfileStart 2013-07-29T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-29T00:00:00)
    0000   0x40 0xc0 0x00 0x1d 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 43 ResultTotals (2000, 6, 0, 0, 13, 60) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x19                   .....
    decimal
              7    0    0    7   25
    datetime ((2000, 6, 0, 0, 13, 60))
    0000   0x7c 0x8d 0x00 0x00 0x00                   |....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7c 0x8d 0x06 0x10 0xe4 0x9e 0x84    n|......
    0008   0x04 0x00 0x00 0x07 0x19 0x03 0x89 0x32    .......2
    0010   0x03 0x90 0x32 0x00 0xba 0x02 0x1c 0x00    ..2.....
    0018   0x00 0x01 0x74 0x00 0x00 0x06 0x00 0x01    ..t.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  124  141    6   16  228  158  132
              4    0    0    7   25    3  137   50
              3  144   50    0  186    2   28    0
              0    1  116    0    0    6    0    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 45 CalBGForPH 2013-07-29T01:42:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2013-07-29T01:42:56)
    0000   0x78 0xea 0x21 0x7d 0x0d                   x.!}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2013-07-29T01:42:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-07-29T01:42:56)
    0000   0x78 0xea 0x81 0x7d 0x0d                   x..}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-07-29T01:43:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 82,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 4.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x52                                  [R
    decimal
             91   82
    datetime (2013-07-29T01:43:03)
    0000   0x43 0xeb 0x01 0x7d 0x0d                   C..}.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x30 0x00    ...n.60.
    0008   0x00 0x00 0x00 0x04 0x00 0x2c 0x36         .....,6
    decimal
              0  144    0  110   23   54   48    0
              0    0    0    4    0   44   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 238, 'amount': 1.25, 'curve': 4},
 {'age': 248, 'amount': 0.55, 'curve': 4},
 {'age': 2, 'amount': 3.0, 'curve': 20},
 {'age': 102, 'amount': 5.05, 'curve': 20},
 {'age': 112, 'amount': 4.25, 'curve': 20},
 {'age': 192, 'amount': 1.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x32 0xee 0x04 0x16 0xf8 0x04    \.2.....
    0008   0x78 0x02 0x14 0xca 0x66 0x14 0xaa 0x70    x...f..p
    0010   0x14 0x30 0xc0 0x14                        .0..
    decimal
             92   20   50  238    4   22  248    4
            120    2   20  202  102   20  170  112
             20   48  192   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-07-29T01:43:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x04 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    4    0
    datetime (2013-07-29T01:43:03)
    0000   0x43 0xeb 0x41 0x7d 0x0d                   C.A}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 BolusWizard 2013-07-29T02:02:45 head[2], body[15] op[0x5b]
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
    datetime (2013-07-29T02:02:45)
    0000   0x6d 0xc2 0x02 0x7d 0x0d                   m..}.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 1.1, 'curve': 4},
 {'age': 1, 'amount': 1.25, 'curve': 20},
 {'age': 11, 'amount': 0.55, 'curve': 20},
 {'age': 21, 'amount': 3.0, 'curve': 20},
 {'age': 121, 'amount': 5.05, 'curve': 20},
 {'age': 131, 'amount': 4.25, 'curve': 20},
 {'age': 211, 'amount': 1.2, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x2c 0x1b 0x04 0x32 0x01 0x14    \.,..2..
    0008   0x16 0x0b 0x14 0x78 0x15 0x14 0xca 0x79    ...x...y
    0010   0x14 0xaa 0x83 0x14 0x30 0xd3 0x14         ....0..
    decimal
             92   23   44   27    4   50    1   20
             22   11   20  120   21   20  202  121
             20  170  131   20   48  211   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-07-29T02:02:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x2c 0x00    ..h.h.,.
    decimal
              1    0  104    0  104    0   44    0
    datetime (2013-07-29T02:02:46)
    0000   0x6e 0xc2 0x42 0x7d 0x0d                   n.B}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 BasalProfileStart 2013-07-29T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-29T04:00:00)
    0000   0x40 0xc0 0x04 0x1d 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 54 CalBGForPH 2013-07-29T08:05:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-07-29T08:05:44)
    0000   0x6c 0xc5 0x28 0x7d 0x0d                   l.(}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 Ian3F 2013-07-29T08:05:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-07-29T08:05:44)
    0000   0x6c 0xc5 0x28 0x7d 0x0d                   l.(}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 BolusWizard 2013-07-29T08:40:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 31,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T08:40:28)
    0000   0x5c 0xe8 0x08 0x7d 0x0d                   \..}.
    body (15)
    hex
    0000   0x1f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x70 0x00 0x00 0x00 0x00 0x70 0x36         p....p6
    decimal
             31  144    0  110   23   54    0    0
            112    0    0    0    0  112   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 149, 'amount': 2.6, 'curve': 20},
 {'age': 169, 'amount': 1.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0x95 0x14 0x2c 0xa9 0x14    \.h..,..
    decimal
             92    8  104  149   20   44  169   20
    datetime (unknown)

    body (0)

#### RECORD 58 Ian69 2013-07-29T08:40:29 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-29T08:40:29)
    0000   0x5d 0xe8 0x08 0x1d 0x0d                   ]....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [1, 1, 1]
#### RECORD 59 Bolus 2013-07-29T08:40:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x00 0x00    ..p.p...
    decimal
              1    0  112    0  112    0    0    0
    datetime (2013-07-29T08:40:28)
    0000   0x5c 0xe8 0x48 0x7d 0x0d                   \.H}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 BasalProfileStart 2013-07-29T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-29T09:30:00)
    0000   0x40 0xde 0x09 0x1d 0x0d                   @....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 BolusWizard 2013-07-29T11:36:59 head[2], body[15] op[0x5b]
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
    datetime (2013-07-29T11:36:59)
    0000   0x7b 0xe4 0x0b 0x7d 0x0d                   {..}.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 2.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0xb5 0x04                   \.p..
    decimal
             92    5  112  181    4
    datetime (unknown)

    body (0)

#### RECORD 63 Ian69 2013-07-29T11:37:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-07-29T11:37:00)
    0000   0x40 0xe5 0x0b 0x1d 0x0d                   @....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [1, 1, 1]
#### RECORD 64 Bolus 2013-07-29T11:37:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x14 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   20    0
    datetime (2013-07-29T11:37:00)
    0000   0x40 0xe5 0x4b 0x7d 0x0d                   @.K}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 CalBGForPH 2013-07-29T11:57:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 55}
```
    op hex (2)
    0000   0x0a 0x37                                  .7
    decimal
             10   55
    datetime (2013-07-29T11:57:40)
    0000   0x68 0xf9 0x4b 0x1d 0x0d                   h.K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 BolusWizard 2013-07-29T11:57:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 55,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 13.2,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x37                                  [7
    decimal
             91   55
    datetime (2013-07-29T11:57:56)
    0000   0x78 0xf9 0x0b 0x7d 0x0d                   x..}.
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x3c 0x00 0x00 0x84 0x00 0x3c 0x36         <....<6
    decimal
             17  144    0  110   23   54    0    0
             60    0    0  132    0   60   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 3.0, 'curve': 4},
 {'age': 202, 'amount': 2.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0x16 0x04 0x70 0xca 0x04    \.x..p..
    decimal
             92    8  120   22    4  112  202    4
    datetime (unknown)

    body (0)

#### RECORD 68 CalBGForPH 2013-07-29T12:01:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 280}
```
    op hex (2)
    0000   0x0a 0x18                                  ..
    decimal
             10   24
    datetime (2013-07-29T12:01:58)
    0000   0x7a 0xc1 0x2c 0x7d 0x8d                   z.,}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 Ian3F 2013-07-29T12:01:58 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2013-07-29T12:01:58)
    0000   0x7a 0xc1 0x0c 0x7d 0x0d                   z..}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 70 BolusWizard 2013-07-29T12:02:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 155,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 12.8,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 17.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2013-07-29T12:02:14)
    0000   0x4e 0xc2 0x0c 0x7d 0x0d                   N..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0xac 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x80 0x00 0x74 0x36         H....t6
    decimal
             20  144    0  110   23   54  172    0
             72    0    0  128    0  116   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 3.0, 'curve': 4},
 {'age': 207, 'amount': 2.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0x1b 0x04 0x70 0xcf 0x04    \.x..p..
    decimal
             92    8  120   27    4  112  207    4
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-07-29T12:02:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x80 0x00    ..t.t...
    decimal
              1    0  116    0  116    0  128    0
    datetime (2013-07-29T12:02:14)
    0000   0x4e 0xc2 0x4c 0x7d 0x0d                   N.L}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 73 BasalProfileStart 2013-07-29T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-29T13:00:00)
    0000   0x40 0xc0 0x0d 0x1d 0x0d                   @....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
`end analysis/ianj/raw//ReadHistoryData-page-33.data: 74 records`
