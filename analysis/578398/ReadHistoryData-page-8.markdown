## START ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x07 0x81                                  ..
##### DEBUG DECIMAL
              7  129
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 4.0},
 {'age': 291, 'amount': 1.1},
 {'age': 301, 'amount': 2.1}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa0 0x79 0x04 0x2c 0x23 0x14    \..y.,#.
    0008   0x54 0x2d 0x14                             T-.
    decimal
             92   11  160  121    4   44   35   20
             84   45   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-04-15T09:10:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2015-04-15T09:10:12)
    0000   0x4c 0x0a 0x49 0x0f 0x0f                   L.I..
    body (0)

#### RECORD 2 CalBGForPH 2015-04-15T12:00:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 178}
```
    op hex (2)
    0000   0x0a 0xb2                                  ..
    decimal
             10  178
    datetime (2015-04-15T12:00:28)
    0000   0x5c 0x00 0x2c 0x6f 0x0f                   \.,o.
    body (0)

#### RECORD 3 BGReceived 2015-04-15T12:00:28 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 178, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-04-15T12:00:28)
    0000   0x5c 0x00 0x4c 0x6f 0x0f                   \.Lo.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 4 SensorAlert 2015-04-15T12:08:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-15T12:08:04)
    0000   0x44 0x08 0x2c 0xaf 0x0f                   D.,..
    body (0)

#### RECORD 5 BolusWizard 2015-04-15T12:08:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 178,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.6,
 'carb_input': 45,
 'carb_ratio': 8,
 'correction_estimate': 1.4,
 'food_estimate': 5.6,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb2                                  [.
    decimal
             91  178
    datetime (2015-04-15T12:08:34)
    0000   0x62 0x08 0x0c 0x0f 0x0f                   b....
    body (13)
    hex
    0000   0x2d 0x50 0x08 0x28 0x5a 0x0e 0x38 0x00    -P.(Z.8.
    0008   0x00 0x04 0x00 0x42 0x78                   ...Bx
    decimal
             45   80    8   40   90   14   56    0
              0    4    0   66  120

#### RECORD 6 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 2.0},
 {'age': 299, 'amount': 4.0},
 {'age': 469, 'amount': 1.1},
 {'age': 479, 'amount': 2.1}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0xb3 0x04 0xa0 0x2b 0x14    \.P...+.
    0008   0x2c 0xd5 0x14 0x54 0xdf 0x14              ,..T..
    decimal
             92   14   80  179    4  160   43   20
             44  213   20   84  223   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2015-04-15T12:08:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'duration': 0, 'programmed': 3.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2015-04-15T12:08:34)
    0000   0x62 0x08 0x8c 0x0f 0x0f                   b....
    body (0)

#### RECORD 8 CalBGForPH 2015-04-15T13:14:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2015-04-15T13:14:00)
    0000   0x40 0x0e 0x2d 0x6f 0x0f                   @.-o.
    body (0)

#### RECORD 9 BGReceived 2015-04-15T13:14:00 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 103, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2015-04-15T13:14:00)
    0000   0x40 0x0e 0xed 0x6f 0x0f                   @..o.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 10 Bolus 2015-04-15T12:11:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'duration': 120, 'programmed': 2.2, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x04                        ....
    decimal
              1   22   22    4
    datetime (2015-04-15T12:11:05)
    0000   0x45 0x0b 0xac 0x0f 0x0f                   E....
    body (0)

#### RECORD 11 CalBGForPH 2015-04-15T15:19:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 52}
```
    op hex (2)
    0000   0x0a 0x34                                  .4
    decimal
             10   52
    datetime (2015-04-15T15:19:40)
    0000   0x68 0x13 0x2f 0x6f 0x0f                   h./o.
    body (0)

#### RECORD 12 BGReceived 2015-04-15T15:19:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 52, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-04-15T15:19:40)
    0000   0x68 0x13 0x8f 0x6f 0x0f                   h..o.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 13 SensorAlert 2015-04-15T15:32:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 73}
