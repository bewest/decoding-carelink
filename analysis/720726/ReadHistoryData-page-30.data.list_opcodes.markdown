## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 56, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x97 0x20 0x48 0x61 0x0d 0x7b 0x02 0x80    . Ha.{..
    0008   0x1e 0x09 0x01 0x0d 0x13 0x1e 0x00 0x0a    ........
    0010   0x4c 0xb2 0x07 0x2b 0x61 0x0d 0x3f 0x09    L..+a.?.
    0018   0xb2 0x07 0x8b 0x61 0x0d 0x69 0x69 0x96    ...a.ii.
##### DEBUG DECIMAL
            151   32   72   97   13  123    2  128
             30    9    1   13   19   30    0   10
             76  178    7   43   97   13   63    9
            178    7  139   97   13  105  105  150
#### RECORD 0 CalBGForPH 2013-08-01T08:32:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-01T08:32:07)
    0000   0x87 0x20 0x28 0x61 0x0d                   . (a.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Ian3F 2013-08-01T08:32:07 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2013-08-01T08:32:07)
    0000   0x87 0x20 0x88 0x61 0x0d                   . .a.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-08-01T08:32:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2013-08-01T08:32:23)
    0000   0x97 0x20 0x08 0x61 0x0d                   . .a.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 Ian69 2013-08-01T08:32:23 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-01T08:32:23)
    0000   0x97 0x20 0x08 0x01 0x0d                   . ...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x54 0x00 0x54 0x00    ....T.T.
    decimal
             10   30    1    0   84    0   84    0
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-30.data: 4 records`
