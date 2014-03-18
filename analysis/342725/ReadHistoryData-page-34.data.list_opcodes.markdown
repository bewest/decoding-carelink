## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 153, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x19 0x7d 0x5c 0x05 0x90 0x29 0x14 0x01    .}\..)..
    0008   0x09 0x09 0x00 0x2f 0xcb 0x55 0x14 0x0d    .../.U..
    0010   0x0a 0x59 0x19 0xed 0x36 0x14 0x0d 0x5b    .Y..6..[
    0018   0x59 0x39 0xed 0x16 0x14 0x0d 0x23 0x50    Y9....#P
##### DEBUG DECIMAL
             25  125   92    5  144   41   20    1
              9    9    0   47  203   85   20   13
             10   89   25  237   54   20   13   91
             89   57  237   22   20   13   35   80
#### RECORD 0 Model522ResultTotals 2013-03-20T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-20T00:00:00)
    0000   0x33 0x8d                                  3.
    body (41)
    hex
    0000   0x05 0x10 0xac 0x5f 0x18 0x06 0x00 0x00    ..._....
    0008   0x05 0xb4 0x03 0x6c 0x3c 0x02 0x48 0x28    ...l<.H(
    0010   0x00 0x8a 0x02 0x48 0x28 0x01 0xa0 0x47    ...H(..G
    0018   0x00 0xa8 0x1d 0x00 0x00 0x00 0x06 0x04    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  172   95   24    6    0    0
              5  180    3  108   60    2   72   40
              0  138    2   72   40    1  160   71
              0  168   29    0    0    0    6    4
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-03-20T12:14:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-03-20T12:14:31)
    0000   0x1f 0xce 0x2c 0x14 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-03-20T12:15:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 244,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2013-03-20T12:15:18)
    0000   0x12 0xcf 0x0c 0x14 0x0d                   .....
    body (15)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x1a 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x3e 0x7d 0x01 0x3e         ...>}.>
    decimal
             47   80   13   45  106   26   36    0
              0    0    0   62  125    1   62
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Base (2013, 3, 20, 12, 15, 18) head[2], body[0] op[0x3e]

    op hex (2)
    0000   0x3e 0x00                                  >.
    decimal
             62    0
    datetime ((2013, 3, 20, 12, 15, 18))
    0000   0x12 0xcf 0x4c 0x14 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-03-20T16:20:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-03-20T16:20:03)
    0000   0x03 0xd4 0x30 0x14 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-03-20T16:20:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-03-20T16:20:38)
    0000   0x26 0xd4 0x10 0x14 0x0d                   &....
    body (15)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d 0x5c 0x05         ...$}\.
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125   92    5
    HOUR BITS: [1, 1, 0]
#### RECORD 6 Base (2000, 0, 4, 4, 1, 4) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0xf6                                  ..
    decimal
            248  246
    datetime ((2000, 0, 4, 4, 1, 4))
    0000   0x04 0x01 0x24 0x24 0x00                   ..$$.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 7 EnableDisableRemote 2009-04-10T13:20:16 head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0xd4                                  &.
    decimal
             38  212
    datetime (2009-04-10T13:20:16)
    0000   0x50 0x14 0x0d 0x0a 0x59                   P...Y
    body (14)
    hex
    0000   0x15 0xcf 0x31 0x14 0x0d 0x0a 0xd3 0x2e    ..1.....
    0008   0xc9 0x35 0x14 0x0d 0x5b 0xd3              .5..[.
    decimal
             21  207   49   20   13   10  211   46
            201   53   20   13   91  211
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2000, 0, 9, 13, 20, 21) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0xcb                                  /.
    decimal
             47  203
    datetime ((2000, 0, 9, 13, 20, 21))
    0000   0x15 0x14 0x0d 0x09 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 9 Base (2000, 4, 0, 6, 19, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 6, 19, 42))
    0000   0x6a 0x13 0x06 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-34.data: 10 records`
