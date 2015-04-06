## START analysis/736868/logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 999, found 23 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x98 0x7a                                  .z
##### DEBUG DECIMAL
            152  122
#### RECORD 0 Sara6E 2015-03-05T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-05T00:00:00)
    0000   0x24 0x8f                                  $.
    body (49)
    hex
    0000   0x05 0x10 0xce 0x6b 0x73 0x03 0x00 0x00    ...ks...
    0008   0x08 0x98 0x03 0x30 0x25 0x05 0x68 0x3f    ...0%.h?
    0010   0x00 0x6c 0x01 0xf0 0x00 0xf8 0x00 0x00    .l......
    0018   0x02 0x80 0x02 0x01 0x00 0x06 0x00 0x9a    ........
    0020   0x1d 0x47 0x00 0x03 0x40 0x04 0x04 0x00    .G..@...
    0028   0x00 0x00 0x07 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  206  107  115    3    0    0
              8  152    3   48   37    5  104   63
              0  108    1  240    0  248    0    0
              2  128    2    1    0    6    0  154
             29   71    0    3   64    4    4    0
              0    0    7    1    0    0    0    0
              0

#### RECORD 1 SensorAlert 2015-03-05T02:46:26 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-05T02:46:26)
    0000   0x1a 0xee 0x22 0xa5 0x0f                   .."..
    body (0)

#### RECORD 2 Bolus 2015-03-05T03:15:29 head[8], body[0] op[0x01]
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
    datetime (2015-03-05T03:15:29)
    0000   0x1d 0xcf 0x43 0x65 0x0f                   ..Ce.
    body (0)

#### RECORD 3 BasalProfileStart 2015-03-05T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-05T04:00:00)
    0000   0x00 0xc0 0x04 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 4 PumpSuspend 2015-03-05T06:45:11 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-05T06:45:11)
    0000   0x0b 0xed 0x06 0x05 0x0f                   .....
    body (0)

#### RECORD 5 BasalProfileStart 2015-03-05T07:15:15 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-05T07:15:15)
    0000   0x0f 0xcf 0x07 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 6 PumpResume 2015-03-05T07:15:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-05T07:15:16)
    0000   0x10 0xcf 0x07 0x05 0x0f                   .....
    body (0)

#### RECORD 7 CalBGForPH 2015-03-05T07:34:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2015-03-05T07:34:50)
    0000   0x32 0xe2 0x27 0x65 0x0f                   2.'e.
    body (0)

#### RECORD 8 BGReceived 2015-03-05T07:34:50 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2015-03-05T07:34:50)
    0000   0x32 0xe2 0x87 0x65 0x0f                   2..e.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 9 BolusWizard 2015-03-05T07:35:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 148,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.2,
 'carb_input': 55,
 'carb_ratio': 12.0,
 'correction_estimate': 0.7,
 'food_estimate': 5.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x94                                  [.
    decimal
             91  148
    datetime (2015-03-05T07:35:52)
    0000   0x34 0xe3 0x07 0x05 0x0f                   4....
    body (15)
    hex
    0000   0x37 0x50 0x00 0x64 0x28 0x5a 0x1c 0x00    7P.d(Z..
    0008   0xdc 0x00 0x00 0x00 0x00 0xf8 0x78         ......x
    decimal
             55   80    0  100   40   90   28    0
            220    0    0    0    0  248  120

#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 1.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x0a 0x14                   \.(..
    decimal
             92    5   40   10   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2015-03-05T07:38:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8,
 'duration': 120,
 'programmed': 2.8,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x00 0x04    ..p.p...
    decimal
              1    0  112    0  112    0    0    4
    datetime (2015-03-05T07:38:08)
    0000   0x08 0xe6 0xa7 0x05 0x0f                   .....
    body (0)

#### RECORD 12 Bolus 2015-03-05T07:35:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4,
 'duration': 0,
 'programmed': 3.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x00 0x00    ........
    decimal
              1    0  136    0  136    0    0    0
    datetime (2015-03-05T07:35:52)
    0000   0x34 0xe3 0x87 0x05 0x0f                   4....
    body (0)

#### RECORD 13 SensorAlert 2015-03-05T08:51:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-05T08:51:47)
    0000   0x2f 0xf3 0x28 0xa5 0x0f                   /.(..
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-05T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-05T10:00:00)
    0000   0x00 0xc0 0x0a 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 15 SensorAlert 2015-03-05T10:51:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-05T10:51:47)
    0000   0x2f 0xf3 0x2a 0xa5 0x0f                   /.*..
    body (0)

#### RECORD 16 SensorAlert 2015-03-05T11:02:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-03-05T11:02:35)
    0000   0x23 0xc2 0x2b 0xa5 0x0f                   #.+..
    body (0)

#### RECORD 17 Bolus 2015-03-05T11:43:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x14 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   20    0
    datetime (2015-03-05T11:43:05)
    0000   0x05 0xeb 0x4b 0x65 0x0f                   ..Ke.
    body (0)

#### RECORD 18 BasalProfileStart 2015-03-05T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-05T12:00:00)
    0000   0x00 0xc0 0x0c 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 19 SensorAlert 2015-03-05T12:31:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 30}