```
    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-04-15T15:32:52)
    0000   0x74 0x20 0x2f 0xaf 0x0f                   t /..
    body (0)

#### RECORD 14 SensorAlert 2015-04-15T15:51:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-04-15T15:51:54)
    0000   0x76 0x33 0x2f 0xaf 0x0f                   v3/..
    body (0)

#### RECORD 15 SensorAlert 2015-04-15T16:12:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-15T16:12:52)
    0000   0x74 0x0c 0x30 0xaf 0x0f                   t.0..
    body (0)

#### RECORD 16 SensorAlert 2015-04-15T20:26:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-15T20:26:37)
    0000   0x65 0x1a 0x34 0xaf 0x0f                   e.4..
    body (0)

#### RECORD 17 SensorAlert 2015-04-15T21:57:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 247}
```
    op hex (3)
    0000   0x0b 0x65 0xf7                             .e.
    decimal
             11  101  247
    datetime (2015-04-15T21:57:16)
    0000   0x50 0x39 0x35 0xaf 0x0f                   P95..
    body (0)

#### RECORD 18 CalBGForPH 2015-04-15T22:07:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 291}
```
    op hex (2)
    0000   0x0a 0x23                                  .#
    decimal
             10   35
    datetime (2015-04-15T22:07:44)
    0000   0x6c 0x07 0x36 0x6f 0x8f                   l.6o.
    body (0)

#### RECORD 19 BGReceived 2015-04-15T22:07:44 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 291, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x24                                  ?$
    decimal
             63   36
    datetime (2015-04-15T22:07:44)
    0000   0x6c 0x07 0x76 0x6f 0x0f                   l.vo.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 20 BolusWizard 2015-04-15T22:07:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 42,
 '_byte[7]': 0,
 'bg': 291,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.2,
 'carb_input': 0,
 'carb_ratio': 6,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x23                                  [#
    decimal
             91   35
    datetime (2015-04-15T22:07:58)
    0000   0x7a 0x07 0x16 0x0f 0x0f                   z....
    body (13)
    hex
    0000   0x00 0x51 0x06 0x28 0x5a 0x2a 0x00 0x00    .Q.(Z*..
    0008   0x00 0x00 0x00 0x2a 0x78                   ...*x
    decimal
              0   81    6   40   90   42    0    0
              0    0    0   42  120

#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 478, 'amount': 0.05}]
```
    op hex (5)
    0000   0x5c 0x05 0x02 0xde 0x14                   \....
    decimal
             92    5    2  222   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2015-04-15T22:07:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'duration': 0, 'programmed': 4.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2015-04-15T22:07:58)
    0000   0x7a 0x07 0x96 0x0f 0x0f                   z....
    body (0)

#### RECORD 23 SensorAlert 2015-04-15T23:28:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 234}
```
    op hex (3)
    0000   0x0b 0x65 0xea                             .e.
    decimal
             11  101  234
    datetime (2015-04-15T23:28:04)
    0000   0x44 0x1c 0x37 0xaf 0x0f                   D.7..
    body (0)

#### RECORD 24 BolusWizard 2015-04-15T23:43:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 10,
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
    datetime (2015-04-15T23:43:29)
    0000   0x5d 0x2b 0x17 0x0f 0x0f                   ]+...
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80   10   40   90    0    0    0
              0    0    0    0  120

#### RECORD 25 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.65}, {'age': 104, 'amount': 1.55}]
```
    op hex (8)
    0000   0x5c 0x08 0x6a 0x5e 0x04 0x3e 0x68 0x04    \.j^.>h.
    decimal
             92    8  106   94    4   62  104    4
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2015-04-15T23:43:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'duration': 0, 'programmed': 1.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2015-04-15T23:43:30)
    0000   0x5e 0x2b 0x57 0x0f 0x0f                   ^+W..
    body (0)

#### RECORD 27 MResultTotals 2015-04-16T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x16                   .....
    decimal
              7    0    0    6   22
    datetime (2015-04-16T00:00:00)
    0000   0x4f 0x0f                                  O.
    body (0)

