## START ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdf 0x50                                  .P
##### DEBUG DECIMAL
            223   80
#### RECORD 0 BolusWizard 2015-04-22T12:33:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.5,
 'carb_input': 20,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 2.5,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-22T12:33:56)
    0000   0x78 0x21 0x0c 0x16 0x0f                   x!...
    body (13)
    hex
    0000   0x14 0x50 0x08 0x28 0x5a 0x00 0x19 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x19 0x78                   ....x
    decimal
             20   80    8   40   90    0   25    0
              0    0    0   25  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.15},
 {'age': 14, 'amount': 0.25},
 {'age': 24, 'amount': 0.25},
 {'age': 34, 'amount': 2.35},
 {'age': 44, 'amount': 5.3},
 {'age': 274, 'amount': 2.8},
 {'age': 284, 'amount': 2.3}]
```
    op hex (23)
    0000   0x5c 0x17 0x06 0x04 0x04 0x0a 0x0e 0x04    \.......
    0008   0x0a 0x18 0x04 0x5e 0x22 0x04 0xd4 0x2c    ...^"..,
    0010   0x04 0x70 0x12 0x14 0x5c 0x1c 0x14         .p..\..
    decimal
             92   23    6    4    4   10   14    4
             10   24    4   94   34    4  212   44
              4  112   18   20   92   28   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-04-22T12:00:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'duration': 60, 'programmed': 1.6, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x02                        ....
    decimal
              1   16   16    2
    datetime (2015-04-22T12:00:25)
    0000   0x59 0x00 0xac 0x16 0x0f                   Y....
    body (0)

#### RECORD 3 Bolus 2015-04-22T12:33:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'duration': 0, 'programmed': 2.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2015-04-22T12:33:56)
    0000   0x78 0x21 0x4c 0x16 0x0f                   x!L..
    body (0)

#### RECORD 4 SensorAlert 2015-04-22T12:36:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 336}
```
    op hex (3)
    0000   0x0b 0x65 0x50                             .eP
    decimal
             11  101   80
    datetime (2015-04-22T12:36:53)
    0000   0x75 0x24 0x2c 0xb6 0x8f                   u$,..
    body (0)

#### RECORD 5 SensorAlert 2015-04-22T14:06:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-04-22T14:06:44)
    0000   0x6c 0x06 0x2e 0xb6 0x0f                   l....
    body (0)

#### RECORD 6 SensorAlert 2015-04-22T17:35:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-22T17:35:55)
    0000   0x77 0x23 0x31 0xb6 0x0f                   w#1..
    body (0)

#### RECORD 7 BolusWizard 2015-04-22T17:36:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 36,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-22T17:36:11)
    0000   0x4b 0x24 0x11 0x16 0x0f                   K$...
    body (13)
    hex
    0000   0x24 0x50 0x08 0x28 0x5a 0x00 0x2d 0x00    $P.(Z.-.
    0008   0x00 0x00 0x00 0x2d 0x78                   ...-x
    decimal
             36   80    8   40   90    0   45    0
              0    0    0   45  120

#### RECORD 8 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 277, 'amount': 0.05},
 {'age': 287, 'amount': 0.25},
 {'age': 297, 'amount': 0.3},
 {'age': 307, 'amount': 2.75},
 {'age': 317, 'amount': 0.25},
 {'age': 327, 'amount': 0.25},
 {'age': 337, 'amount': 2.35},
 {'age': 347, 'amount': 5.3}]
