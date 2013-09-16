## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 168, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1c 0x00 0xe4 0x36 0x5c 0x14 0x60 0x9e    ...6\.`.
    0008   0x04 0x30 0x20 0x14 0x34 0x2a 0x14 0x24    .0 .4*.$
    0010   0x8e 0x14 0x64 0xca 0x14 0x7c 0xde 0x14    ..d..|..
    0018   0x69 0xd1 0xa7 0x20 0x72 0x16 0x0c 0x15    i.. r...
##### DEBUG DECIMAL
             28    0  228   54   92   20   96  158
              4   48   32   20   52   42   20   36
            142   20  100  202   20  124  222   20
            105  209  167   32  114   22   12   21
#### RECORD 0 BolusWizard 2012-08-22T13:47:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 52,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.8,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x34                                  [4
    decimal
             91   52
    datetime (2012-08-22T13:47:06)
    0000   0x86 0x2f 0x0d 0x76 0x0c                   ./.v.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x24 0xf8 0x00 0x6c 0x00 0x20 0x36         $..l. 6
    decimal
             10  144    0  110   23   54  252    0
             36  248    0  108    0   32   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 1.3, 'curve': 4},
 {'age': 113, 'amount': 0.9, 'curve': 4},
 {'age': 173, 'amount': 2.5, 'curve': 4},
 {'age': 193, 'amount': 3.1, 'curve': 4},
 {'age': 87, 'amount': 1.8, 'curve': 20},
 {'age': 107, 'amount': 2.7, 'curve': 20},
 {'age': 147, 'amount': 1.9, 'curve': 20},
 {'age': 207, 'amount': 4.8, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x34 0x0d 0x04 0x24 0x71 0x04    \.4..$q.
    0008   0x64 0xad 0x04 0x7c 0xc1 0x04 0x48 0x57    d..|..HW
    0010   0x14 0x6c 0x6b 0x14 0x4c 0x93 0x14 0xc0    .lk.L...
    0018   0xcf 0x14                                  ..
    decimal
             92   26   52   13    4   36  113    4
            100  173    4  124  193    4   72   87
             20  108  107   20   76  147   20  192
            207   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-08-22T13:47:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x6c 0x00    ..0.0.l.
    decimal
              1    0   48    0   48    0  108    0
    datetime (2012-08-22T13:47:06)
    0000   0x86 0x2f 0x4d 0x76 0x0c                   ./Mv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2012-08-22T16:02:17 head[2], body[15] op[0x5b]
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
    datetime (2012-08-22T16:02:17)
    0000   0x91 0x02 0x10 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 138, 'amount': 1.2, 'curve': 4},
 {'age': 148, 'amount': 1.3, 'curve': 4},
 {'age': 248, 'amount': 0.9, 'curve': 4},
 {'age': 52, 'amount': 2.5, 'curve': 20},
 {'age': 72, 'amount': 3.1, 'curve': 20},
 {'age': 222, 'amount': 1.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x30 0x8a 0x04 0x34 0x94 0x04    \.0..4..
    0008   0x24 0xf8 0x04 0x64 0x34 0x14 0x7c 0x48    $..d4.|H
    0010   0x14 0x48 0xde 0x14                        .H..
    decimal
             92   20   48  138    4   52  148    4
             36  248    4  100   52   20  124   72
             20   72  222   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-08-22T16:02:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x24 0x00    ..`.`.$.
    decimal
              1    0   96    0   96    0   36    0
    datetime (2012-08-22T16:02:17)
    0000   0x91 0x02 0x50 0x76 0x0c                   ..Pv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2012-08-22T17:36:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2012-08-22T17:36:26)
    0000   0x9a 0x24 0x31 0x76 0x0c                   .$1v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Base (2012, 8, 22, 17, 36, 26) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime ((2012, 8, 22, 17, 36, 26))
    0000   0x9a 0x24 0xf1 0x76 0x0c                   .$.v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian69 2000-08-18T13:10:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2000-08-18T13:10:22)
    0000   0x96 0x0a 0xcd 0x92 0x20                   .... 
    body (8)
    hex
    0000   0x32 0x76 0x0c 0x3f 0x19 0x92 0x20 0xb2    2v.?.. .
    decimal
             50  118   12   63   25  146   32  178
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 9 Base (2002, 5, 27, 22, 41, 41) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x0c                                  v.
    decimal
            118   12
    datetime ((2002, 5, 27, 22, 41, 41))
    0000   0x69 0x69 0x96 0x5b 0x72                   ii.[r
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 10 Base (2000, 1, 10, 12, 54, 18) head[2], body[0] op[0xa7]

    op hex (2)
    0000   0xa7 0x20                                  . 
    decimal
            167   32
    datetime ((2000, 1, 10, 12, 54, 18))
    0000   0x12 0x76 0x0c 0x2a 0x90                   .v.*.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 11 Base (2008, 0, 0, 8, 54, 23) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2008, 0, 0, 8, 54, 23))
    0000   0x17 0x36 0x68 0x00 0x98                   .6h..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 1]
`end logs/ReadHistoryData-page-15.data: 12 records`