```
    op hex (3)
    0000   0x0b 0x65 0x1e                             .e.
    decimal
             11  101   30
    datetime (2015-03-05T12:31:06)
    0000   0x06 0xdf 0x2c 0xa5 0x8f                   ..,..
    body (0)

#### RECORD 20 Bolus 2015-03-05T13:20:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x18 0x00    ........
    decimal
              1    0  200    0  200    0   24    0
    datetime (2015-03-05T13:20:57)
    0000   0x39 0xd4 0x4d 0x65 0x0f                   9.Me.
    body (0)

#### RECORD 21 SensorAlert 2015-03-05T14:01:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 60}
```
    op hex (3)
    0000   0x0b 0x65 0x3c                             .e<
    decimal
             11  101   60
    datetime (2015-03-05T14:01:08)
    0000   0x08 0xc1 0x2e 0xa5 0x8f                   .....
    body (0)

#### RECORD 22 BasalProfileStart 2015-03-05T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-05T15:00:00)
    0000   0x00 0xc0 0x0f 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 23 Bolus 2015-03-05T15:24:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x01 0x2c 0x00 0x5c 0x00    ..,.,.\.
    decimal
              1    1   44    1   44    0   92    0
    datetime (2015-03-05T15:24:18)
    0000   0x12 0xd8 0x4f 0x65 0x0f                   ..Oe.
    body (0)

#### RECORD 24 SensorAlert 2015-03-05T15:31:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 112}
```
    op hex (3)
    0000   0x0b 0x65 0x70                             .ep
    decimal
             11  101  112
    datetime (2015-03-05T15:31:47)
    0000   0x2f 0xdf 0x2f 0xa5 0x8f                   /./..
    body (0)

#### RECORD 25 SensorAlert 2015-03-05T17:26:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-05T17:26:25)
    0000   0x19 0xda 0x31 0xa5 0x0f                   ..1..
    body (0)

#### RECORD 26 SensorAlert 2015-03-05T17:37:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-03-05T17:37:42)
    0000   0x2a 0xe5 0x31 0xa5 0x0f                   *.1..
    body (0)

#### RECORD 27 Bolus 2015-03-05T17:38:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.8}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x70 0x00    ..P.P.p.
    decimal
              1    0   80    0   80    0  112    0
    datetime (2015-03-05T17:38:01)
    0000   0x01 0xe6 0x51 0x65 0x0f                   ..Qe.
    body (0)

#### RECORD 28 SensorAlert 2015-03-05T18:35:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-05T18:35:00)
    0000   0x00 0xe3 0x32 0xa5 0x0f                   ..2..
    body (0)

#### RECORD 29 SensorAlert 2015-03-05T19:07:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 229}
```
    op hex (3)
    0000   0x0b 0x65 0xe5                             .e.
    decimal
             11  101  229
    datetime (2015-03-05T19:07:23)
    0000   0x17 0xc7 0x33 0xa5 0x0f                   ..3..
    body (0)