```
    op hex (26)
    0000   0x5c 0x1a 0x02 0x15 0x14 0x0a 0x1f 0x14    \.......
    0008   0x0c 0x29 0x14 0x6e 0x33 0x14 0x0a 0x3d    .).n3..=
    0010   0x14 0x0a 0x47 0x14 0x5e 0x51 0x14 0xd4    ..G.^Q..
    0018   0x5b 0x14                                  [.
    decimal
             92   26    2   21   20   10   31   20
             12   41   20  110   51   20   10   61
             20   10   71   20   94   81   20  212
             91   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2015-04-22T17:36:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'duration': 0, 'programmed': 4.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2015-04-22T17:36:11)
    0000   0x4b 0x24 0x51 0x16 0x0f                   K$Q..
    body (0)

#### RECORD 10 SensorAlert 2015-04-22T21:41:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-04-22T21:41:17)
    0000   0x51 0x29 0x35 0xb6 0x0f                   Q)5..
    body (0)

#### RECORD 11 SensorAlert 2015-04-22T22:54:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-22T22:54:00)
    0000   0x40 0x36 0x36 0xb6 0x0f                   @66..
    body (0)

#### RECORD 12 CalBGForPH 2015-04-22T22:56:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2015-04-22T22:56:08)
    0000   0x48 0x38 0x36 0x76 0x0f                   H86v.
    body (0)

#### RECORD 13 BGReceived 2015-04-22T22:56:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 169, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2015-04-22T22:56:08)
    0000   0x48 0x38 0x36 0x76 0x0f                   H86v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 14 BolusWizard 2015-04-22T22:56:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 169,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2015-04-22T22:56:29)
    0000   0x5d 0x38 0x16 0x16 0x0f                   ]8...
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x0c 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x0c 0x78                   ....x
    decimal
              0   80   10   40   90   12    0    0
              0    0    0   12  120

#### RECORD 15 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 317, 'amount': 0.3}, {'age': 327, 'amount': 4.2}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x3d 0x14 0xa8 0x47 0x14    \..=..G.
    decimal
             92    8   12   61   20  168   71   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2015-04-22T22:56:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'duration': 0, 'programmed': 0.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2015-04-22T22:56:29)
    0000   0x5d 0x38 0x56 0x16 0x0f                   ]8V..
    body (0)

#### RECORD 17 SensorAlert 2015-04-22T23:12:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 190}
```
    op hex (3)
    0000   0x0b 0x65 0xbe                             .e.
    decimal
             11  101  190
    datetime (2015-04-22T23:12:05)
    0000   0x45 0x0c 0x37 0xb6 0x0f                   E.7..
    body (0)

#### RECORD 18 MResultTotals 2015-04-23T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x6e                   ....n
    decimal
              7    0    0    6  110
    datetime (2015-04-23T00:00:00)
    0000   0x56 0x0f                                  V.
    body (0)

#### RECORD 19 Model522ResultTotals 2015-04-23T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-23T00:00:00)
    0000   0x56 0x0f                                  V.
    body (41)
    hex
    0000   0x05 0x11 0x1f 0xa9 0x6d 0x03 0x00 0x00    ....m...
    0008   0x06 0x6e 0x03 0x0e 0x30 0x03 0x60 0x34    .n..0.`4
    0010   0x00 0x51 0x03 0x60 0x34 0x01 0x94 0x2f    .Q.`4../
    0018   0x01 0xcc 0x35 0x00 0x00 0x00 0x05 0x02    ..5.....
    0020   0x02 0x01 0x00 0x50 0xb2 0x2f 0x80 0x20    ...P./. 
    0028   0x03                                       .
    decimal
              5   17   31  169  109    3    0    0
              6  110    3   14   48    3   96   52
              0   81    3   96   52    1  148   47
              1  204   53    0    0    0    5    2
              2    1    0   80  178   47  128   32
              3

#### RECORD 20 SensorAlert 2015-04-23T00:40:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 295}
```
    op hex (3)
    0000   0x0b 0x65 0x27                             .e'
    decimal
             11  101   39
    datetime (2015-04-23T00:40:36)
    0000   0x64 0x28 0x20 0xb7 0x8f                   d( ..
    body (0)

#### RECORD 21 LowReservoir 2015-04-23T01:20:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-04-23T01:20:00)
    0000   0x40 0x14 0x01 0x17 0x0f                   @....
    body (0)

#### RECORD 22 SensorAlert 2015-04-23T02:10:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 367}
```
    op hex (3)
    0000   0x0b 0x65 0x6f                             .eo
    decimal
             11  101  111
    datetime (2015-04-23T02:10:38)
    0000   0x66 0x0a 0x22 0xb7 0x8f                   f."..
    body (0)