#### RECORD 28 Model522ResultTotals 2015-04-16T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-16T00:00:00)
    0000   0x4f 0x0f                                  O.
    body (41)
    hex
    0000   0x05 0x10 0xa3 0x34 0x31 0x09 0x00 0x00    ...41...
    0008   0x06 0x16 0x02 0xe6 0x30 0x03 0x30 0x34    ....0.04
    0010   0x00 0x41 0x03 0x30 0x34 0x01 0x30 0x25    .A.04.0%
    0018   0x02 0x00 0x3f 0x00 0x00 0x00 0x06 0x01    ..?.....
    0020   0x04 0x01 0x00 0x50 0xab 0x28 0x28 0x20    ...P.(( 
    0028   0x08                                       .
    decimal
              5   16  163   52   49    9    0    0
              6   22    2  230   48    3   48   52
              0   65    3   48   52    1   48   37
              2    0   63    0    0    0    6    1
              4    1    0   80  171   40   40   32
              8

#### RECORD 29 SensorAlert 2015-04-16T00:56:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-04-16T00:56:35)
    0000   0x63 0x38 0x20 0xb0 0x0f                   c8 ..
    body (0)

#### RECORD 30 PumpSuspend 2015-04-16T06:59:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-16T06:59:51)
    0000   0x73 0x3b 0x06 0x10 0x0f                   s;...
    body (0)

#### RECORD 31 SensorAlert 2015-04-16T07:36:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 112'}
```
    op hex (3)
    0000   0x0b 0x70 0x00                             .p.
    decimal
             11  112    0
    datetime (2015-04-16T07:36:54)
    0000   0x76 0x24 0x27 0xb0 0x0f                   v$'..
    body (0)

#### RECORD 32 SensorAlert 2015-04-16T07:42:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 113'}
```
    op hex (3)
    0000   0x0b 0x71 0x00                             .q.
    decimal
             11  113    0
    datetime (2015-04-16T07:42:59)
    0000   0x7b 0x2a 0x27 0xb0 0x0f                   {*'..
    body (0)

#### RECORD 33 PumpResume 2015-04-16T07:54:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-16T07:54:46)
    0000   0x6e 0x36 0x07 0x10 0x0f                   n6...
    body (0)

#### RECORD 34 SensorAlert 2015-04-16T09:07:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-16T09:07:00)
    0000   0x40 0x07 0x29 0xb0 0x0f                   @.)..
    body (0)

#### RECORD 35 SensorAlert 2015-04-16T10:07:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-16T10:07:00)
    0000   0x40 0x07 0x2a 0xb0 0x0f                   @.*..
    body (0)

#### RECORD 36 CalBGForPH 2015-04-16T10:08:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2015-04-16T10:08:16)
    0000   0x50 0x08 0x2a 0x70 0x0f                   P.*p.
    body (0)

#### RECORD 37 BGReceived 2015-04-16T10:08:16 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 182, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-04-16T10:08:16)
    0000   0x50 0x08 0xca 0x70 0x0f                   P..p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 38 BolusWizard 2015-04-16T10:08:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 182,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb6                                  [.
    decimal
             91  182
    datetime (2015-04-16T10:08:25)
    0000   0x59 0x08 0x0a 0x10 0x0f                   Y....
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x0f 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x0f 0x78                   ....x
    decimal
              0   80   10   40   90   15    0    0
              0    0    0   15  120

#### RECORD 39 Bolus 2015-04-16T10:08:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 0, 'programmed': 1.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2015-04-16T10:08:25)
    0000   0x59 0x08 0x4a 0x10 0x0f                   Y.J..
    body (0)

#### RECORD 40 SensorAlert 2015-04-16T10:22:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-04-16T10:22:44)
    0000   0x6c 0x16 0x2a 0xb0 0x0f                   l.*..
    body (0)

#### RECORD 41 SensorAlert 2015-04-16T11:51:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-04-16T11:51:55)
    0000   0x77 0x33 0x2b 0xb0 0x0f                   w3+..
    body (0)

#### RECORD 42 SensorAlert 2015-04-16T13:23:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-04-16T13:23:12)
    0000   0x4c 0x17 0x2d 0xb0 0x0f                   L.-..
    body (0)

#### RECORD 43 SensorAlert 2015-04-16T14:52:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-04-16T14:52:53)
    0000   0x75 0x34 0x2e 0xb0 0x0f                   u4...
    body (0)

#### RECORD 44 SensorAlert 2015-04-16T15:32:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-16T15:32:53)
    0000   0x75 0x20 0x2f 0xb0 0x0f                   u /..
    body (0)

#### RECORD 45 CalBGForPH 2015-04-16T15:34:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 220}
```
    op hex (2)
    0000   0x0a 0xdc                                  ..
    decimal
             10  220
    datetime (2015-04-16T15:34:42)
    0000   0x6a 0x22 0x2f 0x70 0x0f                   j"/p.
    body (0)

#### RECORD 46 BGReceived 2015-04-16T15:34:42 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 220, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2015-04-16T15:34:42)
    0000   0x6a 0x22 0x8f 0x70 0x0f                   j".p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 47 BolusWizard 2015-04-16T15:35:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 220,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 8,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdc                                  [.
    decimal
             91  220
    datetime (2015-04-16T15:35:02)
    0000   0x42 0x23 0x0f 0x10 0x0f                   B#...
    body (13)
    hex
    0000   0x00 0x50 0x08 0x28 0x5a 0x19 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x19 0x78                   ....x
    decimal
              0   80    8   40   90   25    0    0
              0    0    0   25  120

#### RECORD 48 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 326, 'amount': 0.6}, {'age': 336, 'amount': 0.9}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x46 0x14 0x24 0x50 0x14    \..F.$P.
    decimal
             92    8   24   70   20   36   80   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2015-04-16T15:35:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'duration': 0, 'programmed': 2.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2015-04-16T15:35:02)
    0000   0x42 0x23 0x4f 0x10 0x0f                   B#O..
    body (0)

#### RECORD 50 SensorAlert 2015-04-16T15:46:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 220}
```
    op hex (3)
    0000   0x0b 0x65 0xdc                             .e.
    decimal
             11  101  220
    datetime (2015-04-16T15:46:38)
    0000   0x66 0x2e 0x2f 0xb0 0x0f                   f./..
    body (0)

#### RECORD 51 SensorAlert 2015-04-16T17:17:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-04-16T17:17:17)
    0000   0x51 0x11 0x31 0xb0 0x0f                   Q.1..
    body (0)

#### RECORD 52 BolusWizard 2015-04-16T18:28:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 30,
 'carb_ratio': 6,
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
    datetime (2015-04-16T18:28:34)
    0000   0x62 0x1c 0x12 0x10 0x0f                   b....
    body (13)
    hex
    0000   0x1e 0x50 0x06 0x28 0x5a 0x00 0x32 0x00    .P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             30   80    6   40   90    0   50    0
              0    0    0   50  120

#### RECORD 53 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 2.5}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0xb3 0x04                   \.d..
    decimal
             92    5  100  179    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2015-04-16T18:28:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 0, 'programmed': 3.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2015-04-16T18:28:34)
    0000   0x62 0x1c 0x92 0x10 0x0f                   b....
    body (0)

#### RECORD 55 Bolus 2015-04-16T18:30:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 60, 'programmed': 1.9, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x02                        ....
    decimal
              1   19   19    2
    datetime (2015-04-16T18:30:39)
    0000   0x67 0x1e 0xb2 0x10 0x0f                   g....
    body (0)

#### RECORD 56 SensorAlert 2015-04-16T19:42:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-16T19:42:44)
    0000   0x6c 0x2a 0x33 0xb0 0x0f                   l*3..
    body (0)

#### RECORD 57 SensorAlert 2015-04-16T20:03:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-04-16T20:03:12)
    0000   0x4c 0x03 0x34 0xb0 0x0f                   L.4..
    body (0)

#### RECORD 58 SensorAlert 2015-04-16T20:22:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 72}
```
    op hex (3)
    0000   0x0b 0x66 0x48                             .fH
    decimal
             11  102   72
    datetime (2015-04-16T20:22:44)
    0000   0x6c 0x16 0x34 0xb0 0x0f                   l.4..
    body (0)

#### RECORD 59 SensorAlert 2015-04-16T20:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-16T20:34:00)
    0000   0x40 0x22 0x34 0xb0 0x0f                   @"4..
    body (0)

#### RECORD 60 SensorAlert 2015-04-16T20:43:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 71}
```
    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2015-04-16T20:43:12)
    0000   0x4c 0x2b 0x34 0xb0 0x0f                   L+4..
    body (0)

#### RECORD 61 SensorAlert 2015-04-16T21:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 73}
```
    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-04-16T21:02:44)
    0000   0x6c 0x02 0x35 0xb0 0x0f                   l.5..
    body (0)

#### RECORD 62 SensorAlert 2015-04-16T21:23:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 69}
```
    op hex (3)
    0000   0x0b 0x66 0x45                             .fE
    decimal
             11  102   69
    datetime (2015-04-16T21:23:12)
    0000   0x4c 0x17 0x35 0xb0 0x0f                   L.5..
    body (0)

#### RECORD 63 SensorAlert 2015-04-16T21:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-16T21:34:00)
    0000   0x40 0x22 0x35 0xb0 0x0f                   @"5..
    body (0)

#### RECORD 64 SensorAlert 2015-04-16T22:04:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-16T22:04:00)
    0000   0x40 0x04 0x36 0xb0 0x0f                   @.6..
    body (0)

#### RECORD 65 SensorAlert 2015-04-16T22:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-16T22:34:00)
    0000   0x40 0x22 0x36 0xb0 0x0f                   @"6..
    body (0)

#### RECORD 66 CalBGForPH 2015-04-16T22:42:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2015-04-16T22:42:42)
    0000   0x6a 0x2a 0x36 0x10 0x0f                   j*6..
    body (0)

#### RECORD 67 MResultTotals 2015-04-17T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x70                   ....p
    decimal
              7    0    0    4  112
    datetime (2015-04-17T00:00:00)
    0000   0x50 0x0f                                  P.
    body (0)

#### RECORD 68 Model522ResultTotals 2015-04-17T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-17T00:00:00)
    0000   0x50 0x0f                                  P.
    body (41)
    hex
    0000   0x05 0x00 0x9d 0x44 0xdc 0x03 0x00 0x00    ...D....
    0008   0x04 0x70 0x03 0x08 0x44 0x01 0x68 0x20    .p..D.h 
    0010   0x00 0x1e 0x01 0x68 0x20 0x00 0xc8 0x38    ...h ..8
    0018   0x00 0xa0 0x2c 0x00 0x00 0x00 0x03 0x01    ..,.....
    0020   0x02 0x00 0x00 0x00 0x95 0x45 0xe6 0xf7    .....E..
    0028   0x03                                       .
    decimal
              5    0  157   68  220    3    0    0
              4  112    3    8   68    1  104   32
              0   30    1  104   32    0  200   56
              0  160   44    0    0    0    3    1
              2    0    0    0  149   69  230  247
              3

#### RECORD 69 SensorAlert 2015-04-17T05:36:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-04-17T05:36:36)
    0000   0x64 0x24 0x25 0xb1 0x0f                   d$%..
    body (0)

#### RECORD 70 SensorAlert 2015-04-17T05:57:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 71}
```
    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2015-04-17T05:57:17)
    0000   0x51 0x39 0x25 0xb1 0x0f                   Q9%..
    body (0)

#### RECORD 71 SensorAlert 2015-04-17T06:16:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 63}
```
    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2015-04-17T06:16:36)
    0000   0x64 0x10 0x26 0xb1 0x0f                   d.&..
    body (0)

