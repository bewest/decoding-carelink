## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 348, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x86 0x16 0x53 0x7d 0x0c 0x5b 0x00 0x99    ..S}.[..
    0008   0x38 0x14 0x7d 0x0c 0x14 0x90 0x00 0x6e    8.}....n
    0010   0x17 0x36 0x00 0x00 0x48 0x00 0x00 0x00    .6..H...
    0018   0x00 0x48 0x36 0x5c 0x11 0x1a 0x5c 0x04    .H6\..\.
##### DEBUG DECIMAL
            134   22   83  125   12   91    0  153
             56   20  125   12   20  144    0  110
             23   54    0    0   72    0    0    0
              0   72   54   92   17   26   92    4
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
#### RECORD 7 Base (2012, 8, 29, 7, 55, 42) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime ((2012, 8, 29, 7, 55, 42))
    0000   0xaa 0x37 0xa7 0x7d 0x0c                   .7.}.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian69 (2001, 8, 0, 0, 25, 22) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2001, 8, 0, 0, 25, 22))
    0000   0x96 0x19 0x00 0x80 0x01                   .....
    body (8)
    hex
    0000   0x08 0x1d 0x0c 0x7b 0x02 0x80 0x1e 0x09    ...{....
    decimal
              8   29   12  123    2  128   30    9
    DAY BITS: [1, 0, 0]
#### RECORD 9 Base (2000, 0, 25, 0, 30, 19) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0x0c                                  ..
    decimal
             29   12
    datetime ((2000, 0, 25, 0, 30, 19))
    0000   0x13 0x1e 0x00 0x19 0x00                   .....
    body (0)

#### RECORD 10 Base (2001, 0, 10, 12, 29, 10) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x01                                  ..
    decimal
            128    1
    datetime ((2001, 0, 10, 12, 29, 10))
    0000   0x0a 0x1d 0x0c 0x0a 0xb1                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 11 Base (2006, 1, 31, 12, 61, 42) head[2], body[0] op[0x97]

    op hex (2)
    0000   0x97 0x0d                                  ..
    decimal
            151   13
    datetime ((2006, 1, 31, 12, 61, 42))
    0000   0x2a 0x7d 0x0c 0x3f 0x16                   *}.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 12 Base (2009, 1, 9, 12, 61, 42) head[2], body[0] op[0x97]

    op hex (2)
    0000   0x97 0x0d                                  ..
    decimal
            151   13
    datetime ((2009, 1, 9, 12, 61, 42))
    0000   0x2a 0x7d 0x0c 0x69 0x69                   *}.ii
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2013, 6, 10, 13, 27, 34) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x5b                                  .[
    decimal
            150   91
    datetime ((2013, 6, 10, 13, 27, 34))
    0000   0x62 0x9b 0x0d 0x0a 0x7d                   b...}
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 14 ClearAlarm 2006-08-23T14:00:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x00                                  ..
    decimal
             12    0
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 15 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x00                                  L.
    decimal
             76    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 16 Base (2010, 4, 13, 27, 8, 41) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x36                                  L6
    decimal
             76   54
    datetime ((2010, 4, 13, 27, 8, 41))
    0000   0x69 0x08 0x9b 0x0d 0x0a                   i....
    body (0)

