## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 57, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa7 0x16 0x52 0x75 0x0c 0x0a 0x53 0xba    ..Ru..S.
    0008   0x25 0x32 0x75 0x8c 0x3f 0x2a 0xba 0x25    %2u.?*.%
    0010   0x72 0x75 0x0c 0x69 0x69 0x96 0x0a 0xa6    ru.ii...
    0018   0x88 0x3a 0x34 0x75 0x0c 0x3f 0x14 0x88    .:4u.?..
##### DEBUG DECIMAL
            167   22   82  117   12   10   83  186
             37   50  117  140   63   42  186   37
            114  117   12  105  105  150   10  166
            136   58   52  117   12   63   20  136
#### RECORD 0 Ian3F 2012-08-21T18:22:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2d                                  ?-
    decimal
             63   45
    datetime (2012-08-21T18:22:18)
    0000   0x92 0x16 0x32 0x75 0x0c                   ..2u.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2012-08-21T18:22:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 200,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc8                                  [.
    decimal
             91  200
    datetime (2012-08-21T18:22:39)
    0000   0xa7 0x16 0x12 0x75 0x0c                   ...u.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0xfc 0x36         ......6
    decimal
              0  144    0  110   23   54  252    0
              0    0    0    0    0  252   54
    DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 248, 'amount': 3.3, 'curve': 4},
 {'age': 82, 'amount': 1.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0xf8 0x04 0x48 0x52 0x14    \....HR.
    decimal
             92    8  132  248    4   72   82   20
    datetime (unknown)

    body (0)

#### RECORD 3 Ian69 2012-08-21T18:22:39 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-21T18:22:39)
    0000   0xa7 0x16 0x72 0x15 0x0c                   ..r..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0xfc 0x00 0xfc 0x00    ........
    decimal
             21   30    1    0  252    0  252    0

`end logs/ReadHistoryData-page-16.data: 4 records`