#### RECORD 72 SensorAlert 2015-04-17T06:37:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 58}
```
    op hex (3)
    0000   0x0b 0x66 0x3a                             .f:
    decimal
             11  102   58
    datetime (2015-04-17T06:37:17)
    0000   0x51 0x25 0x26 0xb1 0x0f                   Q%&..
    body (0)

#### RECORD 73 SensorAlert 2015-04-17T06:56:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 63}
```
    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2015-04-17T06:56:36)
    0000   0x64 0x38 0x26 0xb1 0x0f                   d8&..
    body (0)

#### RECORD 74 SensorAlert 2015-04-17T07:17:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-04-17T07:17:17)
    0000   0x51 0x11 0x27 0xb1 0x0f                   Q.'..
    body (0)

#### RECORD 75 PumpSuspend 2015-04-17T07:38:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-17T07:38:01)
    0000   0x41 0x26 0x07 0x11 0x0f                   A&...
    body (0)

#### RECORD 76 PumpResume 2015-04-17T08:01:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-17T08:01:24)
    0000   0x58 0x01 0x08 0x11 0x0f                   X....
    body (0)

#### RECORD 77 SensorAlert 2015-04-17T09:32:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-04-17T09:32:53)
    0000   0x75 0x20 0x29 0xb1 0x0f                   u )..
    body (0)