#### RECORD 30 Bolus 2015-03-05T19:08:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x48 0x00    ..x.x.H.
    decimal
              1    0  120    0  120    0   72    0
    datetime (2015-03-05T19:08:20)
    0000   0x14 0xc8 0x53 0x65 0x0f                   ..Se.
    body (0)

#### RECORD 31 SensorAlert 2015-03-05T19:35:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-05T19:35:00)
    0000   0x00 0xe3 0x33 0xa5 0x0f                   ..3..
    body (0)

#### RECORD 32 CalBGForPH 2015-03-05T19:36:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2015-03-05T19:36:52)
    0000   0x34 0xe4 0x33 0x65 0x0f                   4.3e.
    body (0)

#### RECORD 33 BGReceived 2015-03-05T19:36:52 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2015-03-05T19:36:52)
    0000   0x34 0xe4 0x53 0x65 0x0f                   4.Se.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 SensorAlert 2015-03-05T20:46:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-05T20:46:25)
    0000   0x19 0xee 0x34 0xa5 0x0f                   ..4..
    body (0)

#### RECORD 35 Bolus 2015-03-05T20:46:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x54 0x00    ......T.
    decimal
              1    0  140    0  140    0   84    0
    datetime (2015-03-05T20:46:47)
    0000   0x2f 0xee 0x54 0x65 0x0f                   /.Te.
    body (0)

#### RECORD 36 SensorAlert 2015-03-05T20:57:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-03-05T20:57:42)
    0000   0x2a 0xf9 0x34 0xa5 0x0f                   *.4..
    body (0)

#### RECORD 37 SensorAlert 2015-03-05T20:57:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 107, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-05T20:57:42)
    0000   0x2a 0xf9 0x34 0xa5 0x0f                   *.4..
    body (0)

#### RECORD 38 SensorAlert 2015-03-05T21:02:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-05T21:02:35)
    0000   0x23 0xc2 0x35 0xa5 0x0f                   #.5..
    body (0)

#### RECORD 39 CalBGForPH 2015-03-05T21:04:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 309}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2015-03-05T21:04:22)
    0000   0x16 0xc4 0x35 0x65 0x8f                   ..5e.
    body (0)

#### RECORD 40 BGReceived 2015-03-05T21:04:22 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x26                                  ?&
    decimal
             63   38
    datetime (2015-03-05T21:04:22)
    0000   0x16 0xc4 0xb5 0x65 0x0f                   ...e.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 41 Bolus 2015-03-05T21:04:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xc8 0x00    ........
    decimal
              1    0  140    0  140    0  200    0
    datetime (2015-03-05T21:04:49)
    0000   0x31 0xc4 0x55 0x65 0x0f                   1.Ue.
    body (0)

