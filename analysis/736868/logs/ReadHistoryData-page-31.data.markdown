## START analysis/736868/logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb9 0x44                                  .D
##### DEBUG DECIMAL
            185   68
#### RECORD 0 SensorAlert 2015-02-11T09:33:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-11T09:33:03)
    0000   0x03 0xa1 0x29 0xab 0x0f                   ..)..
    body (0)

#### RECORD 1 Bolus 2015-02-11T09:33:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xb4 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  180    0
    datetime (2015-02-11T09:33:26)
    0000   0x1a 0xa1 0x49 0x6b 0x0f                   ..Ik.
    body (0)

#### RECORD 2 BasalProfileStart 2015-02-11T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-11T10:00:00)
    0000   0x00 0x80 0x0a 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 3 SensorAlert 2015-02-11T10:13:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-11T10:13:00)
    0000   0x00 0x8d 0x2a 0xab 0x0f                   ..*..
    body (0)

#### RECORD 4 CalBGForPH 2015-02-11T10:17:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2015-02-11T10:17:14)
    0000   0x0e 0x91 0x2a 0x6b 0x0f                   ..*k.
    body (0)

#### RECORD 5 BGReceived 2015-02-11T10:17:14 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-11T10:17:14)
    0000   0x0e 0x91 0x4a 0x6b 0x0f                   ..Jk.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 6 BasalProfileStart 2015-02-11T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-11T12:00:00)
    0000   0x00 0x80 0x0c 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 7 BolusWizard 2015-02-11T12:08:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 1.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-11T12:08:15)
    0000   0x0f 0x88 0x0c 0x6b 0x0f                   ...k.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 8 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 1.0, 'curve': 4},
 {'age': 232, 'amount': 1.5, 'curve': 4},
 {'age': 16, 'amount': 1.25, 'curve': 20},
 {'age': 26, 'amount': 5.5, 'curve': 20},
 {'age': 36, 'amount': 1.25, 'curve': 20},
 {'age': 186, 'amount': 1.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x28 0xa2 0x04 0x3c 0xe8 0x04    \.(..<..
    0008   0x32 0x10 0x14 0xdc 0x1a 0x14 0x32 0x24    2.....2$
    0010   0x14 0x28 0xba 0x14                        .(..
    decimal
             92   20   40  162    4   60  232    4
             50   16   20  220   26   20   50   36
             20   40  186   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2015-02-11T12:10:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 90,
 'programmed': 3.5,
 'type': 'square',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x10 0x03    ........
    decimal
              1    0  140    0  140    0   16    3
    datetime (2015-02-11T12:10:55)
    0000   0x37 0x8a 0xac 0x6b 0x0f                   7..k.
    body (0)

#### RECORD 10 Bolus 2015-02-11T12:08:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x10 0x00    ........
    decimal
              1    0  160    0  160    0   16    0
    datetime (2015-02-11T12:08:15)
    0000   0x0f 0x88 0x8c 0x6b 0x0f                   ...k.
    body (0)

#### RECORD 11 SensorAlert 2015-02-11T12:23:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-11T12:23:41)
    0000   0x29 0x97 0x2c 0xab 0x0f                   ).,..
    body (0)

#### RECORD 12 SensorAlert 2015-02-11T12:34:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-11T12:34:29)
    0000   0x1d 0xa2 0x2c 0xab 0x0f                   ..,..
    body (0)

#### RECORD 13 BasalProfileStart 2015-02-11T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-11T15:00:00)
    0000   0x00 0x80 0x0f 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 14 SensorAlert 2015-02-11T17:59:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-11T17:59:17)
    0000   0x11 0xbb 0x31 0xab 0x0f                   ..1..
    body (0)

#### RECORD 15 SensorAlert 2015-02-11T18:03:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-11T18:03:00)
    0000   0x00 0x83 0x32 0xab 0x0f                   ..2..
    body (0)

#### RECORD 16 Bolus 2015-02-11T18:14:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2015-02-11T18:14:00)
    0000   0x00 0x8e 0x52 0x6b 0x0f                   ..Rk.
    body (0)

#### RECORD 17 BolusWizard 2015-02-11T19:28:57 head[2], body[15] op[0x5b]
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
    datetime (2015-02-11T19:28:57)
    0000   0x39 0x9c 0x13 0x6b 0x0f                   9..k.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    <P.<(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             60   80    0   60   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 18 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 1.0, 'curve': 4},
 {'age': 96, 'amount': 0.2, 'curve': 20},
 {'age': 106, 'amount': 0.4, 'curve': 20},
 {'age': 116, 'amount': 0.35, 'curve': 20},
 {'age': 126, 'amount': 0.4, 'curve': 20},
 {'age': 136, 'amount': 0.4, 'curve': 20},
 {'age': 146, 'amount': 0.4, 'curve': 20},
 {'age': 156, 'amount': 0.35, 'curve': 20},
 {'age': 166, 'amount': 0.4, 'curve': 20},
 {'age': 176, 'amount': 0.4, 'curve': 20},
 {'age': 186, 'amount': 4.2, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x28 0x52 0x04 0x08 0x60 0x14    \#(R..`.
    0008   0x10 0x6a 0x14 0x0e 0x74 0x14 0x10 0x7e    .j..t..~
    0010   0x14 0x10 0x88 0x14 0x10 0x92 0x14 0x0e    ........
    0018   0x9c 0x14 0x10 0xa6 0x14 0x10 0xb0 0x14    ........
    0020   0xa8 0xba 0x14                             ...
    decimal
             92   35   40   82    4    8   96   20
             16  106   20   14  116   20   16  126
             20   16  136   20   16  146   20   14
            156   20   16  166   20   16  176   20
            168  186   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2015-02-11T19:34:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 60,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x1c 0x02    ..d.d...
    decimal
              1    0  100    0  100    0   28    2
    datetime (2015-02-11T19:34:01)
    0000   0x01 0xa2 0xb3 0x6b 0x0f                   ...k.
    body (0)

#### RECORD 20 SensorAlert 2015-02-11T19:33:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 227}
```
    op hex (3)
    0000   0x0b 0x65 0xe3                             .e.
    decimal
             11  101  227
    datetime (2015-02-11T19:33:02)
    0000   0x02 0xa1 0x33 0xab 0x0f                   ..3..
    body (0)

#### RECORD 21 Bolus 2015-02-11T19:28:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x01 0x2c 0x00 0x1c 0x00    ..,.,...
    decimal
              1    1   44    1   44    0   28    0
    datetime (2015-02-11T19:28:57)
    0000   0x39 0x9c 0x93 0x6b 0x0f                   9..k.
    body (0)

#### RECORD 22 BolusWizard 2015-02-11T20:45:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 24,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-11T20:45:40)
    0000   0x28 0xad 0x14 0x6b 0x0f                   (..k.
    body (15)
    hex
    0000   0x18 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             24   80    0   60   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 23 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 0.35, 'curve': 4},
 {'age': 29, 'amount': 0.4, 'curve': 4},
 {'age': 39, 'amount': 0.4, 'curve': 4},
 {'age': 49, 'amount': 0.45, 'curve': 4},
 {'age': 59, 'amount': 0.4, 'curve': 4},
 {'age': 69, 'amount': 0.4, 'curve': 4},
 {'age': 79, 'amount': 1.2, 'curve': 5},
 {'age': 159, 'amount': 1.0, 'curve': 4},
 {'age': 173, 'amount': 0.2, 'curve': 20},
 {'age': 183, 'amount': 0.4, 'curve': 20},
 {'age': 193, 'amount': 0.35, 'curve': 20},
 {'age': 203, 'amount': 0.4, 'curve': 20},
 {'age': 213, 'amount': 0.4, 'curve': 20},
 {'age': 223, 'amount': 0.4, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x0e 0x13 0x04 0x10 0x1d 0x04    \,......
    0008   0x10 0x27 0x04 0x12 0x31 0x04 0x10 0x3b    .'..1..;
    0010   0x04 0x10 0x45 0x04 0x30 0x4f 0x05 0x28    ..E.0O.(
    0018   0x9f 0x04 0x08 0xad 0x14 0x10 0xb7 0x14    ........
    0020   0x0e 0xc1 0x14 0x10 0xcb 0x14 0x10 0xd5    ........
    0028   0x14 0x10 0xdf 0x14                        ....
    decimal
             92   44   14   19    4   16   29    4
             16   39    4   18   49    4   16   59
              4   16   69    4   48   79    5   40
            159    4    8  173   20   16  183   20
             14  193   20   16  203   20   16  213
             20   16  223   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2015-02-11T20:45:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x01 0x38 0x00    ......8.
    decimal
              1    0  160    0  160    1   56    0
    datetime (2015-02-11T20:45:41)
    0000   0x29 0xad 0x54 0x6b 0x0f                   ).Tk.
    body (0)

#### RECORD 25 SensorAlert 2015-02-11T21:17:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-11T21:17:00)
    0000   0x00 0x91 0x35 0xab 0x0f                   ..5..
    body (0)

#### RECORD 26 BasalProfileStart 2015-02-11T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-11T22:00:00)
    0000   0x00 0x80 0x16 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 27 SensorAlert 2015-02-11T22:17:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-11T22:17:00)
    0000   0x00 0x91 0x36 0xab 0x0f                   ..6..
    body (0)

#### RECORD 28 SensorAlert 2015-02-11T22:47:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-11T22:47:00)
    0000   0x00 0xaf 0x36 0xab 0x0f                   ..6..
    body (0)

#### RECORD 29 CalBGForPH 2015-02-11T22:48:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2015-02-11T22:48:20)
    0000   0x14 0xb0 0x36 0x6b 0x0f                   ..6k.
    body (0)

#### RECORD 30 BGReceived 2015-02-11T22:48:20 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-02-11T22:48:20)
    0000   0x14 0xb0 0x56 0x6b 0x0f                   ..Vk.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 31 PumpSuspend 2015-02-11T23:03:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-11T23:03:30)
    0000   0x1e 0x83 0x17 0x0b 0x0f                   .....
    body (0)

#### RECORD 32 SensorAlert 2015-02-11T23:03:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 208}
```
    op hex (3)
    0000   0x0b 0x65 0xd0                             .e.
    decimal
             11  101  208
    datetime (2015-02-11T23:03:41)
    0000   0x29 0x83 0x37 0xab 0x0f                   ).7..
    body (0)

#### RECORD 33 BasalProfileStart 2015-02-11T23:15:07 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-11T23:15:07)
    0000   0x07 0x8f 0x17 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 34 PumpResume 2015-02-11T23:15:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-11T23:15:08)
    0000   0x08 0x8f 0x17 0x0b 0x0f                   .....
    body (0)