#### RECORD 23 CalBGForPH 2015-04-23T02:26:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 347}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2015-04-23T02:26:40)
    0000   0x68 0x1a 0x22 0x77 0x8f                   h."w.
    body (0)

#### RECORD 24 BGReceived 2015-04-23T02:26:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 347, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2b                                  ?+
    decimal
             63   43
    datetime (2015-04-23T02:26:40)
    0000   0x68 0x1a 0x62 0x77 0x0f                   h.bw.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 25 BolusWizard 2015-04-23T02:26:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 56,
 '_byte[7]': 0,
 'bg': 347,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.5,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2015-04-23T02:26:46)
    0000   0x6e 0x1a 0x02 0x17 0x0f                   n....
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x38 0x00 0x00    .Q.(Z8..
    0008   0x00 0x01 0x00 0x37 0x78                   ...7x
    decimal
              0   81   10   40   90   56    0    0
              0    1    0   55  120

#### RECORD 26 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 0.5}]
```
    op hex (5)
    0000   0x5c 0x05 0x14 0xd9 0x04                   \....
    decimal
             92    5   20  217    4
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2015-04-23T02:26:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'duration': 0, 'programmed': 5.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2015-04-23T02:26:46)
    0000   0x6e 0x1a 0x42 0x17 0x0f                   n.B..
    body (0)

#### RECORD 28 SensorAlert 2015-04-23T03:41:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 343}
```
    op hex (3)
    0000   0x0b 0x65 0x57                             .eW
    decimal
             11  101   87
    datetime (2015-04-23T03:41:17)
    0000   0x51 0x29 0x23 0xb7 0x8f                   Q)#..
    body (0)

#### RECORD 29 SensorAlert 2015-04-23T05:12:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 322}
```
    op hex (3)
    0000   0x0b 0x65 0x42                             .eB
    decimal
             11  101   66
    datetime (2015-04-23T05:12:05)
    0000   0x45 0x0c 0x25 0xb7 0x8f                   E.%..
    body (0)

#### RECORD 30 LowReservoir 2015-04-23T06:20:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-04-23T06:20:00)
    0000   0x40 0x14 0x06 0x17 0x0f                   @....
    body (0)

#### RECORD 31 SensorAlert 2015-04-23T06:40:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 291}
```
    op hex (3)
    0000   0x0b 0x65 0x23                             .e#
    decimal
             11  101   35
    datetime (2015-04-23T06:40:36)
    0000   0x64 0x28 0x26 0xb7 0x8f                   d(&..
    body (0)

#### RECORD 32 CalBGForPH 2015-04-23T06:48:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 261}
```
    op hex (2)
    0000   0x0a 0x05                                  ..
    decimal
             10    5
    datetime (2015-04-23T06:48:34)
    0000   0x62 0x30 0x26 0x77 0x8f                   b0&w.
    body (0)

#### RECORD 33 BGReceived 2015-04-23T06:48:34 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 261, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2015-04-23T06:48:34)
    0000   0x62 0x30 0xa6 0x77 0x0f                   b0.w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 BolusWizard 2015-04-23T06:48:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 261,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.5,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x05                                  [.
    decimal
             91    5
    datetime (2015-04-23T06:48:53)
    0000   0x75 0x30 0x06 0x17 0x0f                   u0...
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x23 0x00 0x00    .Q.(Z#..
    0008   0x00 0x00 0x00 0x23 0x78                   ...#x
    decimal
              0   81   10   40   90   35    0    0
              0    0    0   35  120

#### RECORD 35 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 259, 'amount': 2.15},
 {'age': 269, 'amount': 3.35},
 {'age': 479, 'amount': 0.5}]
```
    op hex (11)
    0000   0x5c 0x0b 0x56 0x03 0x14 0x86 0x0d 0x14    \.V.....
    0008   0x14 0xdf 0x14                             ...
    decimal
             92   11   86    3   20  134   13   20
             20  223   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2015-04-23T06:48:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'duration': 0, 'programmed': 3.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2015-04-23T06:48:53)
    0000   0x75 0x30 0x46 0x17 0x0f                   u0F..
    body (0)

