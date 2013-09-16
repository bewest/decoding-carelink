## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 161, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9b 0x0d 0x4a 0x7d 0x0c 0x7b 0x03 0x80    ..J}.{..
    0008   0x00 0x0d 0x1d 0x0c 0x1a 0x26 0x00 0x5b    .....&.[
    0010   0x00 0x84 0x07 0x0d 0x7d 0x0c 0x22 0x90    ....}.".
    0018   0x00 0x6e 0x17 0x36 0x00 0x00 0x78 0x00    .n.6..x.
##### DEBUG DECIMAL
            155   13   74  125   12  123    3  128
              0   13   29   12   26   38    0   91
              0  132    7   13  125   12   34  144
              0  110   23   54    0    0  120    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 2.7, 'curve': 4},
 {'age': 49, 'amount': 0.1, 'curve': 20},
 {'age': 59, 'amount': 3.2, 'curve': 20},
 {'age': 69, 'amount': 3.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0x9b 0x04 0x04 0x31 0x14    \.l...1.
    0008   0x80 0x3b 0x14 0x8c 0x45 0x14              .;..E.
    decimal
             92   14  108  155    4    4   49   20
            128   59   20  140   69   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-08-29T00:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x04 0x00 0x04 0x00 0x20 0x00    ...... .
    decimal
              1    0    4    0    4    0   32    0
    datetime (2012-08-29T00:19:46)
    0000   0xae 0x13 0x40 0x7d 0x0c                   ..@}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 2 Rewind 2012-08-29T00:36:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-29T00:36:04)
    0000   0x84 0x24 0x00 0x1d 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 Prime 2012-08-29T00:37:24 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2b                   ....+
    decimal
              3    0    0    0   43
    datetime (2012-08-29T00:37:24)
    0000   0x98 0x25 0x20 0x1d 0x0c                   .% ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BasalProfileStart 2012-08-29T00:37:39 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-29T00:37:39)
    0000   0xa7 0x25 0x00 0x1d 0x0c                   .%...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2012-08-29T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-29T04:00:00)
    0000   0x80 0x00 0x04 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 6 CalBGForPH 2012-08-29T07:55:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2012-08-29T07:55:42)
    0000   0xaa 0x37 0x27 0x7d 0x0c                   .7'}.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2012-08-29T07:55:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2012-08-29T07:55:42)
    0000   0xaa 0x37 0xa7 0x7d 0x0c                   .7.}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 LowBattery 2012-08-29T08:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-08-29T08:01:00)
    0000   0x80 0x01 0x08 0x1d 0x0c                   .....
    body (0)

#### RECORD 9 BasalProfileStart 2012-08-29T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-29T09:30:00)
    0000   0x80 0x1e 0x09 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 10 LowBattery 2012-08-29T10:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-08-29T10:01:00)
    0000   0x80 0x01 0x0a 0x1d 0x0c                   .....
    body (0)

#### RECORD 11 CalBGForPH 2012-08-29T10:13:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2012-08-29T10:13:23)
    0000   0x97 0x0d 0x2a 0x7d 0x0c                   ..*}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2012-08-29T10:13:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2012-08-29T10:13:23)
    0000   0x97 0x0d 0x2a 0x7d 0x0c                   ..*}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2012-08-29T10:13:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 98,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 7.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2012-08-29T10:13:27)
    0000   0x9b 0x0d 0x0a 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x4c 0x00    ...n.6L.
    0008   0x00 0x00 0x00 0x00 0x00 0x4c 0x36         .....L6
    decimal
              0  144    0  110   23   54   76    0
              0    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 14 Ian69 2012-08-29T10:13:27 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-29T10:13:27)
    0000   0x9b 0x0d 0x0a 0x1d 0x0c                   .....
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x4c 0x00 0x4c 0x00    ....L.L.
    decimal
             10   30    1    0   76    0   76    0

`end logs/ReadHistoryData-page-11.data: 15 records`