#### RECORD 35 TempBasal 2015-02-11T23:15:33 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 3.675}
```
    op hex (2)
    0000   0x33 0x93                                  3.
    decimal
             51  147
    datetime (2015-02-11T23:15:33)
    0000   0x21 0x8f 0x17 0x0b 0x0f                   !....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 36 TempBasalDuration 2015-02-11T23:15:33 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 240}
```
    op hex (2)
    0000   0x16 0x08                                  ..
    decimal
             22    8
    datetime (2015-02-11T23:15:33)
    0000   0x21 0x8f 0x17 0x0b 0x0f                   !....
    body (0)

#### RECORD 37 MResultTotals 2015-02-12T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0xe7                   .....
    decimal
              7    0    0    8  231
    datetime (2015-02-12T00:00:00)
    0000   0x2b 0x0f                                  +.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 38 Sara6E 2015-02-12T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-12T00:00:00)
    0000   0x2b 0x0f                                  +.
    body (49)
    hex
    0000   0x05 0x00 0xc6 0xba 0xd2 0x02 0x00 0x00    ........
    0008   0x08 0xe7 0x03 0x0d 0x22 0x05 0xda 0x42    ...."..B
    0010   0x00 0xe0 0x04 0x9c 0x00 0x62 0x00 0x00    .....b..
    0018   0x00 0xdc 0x05 0x00 0x00 0x05 0x00 0xb4    ........
    0020   0x33 0x31 0x00 0x17 0x28 0x04 0x00 0x00    31..(...
    0028   0x00 0x00 0x0a 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  198  186  210    2    0    0
              8  231    3   13   34    5  218   66
              0  224    4  156    0   98    0    0
              0  220    5    0    0    5    0  180
             51   49    0   23   40    4    0    0
              0    0   10    1    0    0    0    0
              0

#### RECORD 39 Bolus 2015-02-12T00:00:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x1c 0x00    ........
    decimal
              1    0  140    0  140    0   28    0
    datetime (2015-02-12T00:00:44)
    0000   0x2c 0x80 0x40 0x6c 0x0f                   ,.@l.
    body (0)

#### RECORD 40 SensorAlert 2015-02-12T00:34:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 27}
```
    op hex (3)
    0000   0x0b 0x65 0x1b                             .e.
    decimal
             11  101   27
    datetime (2015-02-12T00:34:29)
    0000   0x1d 0xa2 0x20 0xac 0x8f                   .. ..
    body (0)

#### RECORD 41 Bolus 2015-02-12T01:04:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.8}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x70 0x00    ..x.x.p.
    decimal
              1    0  120    0  120    0  112    0
    datetime (2015-02-12T01:04:01)
    0000   0x01 0x84 0x41 0x6c 0x0f                   ..Al.
    body (0)

#### RECORD 42 SensorAlert 2015-02-12T02:03:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 195}
```
    op hex (3)
    0000   0x0b 0x65 0xc3                             .e.
    decimal
             11  101  195
    datetime (2015-02-12T02:03:00)
    0000   0x00 0x83 0x22 0xac 0x0f                   .."..
    body (0)

#### RECORD 43 BasalProfileStart 2015-02-12T03:15:33 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-12T03:15:33)
    0000   0x21 0x8f 0x03 0x0c 0x0f                   !....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 44 SensorAlert 2015-02-12T03:33:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 243}