#### RECORD 37 PumpSuspend 2015-04-23T07:06:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-23T07:06:18)
    0000   0x52 0x06 0x07 0x17 0x0f                   R....
    body (0)

#### RECORD 38 SensorAlert 2015-04-23T08:10:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 225}
```
    op hex (3)
    0000   0x0b 0x65 0xe1                             .e.
    decimal
             11  101  225
    datetime (2015-04-23T08:10:38)
    0000   0x66 0x0a 0x28 0xb7 0x0f                   f.(..
    body (0)

#### RECORD 39 PumpResume 2015-04-23T08:10:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-23T08:10:46)
    0000   0x6e 0x0a 0x08 0x17 0x0f                   n....
    body (0)

#### RECORD 40 BolusWizard 2015-04-23T08:28:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 45,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-23T08:28:47)
    0000   0x6f 0x1c 0x08 0x17 0x0f                   o....
    body (13)
    hex
    0000   0x2d 0x50 0x0a 0x28 0x5a 0x00 0x2d 0x00    -P.(Z.-.
    0008   0x00 0x00 0x00 0x2d 0x78                   ...-x
    decimal
             45   80   10   40   90    0   45    0
              0    0    0   45  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 3.3},
 {'age': 109, 'amount': 0.2},
 {'age': 359, 'amount': 2.15},
 {'age': 369, 'amount': 3.35}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x63 0x04 0x08 0x6d 0x04    \..c..m.
    0008   0x56 0x67 0x14 0x86 0x71 0x14              Vg..q.
    decimal
             92   14  132   99    4    8  109    4
             86  103   20  134  113   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-04-23T08:28:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'duration': 0, 'programmed': 4.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2015-04-23T08:28:47)
    0000   0x6f 0x1c 0x48 0x17 0x0f                   o.H..
    body (0)

#### RECORD 43 BolusWizard 2015-04-23T08:56:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.6,
 'carb_input': 16,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 1.6,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-23T08:56:38)
    0000   0x66 0x38 0x08 0x17 0x0f                   f8...
    body (13)
    hex
    0000   0x10 0x50 0x0a 0x28 0x5a 0x00 0x10 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x10 0x78                   ....x
    decimal
             16   80   10   40   90    0   16    0
              0    0    0   16  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 4.15},
 {'age': 37, 'amount': 0.35},
 {'age': 127, 'amount': 3.3},
 {'age': 137, 'amount': 0.2},
 {'age': 387, 'amount': 2.15},
 {'age': 397, 'amount': 3.35}]
```
    op hex (20)
    0000   0x5c 0x14 0xa6 0x1b 0x04 0x0e 0x25 0x04    \.....%.
    0008   0x84 0x7f 0x04 0x08 0x89 0x04 0x56 0x83    ......V.
    0010   0x14 0x86 0x8d 0x14                        ....
    decimal
             92   20  166   27    4   14   37    4
            132  127    4    8  137    4   86  131
             20  134  141   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-04-23T08:56:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'duration': 0, 'programmed': 1.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2015-04-23T08:56:38)
    0000   0x66 0x38 0x48 0x17 0x0f                   f8H..
    body (0)

#### RECORD 46 SensorAlert 2015-04-23T11:26:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-04-23T11:26:44)
    0000   0x6c 0x1a 0x2b 0xb7 0x0f                   l.+..
    body (0)