#### RECORD 42 SensorAlert 2015-03-05T21:17:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 53}
```
    op hex (3)
    0000   0x0b 0x65 0x35                             .e5
    decimal
             11  101   53
    datetime (2015-03-05T21:17:14)
    0000   0x0e 0xd1 0x35 0xa5 0x8f                   ..5..
    body (0)

#### RECORD 43 BasalProfileStart 2015-03-05T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-05T22:00:00)
    0000   0x00 0xc0 0x16 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 44 CalBGForPH 2015-03-05T22:37:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2015-03-05T22:37:54)
    0000   0x36 0xe5 0x36 0x65 0x0f                   6.6e.
    body (0)

#### RECORD 45 BGReceived 2015-03-05T22:37:54 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2015-03-05T22:37:54)
    0000   0x36 0xe5 0xf6 0x65 0x0f                   6..e.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 46 SensorAlert 2015-03-05T23:47:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-05T23:47:23)
    0000   0x17 0xef 0x37 0xa5 0x0f                   ..7..
    body (0)

#### RECORD 47 SensorAlert 2015-03-05T23:57:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-05T23:57:14)
    0000   0x0e 0xf9 0x37 0xa5 0x0f                   ..7..
    body (0)

#### RECORD 48 BasalProfileStart 2015-03-06T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-06T00:00:00)
    0000   0x00 0xc0 0x00 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 49 MResultTotals 2015-03-06T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x3a                   ....:
    decimal
              7    0    0    8   58
    datetime (2015-03-06T00:00:00)
    0000   0x25 0x8f                                  %.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 50 Sara6E 2015-03-06T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-06T00:00:00)
    0000   0x25 0x8f                                  %.
    body (49)
    hex
    0000   0x05 0x10 0xb5 0x6f 0x35 0x04 0x00 0x00    ...o5...
    0008   0x08 0x3a 0x03 0x1e 0x26 0x05 0x1c 0x3e    .:..&..>
    0010   0x00 0x37 0x00 0x00 0x00 0x00 0x00 0xf8    .7......
    0018   0x04 0x24 0x00 0x00 0x01 0x08 0x00 0xbb    .$......
    0020   0x24 0x40 0x00 0x19 0x4b 0x05 0x01 0x00    $@..K...
    0028   0x00 0x00 0x09 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  181  111   53    4    0    0
              8   58    3   30   38    5   28   62
              0   55    0    0    0    0    0  248
              4   36    0    0    1    8    0  187
             36   64    0   25   75    5    1    0
              0    0    9    1    0    0    0    0
              0

#### RECORD 51 SensorAlert 2015-03-06T01:26:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 246}
```
    op hex (3)
    0000   0x0b 0x65 0xf6                             .e.
    decimal
             11  101  246
    datetime (2015-03-06T01:26:25)
    0000   0x19 0xda 0x21 0xa6 0x0f                   ..!..
    body (0)

#### RECORD 52 SensorAlert 2015-03-06T02:57:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 243}
```
    op hex (3)
    0000   0x0b 0x65 0xf3                             .e.
    decimal
             11  101  243
    datetime (2015-03-06T02:57:42)
    0000   0x2a 0xf9 0x22 0xa6 0x0f                   *."..
    body (0)

#### RECORD 53 BasalProfileStart 2015-03-06T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-06T04:00:00)
    0000   0x00 0xc0 0x04 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 54 SensorAlert 2015-03-06T04:27:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 247}
```
    op hex (3)
    0000   0x0b 0x65 0xf7                             .e.
    decimal
             11  101  247
    datetime (2015-03-06T04:27:23)
    0000   0x17 0xdb 0x24 0xa6 0x0f                   ..$..
    body (0)

#### RECORD 55 Bolus 2015-03-06T04:45:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2015-03-06T04:45:15)
    0000   0x0f 0xed 0x44 0x66 0x0f                   ..Df.
    body (0)

#### RECORD 56 SensorAlert 2015-03-06T05:57:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-06T05:57:14)
    0000   0x0e 0xf9 0x25 0xa6 0x0f                   ..%..
    body (0)