```
    op hex (3)
    0000   0x0b 0x65 0xf3                             .e.
    decimal
             11  101  243
    datetime (2015-02-12T03:33:02)
    0000   0x02 0xa1 0x23 0xac 0x0f                   ..#..
    body (0)

#### RECORD 45 BasalProfileStart 2015-02-12T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-12T04:00:00)
    0000   0x00 0x80 0x04 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 46 Bolus 2015-02-12T04:21:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x10 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   16    0
    datetime (2015-02-12T04:21:00)
    0000   0x00 0x95 0x44 0x6c 0x0f                   ..Dl.
    body (0)

#### RECORD 47 SensorAlert 2015-02-12T05:03:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 33}
```
    op hex (3)
    0000   0x0b 0x65 0x21                             .e!
    decimal
             11  101   33
    datetime (2015-02-12T05:03:41)
    0000   0x29 0x83 0x25 0xac 0x8f                   ).%..
    body (0)

#### RECORD 48 SensorAlert 2015-02-12T06:34:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 253}
```
    op hex (3)
    0000   0x0b 0x65 0xfd                             .e.
    decimal
             11  101  253
    datetime (2015-02-12T06:34:29)
    0000   0x1d 0xa2 0x26 0xac 0x0f                   ..&..
    body (0)

#### RECORD 49 Bolus 2015-02-12T06:34:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x2c 0x00    ..x.x.,.
    decimal
              1    0  120    0  120    0   44    0
    datetime (2015-02-12T06:34:10)
    0000   0x0a 0xa2 0x46 0x6c 0x0f                   ..Fl.
    body (0)

#### RECORD 50 PumpSuspend 2015-02-12T06:41:02 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-12T06:41:02)
    0000   0x02 0xa9 0x06 0x0c 0x0f                   .....
    body (0)

#### RECORD 51 BasalProfileStart 2015-02-12T07:12:14 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-12T07:12:14)
    0000   0x0e 0x8c 0x07 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 52 PumpResume 2015-02-12T07:12:14 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-12T07:12:14)
    0000   0x0e 0x8c 0x07 0x0c 0x0f                   .....
    body (0)

#### RECORD 53 BolusWizard 2015-02-12T07:21:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-12T07:21:06)
    0000   0x06 0x95 0x07 0x6c 0x0f                   ...l.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 54 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 0.3, 'curve': 4},
 {'age': 55, 'amount': 2.7, 'curve': 4},
 {'age': 185, 'amount': 3.0, 'curve': 4},
 {'age': 119, 'amount': 0.05, 'curve': 20},
 {'age': 129, 'amount': 2.95, 'curve': 20},
 {'age': 189, 'amount': 3.5, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0c 0x2d 0x04 0x6c 0x37 0x04    \..-.l7.
    0008   0x78 0xb9 0x04 0x02 0x77 0x14 0x76 0x81    x...w.v.
    0010   0x14 0x8c 0xbd 0x14                        ....
    decimal
             92   20   12   45    4  108   55    4
            120  185    4    2  119   20  118  129
             20  140  189   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2015-02-12T07:21:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x7c 0x00    ......|.
    decimal
              1    0  160    0  160    0  124    0
    datetime (2015-02-12T07:21:06)
    0000   0x06 0x95 0x47 0x6c 0x0f                   ..Gl.
    body (0)

#### RECORD 56 SensorAlert 2015-02-12T08:03:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 203}
```
    op hex (3)
    0000   0x0b 0x65 0xcb                             .e.
    decimal
             11  101  203
    datetime (2015-02-12T08:03:00)
    0000   0x00 0x83 0x28 0xac 0x0f                   ..(..
    body (0)

#### RECORD 57 SensorAlert 2015-02-12T09:23:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-12T09:23:00)
    0000   0x00 0x97 0x29 0xac 0x0f                   ..)..
    body (0)