#### RECORD 47 SensorAlert 2015-04-23T12:55:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 232}
```
    op hex (3)
    0000   0x0b 0x65 0xe8                             .e.
    decimal
             11  101  232
    datetime (2015-04-23T12:55:55)
    0000   0x77 0x37 0x2c 0xb7 0x0f                   w7,..
    body (0)

#### RECORD 48 SensorAlert 2015-04-23T13:52:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-04-23T13:52:05)
    0000   0x45 0x34 0x2d 0xb7 0x0f                   E4-..
    body (0)

#### RECORD 49 BolusWizard 2015-04-23T14:26:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.3,
 'carb_input': 35,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 4.3,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-23T14:26:39)
    0000   0x67 0x1a 0x0e 0x17 0x0f                   g....
    body (13)
    hex
    0000   0x23 0x50 0x08 0x28 0x5a 0x00 0x2b 0x00    #P.(Z.+.
    0008   0x00 0x00 0x00 0x2b 0x78                   ...+x
    decimal
             35   80    8   40   90    0   43    0
              0    0    0   43  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 337, 'amount': 1.6},
 {'age': 357, 'amount': 4.15},
 {'age': 367, 'amount': 0.35},
 {'age': 457, 'amount': 3.3},
 {'age': 467, 'amount': 0.2}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x51 0x14 0xa6 0x65 0x14    \.@Q..e.
    0008   0x0e 0x6f 0x14 0x84 0xc9 0x14 0x08 0xd3    .o......
    0010   0x14                                       .
    decimal
             92   17   64   81   20  166  101   20
             14  111   20  132  201   20    8  211
             20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-04-23T14:26:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'duration': 0, 'programmed': 4.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2015-04-23T14:26:39)
    0000   0x67 0x1a 0x4e 0x17 0x0f                   g.N..
    body (0)

#### RECORD 52 CalBGForPH 2015-04-23T19:10:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 279}
```
    op hex (2)
    0000   0x0a 0x17                                  ..
    decimal
             10   23
    datetime (2015-04-23T19:10:33)
    0000   0x61 0x0a 0x33 0x77 0x8f                   a.3w.
    body (0)