#### RECORD 57 BasalProfileStart 2015-03-06T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-06T07:00:00)
    0000   0x00 0xc0 0x07 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 58 BolusWizard 2015-03-06T08:33:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 75,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-06T08:33:06)
    0000   0x06 0xe1 0x08 0x66 0x0f                   ...f.
    body (15)
    hex
    0000   0x4b 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    KP.d(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             75   80    0  100   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 59 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 4.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0xea 0x04                   \....
    decimal
             92    5  160  234    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2015-03-06T08:36:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 30,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x0c 0x01    ..P.P...
    decimal
              1    0   80    0   80    0   12    1
    datetime (2015-03-06T08:36:48)
    0000   0x30 0xe4 0xa8 0x66 0x0f                   0..f.
    body (0)

#### RECORD 61 LowReservoir 2015-03-06T08:33:42 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-06T08:33:42)
    0000   0x2a 0xe1 0x08 0x06 0x0f                   *....
    body (0)

#### RECORD 62 Bolus 2015-03-06T08:33:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5,
 'duration': 0,
 'programmed': 5.5,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x00 0x0c 0x00    ........
    decimal
              1    0  220    0  220    0   12    0
    datetime (2015-03-06T08:33:06)
    0000   0x06 0xe1 0x88 0x66 0x0f                   ...f.
    body (0)

#### RECORD 63 Bolus 2015-03-06T08:38:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 5.8}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xe8 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  232    0
    datetime (2015-03-06T08:38:47)
    0000   0x2f 0xe6 0x48 0x66 0x0f                   /.Hf.
    body (0)

#### RECORD 64 SensorAlert 2015-03-06T09:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-06T09:38:00)
    0000   0x00 0xe6 0x29 0xa6 0x0f                   ..)..
    body (0)

#### RECORD 65 BasalProfileStart 2015-03-06T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-06T10:00:00)
    0000   0x00 0xc0 0x0a 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 66 SensorAlert 2015-03-06T10:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-06T10:38:00)
    0000   0x00 0xe6 0x2a 0xa6 0x0f                   ..*..
    body (0)

#### RECORD 67 CalBGForPH 2015-03-06T10:40:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2015-03-06T10:40:08)
    0000   0x08 0xe8 0x2a 0x66 0x0f                   ..*f.
    body (0)

#### RECORD 68 BGReceived 2015-03-06T10:40:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2015-03-06T10:40:08)
    0000   0x08 0xe8 0x0a 0x66 0x0f                   ...f.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 69 LowReservoir 2015-03-06T10:46:17 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-06T10:46:17)
    0000   0x11 0xee 0x0a 0x06 0x0f                   .....
    body (0)

#### RECORD 70 SensorAlert 2015-03-06T11:57:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-06T11:57:14)
    0000   0x0e 0xf9 0x2b 0xa6 0x0f                   ..+..
    body (0)

#### RECORD 71 Bolus 2015-03-06T11:58:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x2c 0x00    ..(.(.,.
    decimal
              1    0   40    0   40    0   44    0
    datetime (2015-03-06T11:58:22)
    0000   0x16 0xfa 0x4b 0x66 0x0f                   ..Kf.
    body (0)

#### RECORD 72 BasalProfileStart 2015-03-06T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-06T12:00:00)
    0000   0x00 0xc0 0x0c 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 73 SensorAlert 2015-03-06T12:06:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-03-06T12:06:25)
    0000   0x19 0xc6 0x2c 0xa6 0x0f                   ..,..
    body (0)

#### RECORD 74 SensorAlert 2015-03-06T13:37:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 28}
```
    op hex (3)
    0000   0x0b 0x65 0x1c                             .e.
    decimal
             11  101   28
    datetime (2015-03-06T13:37:41)
    0000   0x29 0xe5 0x2d 0xa6 0x8f                   ).-..
    body (0)

#### RECORD 75 Bolus 2015-03-06T13:36:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x18 0x00    ........
    decimal
              1    0  160    0  160    0   24    0
    datetime (2015-03-06T13:36:12)
    0000   0x0c 0xe4 0x4d 0x66 0x0f                   ..Mf.
    body (0)

#### RECORD 76 Bolus 2015-03-06T13:39:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xb8 0x00    ........
    decimal
              1    0  160    0  160    0  184    0
    datetime (2015-03-06T13:39:44)
    0000   0x2c 0xe7 0x4d 0x66 0x0f                   ,.Mf.
    body (0)

#### RECORD 77 Bolus 2015-03-06T14:12:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 1.3}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x01 0x34 0x00    ..(.(.4.
    decimal
              1    0   40    0   40    1   52    0
    datetime (2015-03-06T14:12:34)
    0000   0x22 0xcc 0x4e 0x66 0x0f                   ".Nf.
    body (0)

#### RECORD 78 BasalProfileStart 2015-03-06T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-06T15:00:00)
    0000   0x00 0xc0 0x0f 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 79 SensorAlert 2015-03-06T15:07:22 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 198}
```
    op hex (3)
    0000   0x0b 0x65 0xc6                             .e.
    decimal
             11  101  198
    datetime (2015-03-06T15:07:22)
    0000   0x16 0xc7 0x2f 0xa6 0x0f                   ../..
    body (0)