#### RECORD 78 SensorAlert 2015-04-17T09:42:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-17T09:42:00)
    0000   0x40 0x2a 0x29 0xb1 0x0f                   @*)..
    body (0)

#### RECORD 79 SensorAlert 2015-04-17T10:42:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-17T10:42:00)
    0000   0x40 0x2a 0x2a 0xb1 0x0f                   @**..
    body (0)

#### RECORD 80 CalBGForPH 2015-04-17T10:48:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 283}
```
    op hex (2)
    0000   0x0a 0x1b                                  ..
    decimal
             10   27
    datetime (2015-04-17T10:48:54)
    0000   0x76 0x30 0x2a 0x71 0x8f                   v0*q.
    body (0)

#### RECORD 81 BGReceived 2015-04-17T10:48:54 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 283, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2015-04-17T10:48:54)
    0000   0x76 0x30 0x6a 0x71 0x0f                   v0jq.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 82 BolusWizard 2015-04-17T10:49:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
 '_byte[7]': 0,
 'bg': 283,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1b                                  [.
    decimal
             91   27
    datetime (2015-04-17T10:49:12)
    0000   0x4c 0x31 0x0a 0x11 0x0f                   L1...
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x28 0x00 0x00    .Q.(Z(..
    0008   0x00 0x00 0x00 0x28 0x78                   ...(x
    decimal
              0   81   10   40   90   40    0    0
              0    0    0   40  120

#### RECORD 83 Bolus 2015-04-17T10:49:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'duration': 0, 'programmed': 4.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2015-04-17T10:49:12)
    0000   0x4c 0x31 0x8a 0x11 0x0f                   L1...
    body (0)

#### RECORD 84 SensorAlert 2015-04-17T11:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 280}
```
    op hex (3)
    0000   0x0b 0x65 0x18                             .e.
    decimal
             11  101   24
    datetime (2015-04-17T11:02:44)
    0000   0x6c 0x02 0x2b 0xb1 0x8f                   l.+..
    body (0)

