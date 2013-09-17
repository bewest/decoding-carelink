## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 36, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x78 0xd3 0x49 0x72 0x0d 0x0a 0x73 0x4c    x.Ir..sL
    0008   0xd4 0x2a 0x12 0x0d 0x5b 0x73 0x51 0xd4    .*..[sQ.
    0010   0x0a 0x72 0x0d 0x0b 0x50 0x00 0x78 0x3c    .r..P.x<
    0018   0x64 0x00 0x00 0x24 0x00 0x00 0x28 0x00    d..$..(.
##### DEBUG DECIMAL
            120  211   73  114   13   10  115   76
            212   42   18   13   91  115   81  212
             10  114   13   11   80    0  120   60
            100    0    0   36    0    0   40    0
#### RECORD 0 CalBGForPH 2013-07-18T09:19:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-07-18T09:19:47)
    0000   0x6f 0xd3 0x29 0x12 0x0d                   o.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BolusWizard 2013-07-18T09:19:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 92,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-07-18T09:19:56)
    0000   0x78 0xd3 0x09 0x72 0x0d                   x..r.
    body (13)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0xf8 0x00    .P.x<d..
    0008   0x40 0xf8 0x00 0x00 0x00                   @....
    decimal
             20   80    0  120   60  100  248    0
             64  248    0    0    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 Base (2008, 0, 0, 24, 0, 1) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x78                                  8x
    decimal
             56  120
    datetime ((2008, 0, 0, 24, 0, 1))
    0000   0x01 0x00 0x38 0x00 0x38                   ..8.8
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-23.data: 3 records`