#### RECORD 80 SensorAlert 2015-03-06T16:37:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 34}
```
    op hex (3)
    0000   0x0b 0x65 0x22                             .e"
    decimal
             11  101   34
    datetime (2015-03-06T16:37:13)
    0000   0x0d 0xe5 0x30 0xa6 0x8f                   ..0..
    body (0)

#### RECORD 81 Bolus 2015-03-06T16:37:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x44 0x00    ..x.x.D.
    decimal
              1    0  120    0  120    0   68    0
    datetime (2015-03-06T16:37:59)
    0000   0x3b 0xe5 0x50 0x66 0x0f                   ;.Pf.
    body (0)

#### RECORD 82 SensorAlert 2015-03-06T18:06:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 235}
```
    op hex (3)
    0000   0x0b 0x65 0xeb                             .e.
    decimal
             11  101  235
    datetime (2015-03-06T18:06:24)
    0000   0x18 0xc6 0x32 0xa6 0x0f                   ..2..
    body (0)

#### RECORD 83 Bolus 2015-03-06T18:06:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x50 0x00    ..<.<.P.
    decimal
              1    0   60    0   60    0   80    0
    datetime (2015-03-06T18:06:37)
    0000   0x25 0xc6 0x52 0x66 0x0f                   %.Rf.
    body (0)

#### RECORD 84 Bolus 2015-03-06T18:26:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.55,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 3.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x16 0x00 0x78 0x00    ..x...x.
    decimal
              1    0  120    0   22    0  120    0
    datetime (2015-03-06T18:26:40)
    0000   0x28 0xda 0x52 0x66 0x0f                   (.Rf.
    body (0)

#### RECORD 85 NoDelivery 2015-03-06T18:27:02 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-06T18:27:02)
    0000   0x02 0xdb 0x52 0x46 0x0f                   ..RF.
    body (0)

#### RECORD 86 ClearAlarm 2015-03-06T18:27:07 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-06T18:27:07)
    0000   0x07 0xdb 0x12 0x06 0x0f                   .....
    body (0)

#### RECORD 87 Rewind 2015-03-06T18:27:13 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-06T18:27:13)
    0000   0x0d 0xdb 0x12 0x06 0x0f                   .....
    body (0)

#### RECORD 88 Prime 2015-03-06T18:37:31 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x3c                   ....<
    decimal
              3    0    0    0   60
    datetime (2015-03-06T18:37:31)
    0000   0x1f 0xe5 0x32 0x06 0x0f                   ..2..
    body (0)

#### RECORD 89 BasalProfileStart 2015-03-06T18:39:38 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-06T18:39:38)
    0000   0x26 0xe7 0x12 0x06 0x0f                   &....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 90 Prime 2015-03-06T18:39:23 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-06T18:39:23)
    0000   0x17 0xe7 0x12 0x06 0x0f                   .....
    body (0)

#### RECORD 91 BolusWizard 2015-03-06T19:04:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.9,
 'carb_input': 68,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.9,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-06T19:04:22)
    0000   0x16 0xc4 0x13 0x66 0x0f                   ...f.
    body (15)
    hex
    0000   0x44 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    DP.<(Z..
    0008   0xc4 0x00 0x00 0x00 0x01 0xc4 0x78         ......x
    decimal
             68   80    0   60   40   90    0    1
            196    0    0    0    1  196  120

`end analysis/736868/logs/ReadHistoryData-page-15.data: 92 records`