#### RECORD 53 BGReceived 2015-04-23T19:10:33 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 279, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2015-04-23T19:10:33)
    0000   0x61 0x0a 0xf3 0x77 0x0f                   a..w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 54 BolusWizard 2015-04-23T19:10:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 279,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 6,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x17                                  [.
    decimal
             91   23
    datetime (2015-04-23T19:10:49)
    0000   0x71 0x0a 0x13 0x17 0x0f                   q....
    body (13)
    hex
    0000   0x00 0x51 0x06 0x28 0x5a 0x27 0x00 0x00    .Q.(Z'..
    0008   0x00 0x00 0x00 0x27 0x78                   ...'x
    decimal
              0   81    6   40   90   39    0    0
              0    0    0   39  120

#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 281, 'amount': 0.8}, {'age': 291, 'amount': 3.5}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x19 0x14 0x8c 0x23 0x14    \. ...#.
    decimal
             92    8   32   25   20  140   35   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2015-04-23T19:10:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'duration': 0, 'programmed': 3.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x27 0x03 0x00                        .'..
    decimal
              1   39    3    0
    datetime (2015-04-23T19:10:49)
    0000   0x71 0x0a 0x53 0x17 0x0f                   q.S..
    body (0)

#### RECORD 57 NoDelivery 2015-04-23T19:10:59 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xff                        ....
    decimal
              6    4   11  255
    datetime (2015-04-23T19:10:59)
    0000   0x7b 0x0a 0x53 0x57 0x0f                   {.SW.
    body (0)

#### RECORD 58 ClearAlarm 2015-04-23T19:11:12 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-04-23T19:11:12)
    0000   0x4c 0x0b 0x13 0x17 0x0f                   L....
    body (0)

#### RECORD 59 Rewind 2015-04-23T19:11:17 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-04-23T19:11:17)
    0000   0x51 0x0b 0x13 0x17 0x0f                   Q....
    body (0)

#### RECORD 60 Prime 2015-04-23T19:15:10 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x3c                   ....<
    decimal
              3    0    0    0   60
    datetime (2015-04-23T19:15:10)
    0000   0x4a 0x0f 0x33 0x17 0x0f                   J.3..
    body (0)

#### RECORD 61 Prime 2015-04-23T19:15:43 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2015-04-23T19:15:43)
    0000   0x6b 0x0f 0x13 0x17 0x0f                   k....
    body (0)

#### RECORD 62 SensorAlert 2015-04-23T19:20:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 279}
```
    op hex (3)
    0000   0x0b 0x65 0x17                             .e.
    decimal
             11  101   23
    datetime (2015-04-23T19:20:37)
    0000   0x65 0x14 0x33 0xb7 0x8f                   e.3..
    body (0)

#### RECORD 63 SensorAlert 2015-04-23T20:50:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 370}
```
    op hex (3)
    0000   0x0b 0x65 0x72                             .er
    decimal
             11  101  114
    datetime (2015-04-23T20:50:39)
    0000   0x67 0x32 0x34 0xb7 0x8f                   g24..
    body (0)

#### RECORD 64 BolusWizard 2015-04-23T20:51:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-23T20:51:25)
    0000   0x59 0x33 0x14 0x17 0x0f                   Y3...
    body (13)
    hex
    0000   0x00 0x50 0x06 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80    6   40   90    0    0    0
              0    0    0    0  120

#### RECORD 65 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 0.25},
 {'age': 382, 'amount': 0.8},
 {'age': 392, 'amount': 3.5}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0a 0x66 0x04 0x20 0x7e 0x14    \..f. ~.
    0008   0x8c 0x88 0x14                             ...
    decimal
             92   11   10  102    4   32  126   20
            140  136   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2015-04-23T20:51:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'duration': 0, 'programmed': 5.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2015-04-23T20:51:25)
    0000   0x59 0x33 0x54 0x17 0x0f                   Y3T..
    body (0)

#### RECORD 67 BolusWizard 2015-04-23T21:30:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.3,
 'carb_input': 50,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 8.3,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-23T21:30:19)
    0000   0x53 0x1e 0x15 0x17 0x0f                   S....
    body (13)
    hex
    0000   0x32 0x50 0x06 0x28 0x5a 0x00 0x53 0x00    2P.(Z.S.
    0008   0x00 0x00 0x00 0x53 0x78                   ...Sx
    decimal
             50   80    6   40   90    0   83    0
              0    0    0   83  120

#### RECORD 68 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 5.6},
 {'age': 141, 'amount': 0.25},
 {'age': 421, 'amount': 0.8},
 {'age': 431, 'amount': 3.5}]
```
    op hex (14)
    0000   0x5c 0x0e 0xe0 0x29 0x04 0x0a 0x8d 0x04    \..)....
    0008   0x20 0xa5 0x14 0x8c 0xaf 0x14               .....
    decimal
             92   14  224   41    4   10  141    4
             32  165   20  140  175   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2015-04-23T21:30:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'duration': 0, 'programmed': 4.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2015-04-23T21:30:19)
    0000   0x53 0x1e 0x95 0x17 0x0f                   S....
    body (0)

#### RECORD 70 CalBGForPH 2015-04-23T22:18:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2015-04-23T22:18:14)
    0000   0x4e 0x12 0x36 0x77 0x0f                   N.6w.
    body (0)

#### RECORD 71 BGReceived 2015-04-23T22:18:14 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 235, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2015-04-23T22:18:14)
    0000   0x4e 0x12 0x76 0x77 0x0f                   N.vw.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 72 SensorAlert 2015-04-23T22:21:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 289}
```
    op hex (3)
    0000   0x0b 0x65 0x21                             .e!
    decimal
             11  101   33
    datetime (2015-04-23T22:21:18)
    0000   0x52 0x15 0x36 0xb7 0x8f                   R.6..
    body (0)

#### RECORD 73 Bolus 2015-04-23T21:33:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'duration': 60, 'programmed': 2.3, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x02                        ....
    decimal
              1   23   23    2
    datetime (2015-04-23T21:33:13)
    0000   0x4d 0x21 0xb5 0x17 0x0f                   M!...
    body (0)

#### RECORD 74 MResultTotals 2015-04-24T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xfc                   .....
    decimal
              7    0    0    7  252
    datetime (2015-04-24T00:00:00)
    0000   0x57 0x0f                                  W.
    body (0)

#### RECORD 75 Model522ResultTotals 2015-04-24T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-24T00:00:00)
    0000   0x57 0x0f                                  W.
    body (41)
    hex
    0000   0x05 0x11 0x19 0xeb 0x5b 0x04 0x00 0x00    ....[...
    0008   0x07 0xfc 0x02 0xfe 0x25 0x04 0xfe 0x3f    ....%..?
    0010   0x00 0x92 0x04 0xfe 0x3f 0x02 0xac 0x36    ....?..6
    0018   0x02 0x52 0x2e 0x00 0x00 0x00 0x08 0x04    .R......
    0020   0x04 0x00 0x00 0x11 0x10 0x82 0x90 0xde    ........
    0028   0x04                                       .
    decimal
              5   17   25  235   91    4    0    0
              7  252    2  254   37    4  254   63
              0  146    4  254   63    2  172   54
              2   82   46    0    0    0    8    4
              4    0    0   17   16  130  144  222
              4

#### RECORD 76 PumpSuspend 2015-04-24T07:31:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-24T07:31:39)
    0000   0x67 0x1f 0x07 0x18 0x0f                   g....
    body (0)

#### RECORD 77 LowBattery 2015-04-24T08:02:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2015-04-24T08:02:00)
    0000   0x40 0x02 0x08 0x18 0x0f                   @....
    body (0)

#### RECORD 78 PumpResume 2015-04-24T08:02:47 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-24T08:02:47)
    0000   0x6f 0x02 0x08 0x18 0x0f                   o....
    body (0)

#### RECORD 79 SensorAlert 2015-04-24T09:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-24T09:18:00)
    0000   0x40 0x12 0x29 0xb8 0x0f                   @.)..
    body (0)

#### RECORD 80 BolusWizard 2015-04-24T09:19:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-24T09:19:25)
    0000   0x59 0x13 0x09 0x18 0x0f                   Y....
    body (13)
    hex
    0000   0x32 0x50 0x0a 0x28 0x5a 0x00 0x32 0x00    2P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             50   80   10   40   90    0   50    0
              0    0    0   50  120

#### RECORD 81 Bolus 2015-04-24T09:19:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'duration': 0, 'programmed': 5.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2015-04-24T09:19:25)
    0000   0x59 0x13 0x49 0x18 0x0f                   Y.I..
    body (0)

#### RECORD 82 SensorAlert 2015-04-24T09:47:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-24T09:47:13)
    0000   0x4d 0x2f 0x29 0xb8 0x0f                   M/)..
    body (0)

