## START logs/ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 131, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8b 0x02 0x49 0x7b 0x0c 0x7b 0x02 0x80    ..I{.{..
    0008   0x1e 0x09 0x1b 0x0c 0x13 0x1e 0x00 0x0a    ........
    0010   0x81 0xae 0x2f 0x2c 0x7b 0x0c 0x3f 0x10    ../,{.?.
    0018   0xae 0x2f 0x2c 0x7b 0x0c 0x69 0x69 0x96    ./,{.ii.
##### DEBUG DECIMAL
            139    2   73  123   12  123    2  128
             30    9   27   12   19   30    0   10
            129  174   47   44  123   12   63   16
            174   47   44  123   12  105  105  150
#### RECORD 0 Bolus 2012-08-27T00:37:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x54 0x00    ..X.X.T.
    decimal
              1    0   88    0   88    0   84    0
    datetime (2012-08-27T00:37:56)
    0000   0xb8 0x25 0x40 0x7b 0x0c                   .%@{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2012-08-27T00:43:44 head[2], body[15] op[0x5b]
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
    datetime (2012-08-27T00:43:44)
    0000   0xac 0x2b 0x00 0x7b 0x0c                   .+.{.
    body (15)
    hex
    0000   0x1f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x70 0x00 0x00 0x00 0x00 0x70 0x36         p....p6
    decimal
             31  144    0  110   23   54    0    0
            112    0    0    0    0  112   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 2.2, 'curve': 4},
 {'age': 139, 'amount': 4.2, 'curve': 4},
 {'age': 169, 'amount': 1.8, 'curve': 4},
 {'age': 63, 'amount': 1.3, 'curve': 20},
 {'age': 103, 'amount': 2.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x09 0x04 0xa8 0x8b 0x04    \.X.....
    0008   0x48 0xa9 0x04 0x34 0x3f 0x14 0x5c 0x67    H..4?.\g
    0010   0x14                                       .
    decimal
             92   17   88    9    4  168  139    4
             72  169    4   52   63   20   92  103
             20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2012-08-27T00:43:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0xa4 0x00    ........
    decimal
              1    0  132    0  132    0  164    0
    datetime (2012-08-27T00:43:44)
    0000   0xac 0x2b 0x40 0x7b 0x0c                   .+@{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 BasalProfileStart 2012-08-27T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-27T04:00:00)
    0000   0x80 0x00 0x04 0x1b 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 5 CalBGForPH 2012-08-27T08:20:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-08-27T08:20:52)
    0000   0xb4 0x14 0x28 0x7b 0x0c                   ..({.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 Ian3F 2012-08-27T08:20:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2012-08-27T08:20:52)
    0000   0xb4 0x14 0x68 0x7b 0x0c                   ..h{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 7 BolusWizard 2012-08-27T09:02:11 head[2], body[15] op[0x5b]
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
    datetime (2012-08-27T09:02:11)
    0000   0x8b 0x02 0x09 0x7b 0x0c                   ...{.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 8 Ian69 2012-08-27T09:02:11 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-27T09:02:11)
    0000   0x8b 0x02 0x09 0x1b 0x0c                   .....
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x6c 0x00 0x6c 0x00    ....l.l.
    decimal
             10   30    1    0  108    0  108    0

`end logs/ReadHistoryData-page-12.data: 9 records`
