## START analysis/736868/logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 1002, found 20 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x48 0x49                                  HI
##### DEBUG DECIMAL
             72   73
#### RECORD 0 Sara6E 2015-03-11T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-11T00:00:00)
    0000   0x2a 0x8f                                  *.
    body (49)
    hex
    0000   0x05 0x10 0x9a 0x33 0x00 0x02 0x00 0x00    ...3....
    0008   0x0a 0x06 0x03 0x16 0x1f 0x06 0xf0 0x45    .......E
    0010   0x00 0x92 0x02 0xbc 0x01 0xb4 0x00 0x00    ........
    0018   0x02 0x80 0x03 0x02 0x00 0x07 0x00 0xc7    ........
    0020   0x37 0x2c 0x01 0x20 0x4e 0x02 0x01 0x00    7,. N...
    0028   0x00 0x01 0x09 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  154   51    0    2    0    0
             10    6    3   22   31    6  240   69
              0  146    2  188    1  180    0    0
              2  128    3    2    0    7    0  199
             55   44    1   32   78    2    1    0
              0    1    9    1    0    0    0    0
              0

#### RECORD 1 SensorAlert 2015-03-11T00:49:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-11T00:49:01)
    0000   0x01 0xf1 0x20 0xab 0x0f                   .. ..
    body (0)

#### RECORD 2 SensorAlert 2015-03-11T00:58:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-11T00:58:52)
    0000   0x34 0xfa 0x20 0xab 0x0f                   4. ..
    body (0)

#### RECORD 3 SensorAlert 2015-03-11T03:59:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 20}
```
    op hex (3)
    0000   0x0b 0x65 0x14                             .e.
    decimal
             11  101   20
    datetime (2015-03-11T03:59:20)
    0000   0x14 0xfb 0x23 0xab 0x8f                   ..#..
    body (0)

#### RECORD 4 BasalProfileStart 2015-03-11T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-11T04:00:00)
    0000   0x00 0xc0 0x04 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 5 SensorAlert 2015-03-11T05:29:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 90}
```
    op hex (3)
    0000   0x0b 0x65 0x5a                             .eZ
    decimal
             11  101   90
    datetime (2015-03-11T05:29:01)
    0000   0x01 0xdd 0x25 0xab 0x8f                   ..%..
    body (0)

#### RECORD 6 CalBGForPH 2015-03-11T06:44:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 392}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2015-03-11T06:44:48)
    0000   0x30 0xec 0x26 0x6b 0x8f                   0.&k.
    body (0)

#### RECORD 7 BGReceived 2015-03-11T06:44:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x31                                  ?1
    decimal
             63   49
    datetime (2015-03-11T06:44:48)
    0000   0x30 0xec 0x06 0x6b 0x0f                   0..k.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 8 BolusWizard 2015-03-11T06:45:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 392,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2015-03-11T06:45:08)
    0000   0x08 0xed 0x06 0x0b 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0x10 0x00    .Q.d(Z..
    0008   0x00 0x08 0x00 0x00 0x01 0x10 0x78         ......x
    decimal
              0   81    0  100   40   90   16    0
              0    8    0    0    1   16  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 190, 'amount': 1.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0xbe 0x14                   \.<..
    decimal
             92    5   60  190   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2015-03-11T06:45:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4,
 'duration': 0,
 'programmed': 0.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x10 0x01 0x10 0x00 0x00 0x00    ........
    decimal
              1    1   16    1   16    0    0    0
    datetime (2015-03-11T06:45:08)
    0000   0x08 0xed 0x46 0x0b 0x0f                   ..F..
    body (0)

#### RECORD 11 SensorAlert 2015-03-11T06:58:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 134}
```
    op hex (3)
    0000   0x0b 0x65 0x86                             .e.
    decimal
             11  101  134
    datetime (2015-03-11T06:58:52)
    0000   0x34 0xfa 0x26 0xab 0x8f                   4.&..
    body (0)

#### RECORD 12 BasalProfileStart 2015-03-11T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-11T07:00:00)
    0000   0x00 0xc0 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 13 PumpSuspend 2015-03-11T07:00:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-11T07:00:53)
    0000   0x35 0xc0 0x07 0x0b 0x0f                   5....
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-11T07:20:46 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-11T07:20:46)
    0000   0x2e 0xd4 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 15 PumpResume 2015-03-11T07:20:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-11T07:20:46)
    0000   0x2e 0xd4 0x07 0x0b 0x0f                   .....
    body (0)

#### RECORD 16 BolusWizard 2015-03-11T07:32:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 36,
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
    datetime (2015-03-11T07:32:51)
    0000   0x33 0xe0 0x07 0x6b 0x0f                   3..k.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    $P.d(Z..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x78         ......x
    decima