#### RECORD 83 SensorAlert 2015-04-24T10:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-24T10:18:00)
    0000   0x40 0x12 0x2a 0xb8 0x0f                   @.*..
    body (0)

#### RECORD 84 CalBGForPH 2015-04-24T10:19:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 257}
```
    op hex (2)
    0000   0x0a 0x01                                  ..
    decimal
             10    1
    datetime (2015-04-24T10:19:47)
    0000   0x6f 0x13 0x2a 0x18 0x8f                   o.*..
    body (0)

#### RECORD 85 CalBGForPH 2015-04-24T10:20:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 257}
```
    op hex (2)
    0000   0x0a 0x01                                  ..
    decimal
             10    1
    datetime (2015-04-24T10:20:28)
    0000   0x5c 0x14 0x2a 0x18 0x8f                   \.*..
    body (0)

#### RECORD 86 SensorAlert 2015-04-24T10:32:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 242}
```
    op hex (3)
    0000   0x0b 0x65 0xf2                             .e.
    decimal
             11  101  242
    datetime (2015-04-24T10:32:06)
    0000   0x46 0x20 0x2a 0xb8 0x0f                   F *..
    body (0)

#### RECORD 87 BolusWizard 2015-04-24T12:20:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.3,
 'carb_input': 35,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 4.3,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-24T12:20:24)
    0000   0x58 0x14 0x0c 0x18 0x0f                   X....
    body (13)
    hex
    0000   0x23 0x50 0x08 0x28 0x5a 0x00 0x2b 0x00    #P.(Z.+.
    0008   0x00 0x00 0x00 0x2b 0x78                   ...+x
    decimal
             35   80    8   40   90    0   43    0
              0    0    0   43  120

#### RECORD 88 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 5.0}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0xb5 0x04                   \....
    decimal
             92    5  200  181    4
    datetime (unknown)

    body (0)

`end ReadHistoryData-page-5.data: 89 records`