#### RECORD 85 BolusWizard 2015-04-17T12:21:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 45,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
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
    datetime (2015-04-17T12:21:19)
    0000   0x53 0x15 0x0c 0x11 0x0f                   S....
    body (13)
    hex
    0000   0x2d 0x50 0x08 0x28 0x5a 0x00 0x38 0x00    -P.(Z.8.
    0008   0x00 0x00 0x00 0x38 0x78                   ...8x
    decimal
             45   80    8   40   90    0   56    0
              0    0    0   56  120

#### RECORD 86 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 4.0}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0x5c 0x04                   \..\.
    decimal
             92    5  160   92    4
    datetime (unknown)

    body (0)

#### RECORD 87 Bolus 2015-04-17T12:21:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-17T12:21:19)
    0000   0x53 0x15 0x8c 0x11 0x0f                   S....
    body (0)

#### RECORD 88 Bolus 2015-04-17T12:23:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 180, 'programmed': 2.6, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x06                        ....
    decimal
              1   26   26    6
    datetime (2015-04-17T12:23:18)
    0000   0x52 0x17 0xac 0x11 0x0f                   R....
    body (0)

#### RECORD 89 SensorAlert 2015-04-17T15:42:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-17T15:42:44)
    0000   0x6c 0x2a 0x2f 0xb1 0x0f                   l*/..
    body (0)

#### RECORD 90 BolusWizard 2015-04-17T17:04:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 40,
 'carb_ratio': 8,
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
    datetime (2015-04-17T17:04:07)
    0000   0x47 0x04 0x11 0x11 0x0f                   G....
    body (13)
    hex
    0000   0x28 0x50 0x08 0x28 0x5a 0x00 0x32 0x00    (P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             40   80    8   40   90    0   50    0
              0    0    0   50  120

#### RECORD 91 UnabsorbedInsulinBolus unknown head[62], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 0.05},
 {'age': 115, 'amount': 0.15},
 {'age': 125, 'amount': 0.15},
 {'age': 135, 'amount': 0.15},
 {'age': 145, 'amount': 0.15},
 {'age': 155, 'amount': 0.15},
 {'age': 165, 'amount': 0.15},
 {'age': 175, 'amount': 0.1},
 {'age': 185, 'amount': 0.15},
 {'age': 195, 'amount': 0.15},
 {'age': 205, 'amount': 0.15},
 {'age': 215, 'amount': 0.15},
 {'age': 225, 'amount': 0.15},
 {'age': 235, 'amount': 0.15},
 {'age': 245, 'amount': 0.15},
 {'age': 255, 'amount': 0.15},
 {'age': 265, 'amount': 0.1},
 {'age': 275, 'amount': 0.15},
 {'age': 285, 'amount': 3.1},
 {'age': 375, 'amount': 4.0}]
```
    op hex (62)
    0000   0x5c 0x3e 0x02 0x69 0x04 0x06 0x73 0x04    \>.i..s.
    0008   0x06 0x7d 0x04 0x06 0x87 0x04 0x06 0x91    .}......
    0010   0x04 0x06 0x9b 0x04 0x06 0xa5 0x04 0x04    ........
    0018   0xaf 0x04 0x06 0xb9 0x04 0x06 0xc3 0x04    ........
    0020   0x06 0xcd 0x04 0x06 0xd7 0x04 0x06 0xe1    ........
    0028   0x04 0x06 0xeb 0x04 0x06 0xf5 0x04 0x06    ........
    0030   0xff 0x04 0x04 0x09 0x14 0x06 0x13 0x14    ........
    0038   0x7c 0x1d 0x14 0xa0 0x77 0x14              |...w.
    decimal
             92   62    2  105    4    6  115    4
              6  125    4    6  135    4    6  145
              4    6  155    4    6  165    4    4
            175    4    6  185    4    6  195    4
              6  205    4    6  215    4    6  225
              4    6  235    4    6  245    4    6
            255    4    4    9   20    6   19   20
            124   29   20  160  119   20
    datetime (unknown)

    body (0)

#### RECORD 92 Bolus 2015-04-17T17:04:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'duration': 0, 'programmed': 5.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2015-04-17T17:04:08)
    0000   0x48 0x04 0x51 0x11 0x0f                   H.Q..
    body (0)

#### RECORD 93 SensorAlert 2015-04-17T21:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-04-17T21:02:44)
    0000   0x6c 0x02 0x35 0xb1 0x0f                   l.5..
    body (0)

#### RECORD 94 BolusWizard 2015-04-17T21:40:22 head[2], body[13] op[0x5b]
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
    datetime (2015-04-17T21:40:22)
    0000   0x56 0x28 0x15 0x11 0x0f                   V(...
    body (13)
    hex
    0000   0x00 0x50 0x06 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80    6   40   90    0    0    0
              0    0    0    0  120

`end ReadHistoryData-page-8.data: 95 records`
