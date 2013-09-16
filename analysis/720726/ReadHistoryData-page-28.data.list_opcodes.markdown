## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 49, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xba 0x23 0x48 0x64 0x0d 0x7b 0x02 0x80    .#Hd.{..
    0008   0x1e 0x09 0x04 0x0d 0x13 0x1e 0x00 0x0a    ........
    0010   0x3c 0x92 0x22 0x29 0x64 0x0d 0x3f 0x07    <.")d.?.
    0018   0x92 0x22 0x89 0x64 0x0d 0x69 0x69 0x96    .".d.ii.
##### DEBUG DECIMAL
            186   35   72  100   13  123    2  128
             30    9    4   13   19   30    0   10
             60  146   34   41  100   13   63    7
            146   34  137  100   13  105  105  150
#### RECORD 0 Ian3F 2013-08-04T08:35:50 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2013-08-04T08:35:50)
    0000   0xb2 0x23 0x08 0x64 0x0d                   .#.d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-08-04T08:35:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 142,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 15.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-08-04T08:35:58)
    0000   0xba 0x23 0x08 0x64 0x0d                   .#.d.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x98 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x98 0x36         ......6
    decimal
              0  144    0  110   23   54  152    0
              0    0    0    0    0  152   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian69 2013-08-04T08:35:58 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-04T08:35:58)
    0000   0xba 0x23 0x08 0x04 0x0d                   .#...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x98 0x00 0x98 0x00    ........
    decimal
             10   30    1    0  152    0  152    0
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-28.data: 3 records`