#### RECORD 17 Base (2012, 0, 0, 1, 30, 10) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0x0c                                  ..
    decimal
             29   12
    datetime ((2012, 0, 0, 1, 30, 10))
    0000   0x0a 0x1e 0x01 0x00 0x4c                   ....L
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 18 Base (2013, 0, 27, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x4c                                  .L
    decimal
              0   76
    datetime ((2013, 0, 27, 0, 0, 0))
    0000   0x00 0x00 0x00 0x9b 0x0d                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 19 Base (2000, 1, 0, 3, 59, 12) head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0x7d                                  J}
    decimal
             74  125
    datetime ((2000, 1, 0, 3, 59, 12))
    0000   0x0c 0x7b 0x03 0x80 0x00                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 20 Base (2011, 0, 0, 6, 26, 12) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1d                                  ..
    decimal
             13   29
    datetime ((2011, 0, 0, 6, 26, 12))
    0000   0x0c 0x1a 0x26 0x00 0x5b                   ..&.[
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 21 Base (2002, 0, 12, 29, 13, 7) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x84                                  ..
    decimal
              0  132
    datetime ((2002, 0, 12, 29, 13, 7))
    0000   0x07 0x0d 0x7d 0x0c 0x22                   ..}."
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 22 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 23 Base (2006, 0, 24, 0, 0, 0) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x00                                  x.
    decimal
            120    0
    datetime ((2006, 0, 24, 0, 0, 0))
    0000   0x00 0x00 0x00 0x78 0x36                   ...x6
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 1.1, 'curve': 4},
 {'age': 183, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0xad 0x04 0x20 0xb7 0x04    \.,.. ..
    decimal
             92    8   44  173    4   32  183    4
    datetime (unknown)

    body (0)

#### RECORD 25 Ian69 2012-08-29T13:07:04 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-29T13:07:04)
    0000   0x84 0x07 0x0d 0x1d 0x0c                   .....
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x78 0x00 0x78 0x00    ....x.x.
    decimal
             14   30    1    0  120    0  120    0

#### RECORD 26 Base (2012, 8, 29, 13, 7, 4) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2012, 8, 29, 13, 7, 4))
    0000   0x84 0x07 0x4d 0x7d 0x0c                   ..M}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2012-08-29T15:12:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 278}
```
    op hex (2)
    0000   0x0a 0x16                                  ..
    decimal
             10   22
    datetime (2012-08-29T15:12:03)
    0000   0x83 0x0c 0x2f 0x7d 0x8c                   ../}.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 28 Base (2012, 8, 29, 15, 12, 3) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime ((2012, 8, 29, 15, 12, 3))
    0000   0x83 0x0c 0xcf 0x7d 0x0c                   ...}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 29 Ian69 (2012, 8, 6, 27, 10, 22) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2012, 8, 6, 27, 10, 22))
    0000   0x96 0x0a 0x9b 0x86 0x0c                   .....
    body (8)
    hex
    0000   0x4f 0xdd 0x0c 0x5b 0x9b 0x88 0x0c 0x0f    O..[....
    decimal
             79  221   12   91  155  136   12   15
    DAY BITS: [1, 0, 0]
#### RECORD 30 Base (2007, 2, 14, 0, 16, 0) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x0c                                  }.
    decimal
            125   12
    datetime ((2007, 2, 14, 0, 16, 0))
    0000   0x00 0x90 0x00 0x6e 0x17                   ...n.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 31 Base (2004, 0, 0, 0, 0, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0xac                                  6.
    decimal
             54  172
    datetime ((2004, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x34                   ....4
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 32 Base (2000, 1, 24, 11, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 1, 24, 11, 28, 54))
    0000   0x36 0x5c 0x0b 0x78 0x80                   6\.x.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 Base (2004, 0, 20, 0, 20, 42) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x2c                                  .,
    decimal
              4   44
    datetime ((2004, 0, 20, 0, 20, 42))
    0000   0x2a 0x14 0x20 0x34 0x14                   *. 4.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 34 Bolus 2012-08-29T15:12:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x34 0x00    ..x.x.4.
    decimal
              1    0  120    0  120    0   52    0
    datetime (2012-08-29T15:12:08)
    0000   0x88 0x0c 0x4f 0x7d 0x0c                   ..O}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2012-08-29T19:22:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 38,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 136}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-29T19:22:06)
    0000   0x86 0x16 0x13 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x26 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    &..n.6..
    0008   0x88 0x00 0x00 0x00 0x00 0x88 0x36         ......6
    decimal
             38  144    0  110   23   54    0    0
            136    0    0    0    0  136   54
    DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 248, 'amount': 0.25, 'curve': 4},
 {'age': 2, 'amount': 2.75, 'curve': 20},
 {'age': 122, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0a 0xf8 0x04 0x6e 0x02 0x14    \....n..
    0008   0x78 0x7a 0x14                             xz.
    decimal
             92   11   10  248    4  110    2   20
            120  122   20
    datetime (unknown)

    body (0)

#### RECORD 37 Ian69 2012-08-29T19:22:06 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-29T19:22:06)
    0000   0x86 0x16 0x73 0x1d 0x0c                   ..s..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0x88 0x00 0x88 0x00    ........
    decimal
             21   30    1    0  136    0  136    0

`end logs/ReadHistoryData-page-11.data: 38 records`