#### RECORD 58 SensorAlert 2015-02-12T09:33:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-12T09:33:02)
    0000   0x02 0xa1 0x29 0xac 0x0f                   ..)..
    body (0)

#### RECORD 59 SensorAlert 2015-02-12T09:43:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 107, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-02-12T09:43:41)
    0000   0x29 0xab 0x29 0xac 0x0f                   ).)..
    body (0)

#### RECORD 60 BasalProfileStart 2015-02-12T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-12T10:00:00)
    0000   0x00 0x80 0x0a 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 61 BasalProfileStart 2015-02-12T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-12T12:00:00)
    0000   0x00 0x80 0x0c 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 62 SensorAlert 2015-02-12T12:43:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-12T12:43:00)
    0000   0x00 0xab 0x2c 0xac 0x0f                   ..,..
    body (0)

#### RECORD 63 CalBGForPH 2015-02-12T12:44:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 304}
```
    op hex (2)
    0000   0x0a 0x30                                  .0
    decimal
             10   48
    datetime (2015-02-12T12:44:52)
    0000   0x34 0xac 0x2c 0x6c 0x8f                   4.,l.
    body (0)

#### RECORD 64 BGReceived 2015-02-12T12:44:52 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x26                                  ?&
    decimal
             63   38
    datetime (2015-02-12T12:44:52)
    0000   0x34 0xac 0x0c 0x6c 0x0f                   4..l.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 65 BolusWizard 2015-02-12T12:45:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 304,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.6,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -1.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x30                                  [0
    decimal
             91   48
    datetime (2015-02-12T12:45:07)
    0000   0x07 0xad 0x0c 0x0c 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x50 0x28 0x5a 0xb8 0x00    .Q.P(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0xb8 0x78         ......x
    decimal
              0   81    0   80   40   90  184    0
              0    0    0    0    0  184  120

#### RECORD 66 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 4.0, 'curve': 20},
 {'age': 113, 'amount': 0.3, 'curve': 20},
 {'age': 123, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa0 0x49 0x14 0x0c 0x71 0x14    \..I..q.
    0008   0x6c 0x7b 0x14                             l{.
    decimal
             92   11  160   73   20   12  113   20
            108  123   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2015-02-12T12:45:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6,
 'duration': 0,
 'programmed': 4.6,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xb8 0x00 0xb8 0x00 0x00 0x00    ........
    decimal
              1    0  184    0  184    0    0    0
    datetime (2015-02-12T12:45:07)
    0000   0x07 0xad 0x4c 0x0c 0x0f                   ..L..
    body (0)

#### RECORD 68 BolusWizard 2015-02-12T12:49:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 304,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 40,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -1.8,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 4.6}
```
    op hex (2)
    0000   0x5b 0x30                                  [0
    decimal
             91   48
    datetime (2015-02-12T12:49:40)
    0000   0x28 0xb1 0x0c 0x6c 0x0f                   (..l.
    body (15)
    hex
    0000   0x28 0x51 0x00 0x50 0x28 0x5a 0xb8 0x00    (Q.P(Z..
    0008   0xc8 0x00 0x00 0xb8 0x00 0xc8 0x78         ......x
    decimal
             40   81    0   80   40   90  184    0
            200    0    0  184    0  200  120

#### RECORD 69 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 3.25, 'curve': 4},
 {'age': 13, 'amount': 1.35, 'curve': 4},
 {'age': 77, 'amount': 4.0, 'curve': 20},
 {'age': 117, 'amount': 0.3, 'curve': 20},
 {'age': 127, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x82 0x03 0x04 0x36 0x0d 0x04    \....6..
    0008   0xa0 0x4d 0x14 0x0c 0x75 0x14 0x6c 0x7f    .M..u.l.
    0010   0x14                                       .
    decimal
             92   17  130    3    4   54   13    4
            160   77   20   12  117   20  108  127
             20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2015-02-12T12:49:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0xb8 0x00    ........
    decimal
              1    0  200    0  200    0  184    0
    datetime (2015-02-12T12:49:40)
    0000   0x28 0xb1 0x4c 0x6c 0x0f                   (.Ll.
    body (0)

#### RECORD 71 SensorAlert 2015-02-12T12:58:19 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 48}
```
    op hex (3)
    0000   0x0b 0x65 0x30                             .e0
    decimal
             11  101   48
    datetime (2015-02-12T12:58:19)
    0000   0x13 0xba 0x2c 0xac 0x8f                   ..,..
    body (0)

#### RECORD 72 BasalProfileStart 2015-02-12T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-12T15:00:00)
    0000   0x00 0x80 0x0f 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 73 SensorAlert 2015-02-12T15:29:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-12T15:29:08)
    0000   0x08 0x9d 0x2f 0xac 0x0f                   ../..
    body (0)

#### RECORD 74 Bolus 2015-02-12T15:30:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x58 0x00    ..P.P.X.
    decimal
              1    0   80    0   80    0   88    0
    datetime (2015-02-12T15:30:53)
    0000   0x35 0x9e 0x4f 0x6c 0x0f                   5.Ol.
    body (0)

#### RECORD 75 SensorAlert 2015-02-12T15:33:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-12T15:33:02)
    0000   0x02 0xa1 0x2f 0xac 0x0f                   ../..
    body (0)

#### RECORD 76 SensorAlert 2015-02-12T17:03:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 197}
```
    op hex (3)
    0000   0x0b 0x65 0xc5                             .e.
    decimal
             11  101  197
    datetime (2015-02-12T17:03:41)
    0000   0x29 0x83 0x31 0xac 0x0f                   ).1..
    body (0)

#### RECORD 77 SensorAlert 2015-02-12T17:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-12T17:45:00)
    0000   0x00 0xad 0x31 0xac 0x0f                   ..1..
    body (0)

#### RECORD 78 SensorAlert 2015-02-12T18:34:28 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 27}
```
    op hex (3)
    0000   0x0b 0x65 0x1b                             .e.
    decimal
             11  101   27
    datetime (2015-02-12T18:34:28)
    0000   0x1c 0xa2 0x32 0xac 0x8f                   ..2..
    body (0)

#### RECORD 79 Bolus 2015-02-12T18:35:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x0c 0x00    ........
    decimal
              1    0  240    0  240    0   12    0
    datetime (2015-02-12T18:35:42)
    0000   0x2a 0xa3 0x52 0x6c 0x0f                   *.Rl.
    body (0)

#### RECORD 80 SensorAlert 2015-02-12T18:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-12T18:45:00)
    0000   0x00 0xad 0x32 0xac 0x0f                   ..2..
    body (0)

#### RECORD 81 SensorAlert 2015-02-12T19:15:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-12T19:15:00)
    0000   0x00 0x8f 0x33 0xac 0x0f                   ..3..
    body (0)

#### RECORD 82 CalBGForPH 2015-02-12T19:44:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 41}
```
    op hex (2)
    0000   0x0a 0x29                                  .)
    decimal
             10   41
    datetime (2015-02-12T19:44:49)
    0000   0x31 0xac 0x33 0x6c 0x0f                   1.3l.
    body (0)

#### RECORD 83 BGReceived 2015-02-12T19:44:49 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x05                                  ?.
    decimal
             63    5
    datetime (2015-02-12T19:44:49)
    0000   0x31 0xac 0x33 0x6c 0x0f                   1.3l.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 84 SensorAlert 2015-02-12T19:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-12T19:45:00)
    0000   0x00 0xad 0x33 0xac 0x0f                   ..3..
    body (0)

#### RECORD 85 SensorAlert 2015-02-12T19:59:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-02-12T19:59:16)
    0000   0x10 0xbb 0x33 0xac 0x0f                   ..3..
    body (0)

`end analysis/736868/logs/ReadHistoryData-page-31.data: 86 records`
