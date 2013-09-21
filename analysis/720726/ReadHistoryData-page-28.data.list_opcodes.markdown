## START analysis/ianj/raw/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8b 0xf2                                  ..
##### DEBUG DECIMAL
            139  242
#### RECORD 0 Ian3F 2013-08-04T08:35:50 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2013-08-04T08:35:50)
    0000   0xb2 0x23 0x08 0x64 0x0d                   .#.d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-08-04T08:35:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 142,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 15.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-08-04T08:35:58)
    0000   0xba 0x23 0x08 0x64 0x0d                   .#.d.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x98 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x98 0x36         ......6
    decimal
              0  144    0  110   23   54  152    0
              0    0    0    0    0  152   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian69 2013-08-04T08:35:58 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-04T08:35:58)
    0000   0xba 0x23 0x08 0x04 0x0d                   .#...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 3 Bolus 2013-08-04T08:35:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x00 0x00    ........
    decimal
              1    0  152    0  152    0    0    0
    datetime (2013-08-04T08:35:58)
    0000   0xba 0x23 0x48 0x64 0x0d                   .#Hd.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 BasalProfileStart 2013-08-04T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-04T09:30:00)
    0000   0x80 0x1e 0x09 0x04 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 5 CalBGForPH 2013-08-04T09:34:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2013-08-04T09:34:18)
    0000   0x92 0x22 0x29 0x64 0x0d                   .")d.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Ian3F 2013-08-04T09:34:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2013-08-04T09:34:18)
    0000   0x92 0x22 0x89 0x64 0x0d                   .".d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 BolusWizard 2013-08-04T10:54:57 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T10:54:57)
    0000   0xb9 0x36 0x0a 0x64 0x0d                   .6.d.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 3.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x98 0x8b 0x04                   \....
    decimal
             92    5  152  139    4
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-08-04T10:54:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x38 0x00    ..l.l.8.
    decimal
              1    0  108    0  108    0   56    0
    datetime (2013-08-04T10:54:57)
    0000   0xb9 0x36 0x4a 0x64 0x0d                   .6Jd.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2013-08-04T12:08:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 128}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-04T12:08:32)
    0000   0xa0 0x08 0x0c 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x24 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    $..n.6..
    0008   0x80 0x00 0x00 0x00 0x00 0x80 0x36         ......6
    decimal
             36  144    0  110   23   54    0    0
            128    0    0    0    0  128   54
    DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 2.6, 'curve': 4},
 {'age': 83, 'amount': 0.1, 'curve': 4},
 {'age': 213, 'amount': 3.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0x49 0x04 0x04 0x53 0x04    \.hI..S.
    0008   0x98 0xd5 0x04                             ...
    decimal
             92   11  104   73    4    4   83    4
            152  213    4
    datetime (unknown)

    body (0)

#### RECORD 12 Ian69 2013-08-04T12:08:32 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-04T12:08:32)
    0000   0xa0 0x08 0x0c 0x04 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 13 Bolus 2013-08-04T12:08:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x60 0x00    ......`.
    decimal
              1    0  128    0  128    0   96    0
    datetime (2013-08-04T12:08:32)
    0000   0xa0 0x08 0x4c 0x64 0x0d                   ..Ld.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 14 BasalProfileStart 2013-08-04T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-04T13:00:00)
    0000   0x80 0x00 0x0d 0x04 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 15 CalBGForPH 2013-08-04T16:42:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2013-08-04T16:42:46)
    0000   0xae 0x2a 0x30 0x64 0x0d                   .*0d.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2013-08-04T16:42:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-08-04T16:42:46)
    0000   0xae 0x2a 0xb0 0x64 0x0d                   .*.d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2013-08-04T16:52:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 43,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 23.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x2b                                  [+
    decimal
             91   43
    datetime (2013-08-04T16:52:13)
    0000   0x8d 0x34 0x10 0x64 0x0d                   .4.d.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0xec 0x00    ...n.6..
    0008   0x4c 0xf8 0x00 0x00 0x00 0x38 0x36         L....86
    decimal
             21  144    0  110   23   54  236    0
             76  248    0    0    0   56   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 3.2, 'curve': 20},
 {'age': 101, 'amount': 2.6, 'curve': 20},
 {'age': 111, 'amount': 0.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x80 0x1f 0x14 0x68 0x65 0x14    \....he.
    0008   0x04 0x6f 0x14                             .o.
    decimal
             92   11  128   31   20  104  101   20
              4  111   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-08-04T16:52:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-04T16:52:14)
    0000   0x8e 0x34 0x50 0x64 0x0d                   .4Pd.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2013-08-04T17:13:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-08-04T17:13:26)
    0000   0x9a 0x0d 0x11 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 1.4, 'curve': 4},
 {'age': 52, 'amount': 3.2, 'curve': 20},
 {'age': 122, 'amount': 2.6, 'curve': 20},
 {'age': 132, 'amount': 0.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x1c 0x04 0x80 0x34 0x14    \.8...4.
    0008   0x68 0x7a 0x14 0x04 0x84 0x14              hz....
    decimal
             92   14   56   28    4  128   52   20
            104  122   20    4  132   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-08-04T17:13:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x38 0x00    ......8.
    decimal
              1    0  144    0  144    0   56    0
    datetime (2013-08-04T17:13:26)
    0000   0x9a 0x0d 0x51 0x64 0x0d                   ..Qd.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2013-08-04T19:41:47 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T19:41:47)
    0000   0xaf 0x29 0x13 0x64 0x0d                   .).d.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 1.3, 'curve': 4},
 {'age': 156, 'amount': 2.3, 'curve': 4},
 {'age': 176, 'amount': 1.4, 'curve': 4},
 {'age': 200, 'amount': 3.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0x92 0x04 0x5c 0x9c 0x04    \.4..\..
    0008   0x38 0xb0 0x04 0x80 0xc8 0x14              8.....
    decimal
             92   14   52  146    4   92  156    4
             56  176    4  128  200   20
    datetime (unknown)

    body (0)

#### RECORD 25 Ian69 2013-08-04T19:41:47 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-04T19:41:47)
    0000   0xaf 0x29 0x73 0x04 0x0d                   .)s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 26 Bolus 2013-08-04T19:41:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x34 0x00    ..h.h.4.
    decimal
              1    0  104    0  104    0   52    0
    datetime (2013-08-04T19:41:47)
    0000   0xaf 0x29 0x53 0x64 0x0d                   .)Sd.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2013-08-04T20:48:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-08-04T20:48:10)
    0000   0x8a 0x30 0x34 0x64 0x0d                   .04d.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2013-08-04T20:48:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-08-04T20:48:10)
    0000   0x8a 0x30 0x34 0x64 0x0d                   .04d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 29 BolusWizard 2013-08-04T21:16:12 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T21:16:12)
    0000   0x8c 0x10 0x15 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 2.6, 'curve': 4},
 {'age': 241, 'amount': 1.3, 'curve': 4},
 {'age': 251, 'amount': 2.3, 'curve': 4},
 {'age': 15, 'amount': 1.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0x65 0x04 0x34 0xf1 0x04    \.he.4..
    0008   0x5c 0xfb 0x04 0x38 0x0f 0x14              \..8..
    decimal
             92   14  104  101    4   52  241    4
             92  251    4   56   15   20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-08-04T21:16:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x3c 0x00    ..x.x.<.
    decimal
              1    0  120    0  120    0   60    0
    datetime (2013-08-04T21:16:13)
    0000   0x8d 0x10 0x55 0x64 0x0d                   ..Ud.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2013-08-04T21:20:11 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T21:20:11)
    0000   0x8b 0x14 0x15 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 3.0, 'curve': 4},
 {'age': 105, 'amount': 2.6, 'curve': 4},
 {'age': 245, 'amount': 1.3, 'curve': 4},
 {'age': 255, 'amount': 2.3, 'curve': 4},
 {'age': 19, 'amount': 1.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x78 0x05 0x04 0x68 0x69 0x04    \.x..hi.
    0008   0x34 0xf5 0x04 0x5c 0xff 0x04 0x38 0x13    4..\..8.
    0010   0x14                                       .
    decimal
             92   17  120    5    4  104  105    4
             52  245    4   92  255    4   56   19
             20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-08-04T21:20:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0xb4 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  180    0
    datetime (2013-08-04T21:20:11)
    0000   0x8b 0x14 0x55 0x64 0x0d                   ..Ud.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 35 CalBGForPH 2013-08-04T22:45:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-08-04T22:45:08)
    0000   0x88 0x2d 0x36 0x64 0x0d                   .-6d.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 Ian3F 2013-08-04T22:45:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2013-08-04T22:45:08)
    0000   0x88 0x2d 0x96 0x64 0x0d                   .-.d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 BolusWizard 2013-08-04T23:30:21 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T23:30:21)
    0000   0x95 0x1e 0x17 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 135, 'amount': 3.9, 'curve': 4},
 {'age': 235, 'amount': 2.6, 'curve': 4},
 {'age': 119, 'amount': 1.3, 'curve': 20},
 {'age': 129, 'amount': 2.3, 'curve': 20},
 {'age': 149, 'amount': 1.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x9c 0x87 0x04 0x68 0xeb 0x04    \....h..
    0008   0x34 0x77 0x14 0x5c 0x81 0x14 0x38 0x95    4w.\..8.
    0010   0x14                                       .
    decimal
             92   17  156  135    4  104  235    4
             52  119   20   92  129   20   56  149
             20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-08-04T23:30:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x40 0x00    ..l.l.@.
    decimal
              1    0  108    0  108    0   64    0
    datetime (2013-08-04T23:30:21)
    0000   0x95 0x1e 0x57 0x64 0x0d                   ..Wd.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 40 BasalProfileStart 2013-08-05T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-05T00:00:00)
    0000   0x80 0x00 0x00 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 41 MResultTotals 2013-08-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x3f                   ....?
    decimal
              7    0    0    7   63
    datetime (2013-08-05T00:00:00)
    0000   0x84 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 42 Sara6E 2013-08-05T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-05T00:00:00)
    0000   0x84 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x10 0x70 0x3c 0x00 0x06 0x00 0x00    ..p<....
    0008   0x07 0x3f 0x03 0x83 0x30 0x03 0xbc 0x34    .?..0..4
    0010   0x00 0xe5 0x03 0x24 0x00 0x98 0x00 0x00    ...$....
    0018   0x00 0x00 0x08 0x01 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6   16  112   60    0    6    0    0
              7   63    3  131   48    3  188   52
              0  229    3   36    0  152    0    0
              0    0    8    1    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 43 BolusWizard 2013-08-05T00:10:18 head[2], body[15] op[0x5b]
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
    datetime (2013-08-05T00:10:18)
    0000   0x92 0x0a 0x00 0x65 0x0d                   ...e.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 2.7, 'curve': 4},
 {'age': 175, 'amount': 3.9, 'curve': 4},
 {'age': 19, 'amount': 2.6, 'curve': 20},
 {'age': 159, 'amount': 1.3, 'curve': 20},
 {'age': 169, 'amount': 2.3, 'curve': 20},
 {'age': 189, 'amount': 1.4, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x6c 0x2d 0x04 0x9c 0xaf 0x04    \.l-....
    0008   0x68 0x13 0x14 0x34 0x9f 0x14 0x5c 0xa9    h..4..\.
    0010   0x14 0x38 0xbd 0x14                        .8..
    decimal
             92   20  108   45    4  156  175    4
            104   19   20   52  159   20   92  169
             20   56  189   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-08-05T00:10:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x80 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  128    0
    datetime (2013-08-05T00:10:18)
    0000   0x92 0x0a 0x40 0x65 0x0d                   ..@e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 46 Bolus 2013-08-05T00:54:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x74 0x00    ..(.(.t.
    decimal
              1    0   40    0   40    0  116    0
    datetime (2013-08-05T00:54:15)
    0000   0x8f 0x36 0x40 0x65 0x0d                   .6@e.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-08-05T03:32:29 head[2], body[15] op[0x5b]
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
    datetime (2013-08-05T03:32:29)
    0000   0x9d 0x20 0x03 0x65 0x0d                   . .e.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 1.0, 'curve': 4},
 {'age': 207, 'amount': 0.9, 'curve': 4},
 {'age': 247, 'amount': 2.7, 'curve': 4},
 {'age': 121, 'amount': 3.9, 'curve': 20},
 {'age': 221, 'amount': 2.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0xa7 0x04 0x24 0xcf 0x04    \.(..$..
    0008   0x6c 0xf7 0x04 0x9c 0x79 0x14 0x68 0xdd    l...y.h.
    0010   0x14                                       .
    decimal
             92   17   40  167    4   36  207    4
            108  247    4  156  121   20  104  221
             20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-08-05T03:32:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x10 0x00    ..T.T...
    decimal
              1    0   84    0   84    0   16    0
    datetime (2013-08-05T03:32:29)
    0000   0x9d 0x20 0x43 0x65 0x0d                   . Ce.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 BasalProfileStart 2013-08-05T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-05T04:00:00)
    0000   0x80 0x00 0x04 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 51 CalBGForPH 2013-08-05T08:21:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2013-08-05T08:21:30)
    0000   0x9e 0x15 0x28 0x65 0x0d                   ..(e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 52 Ian3F 2013-08-05T08:21:30 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-08-05T08:21:30)
    0000   0x9e 0x15 0xe8 0x65 0x0d                   ...e.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 53 BasalProfileStart 2013-08-05T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-05T09:30:00)
    0000   0x80 0x1e 0x09 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 54 Ian69 2013-08-05T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-05T10:30:00)
    0000   0x80 0x1e 0x0a 0x05 0x0d                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 55 BolusWizard 2013-08-05T12:38:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 43,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 156}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-05T12:38:14)
    0000   0x8e 0x26 0x0c 0x65 0x0d                   .&.e.
    body (15)
    hex
    0000   0x2b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    +..n.6..
    0008   0x9c 0x00 0x00 0x00 0x00 0x9c 0x36         ......6
    decimal
             43  144    0  110   23   54    0    0
            156    0    0    0    0  156   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 Ian69 2013-08-05T12:38:14 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-05T12:38:14)
    0000   0x8e 0x26 0x0c 0x05 0x0d                   .&...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 57 Bolus 2013-08-05T12:38:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x00 0x00    ........
    decimal
              1    0  156    0  156    0    0    0
    datetime (2013-08-05T12:38:14)
    0000   0x8e 0x26 0x4c 0x65 0x0d                   .&Le.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 BasalProfileStart 2013-08-05T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-05T13:00:00)
    0000   0x80 0x00 0x0d 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 59 BolusWizard 2013-08-05T14:16:23 head[2], body[15] op[0x5b]
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
    datetime (2013-08-05T14:16:23)
    0000   0x97 0x10 0x0e 0x65 0x0d                   ...e.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 3.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x65 0x04                   \..e.
    decimal
             92    5  156  101    4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-08-05T14:16:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x5c 0x00    ..d.d.\.
    decimal
              1    0  100    0  100    0   92    0
    datetime (2013-08-05T14:16:23)
    0000   0x97 0x10 0x4e 0x65 0x0d                   ..Ne.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2013-08-05T14:30:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2013-08-05T14:30:22)
    0000   0x96 0x1e 0x2e 0x65 0x0d                   ...e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2013-08-05T14:30:22 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2013-08-05T14:30:22)
    0000   0x96 0x1e 0x8e 0x65 0x0d                   ...e.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2013-08-05T14:42:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-08-05T14:42:08)
    0000   0x88 0x2a 0x2e 0x65 0x0d                   .*.e.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 Ian3F 2013-08-05T14:42:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2013-08-05T14:42:08)
    0000   0x88 0x2a 0x4e 0x65 0x0d                   .*Ne.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-08-05T16:26:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-08-05T16:26:00)
    0000   0x80 0x1a 0x30 0x65 0x0d                   ..0e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2013-08-05T16:26:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-08-05T16:26:00)
    0000   0x80 0x1a 0x50 0x65 0x0d                   ..Pe.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2013-08-05T18:14:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-08-05T18:14:00)
    0000   0x80 0x0e 0x32 0x65 0x0d                   ..2e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 69 Ian3F 2013-08-05T18:14:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2013-08-05T18:14:00)
    0000   0x80 0x0e 0x52 0x65 0x0d                   ..Re.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 70 BolusWizard 2013-08-05T18:14:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 37,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 13.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-08-05T18:14:32)
    0000   0xa0 0x0e 0x12 0x65 0x0d                   ...e.
    body (15)
    hex
    0000   0x25 0x90 0x00 0x6e 0x17 0x36 0x84 0x00    %..n.6..
    0008   0x84 0x00 0x00 0x08 0x01 0x00 0x36         ......6
    decimal
             37  144    0  110   23   54  132    0
            132    0    0    8    1    0   54
    DAY BITS: [0, 1, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 2.5, 'curve': 4},
 {'age': 83, 'amount': 3.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0xef 0x04 0x9c 0x53 0x14    \.d...S.
    decimal
             92    8  100  239    4  156   83   20
    datetime (unknown)

    body (0)

#### RECORD 72 Ian69 2013-08-05T18:14:32 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-05T18:14:32)
    0000   0xa0 0x0e 0x72 0x05 0x0d                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 73 Bolus 2013-08-05T18:14:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x00 0x01 0x00 0x00 0x08 0x00    ........
    decimal
              1    1    0    1    0    0    8    0
    datetime (2013-08-05T18:14:32)
    0000   0xa0 0x0e 0x52 0x65 0x0d                   ..Re.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 74 BolusWizard 2013-08-05T19:52:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 37,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-05T19:52:24)
    0000   0x98 0x34 0x13 0x65 0x0d                   .4.e.
    body (15)
    hex
    0000   0x25 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    %..n.6..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x36         ......6
    decimal
             37  144    0  110   23   54    0    0
            132    0    0    0    0  132   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
`end analysis/ianj/raw/ReadHistoryData-page-28.data: 75 records`
