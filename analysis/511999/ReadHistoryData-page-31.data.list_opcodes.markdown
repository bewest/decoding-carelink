## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 78, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x30 0x78 0x5c 0x0e 0x60 0xeb 0xc0 0x28    0x\.`..(
    0008   0xf5 0xc0 0x2c 0x1d 0xd0 0x2c 0x77 0xd0    ..,..,w.
    0010   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    0018   0x5a 0xd3 0x52 0x68 0x0d 0x0a 0x77 0x63    Z.Rh..wc
##### DEBUG DECIMAL
             48  120   92   14   96  235  192   40
            245  192   44   29  208   44  119  208
              1    0   48    0   48    0    0    0
             90  211   82  104   13   10  119   99
#### RECORD 0 BolusWizard 2013-07-08T14:27:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-07-08T14:27:24)
    0000   0x58 0xdb 0x0e 0x68 0x0d                   X..h.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x28 0x00 0x00 0x50 0x00 0x28 0x78         (..P.(x
    decimal
             13   80    0  120   60  100   44    0
             40    0    0   80    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 1.0, 'curve': 192},
 {'age': 53, 'amount': 1.1, 'curve': 192},
 {'age': 143, 'amount': 1.1, 'curve': 192},
 {'age': 7, 'amount': 1.6, 'curve': 208},
 {'age': 87, 'amount': 2.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x0d 0xc0 0x2c 0x35 0xc0    \.(..,5.
    0008   0x2c 0x8f 0xc0 0x40 0x07 0xd0 0x60 0x57    ,..@..`W
    0010   0xd0                                       .
    decimal
             92   17   40   13  192   44   53  192
             44  143  192   64    7  208   96   87
            208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus (2008, 4, 0, 16, 0, 32) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x60 0x00                        ..`.
    decimal
              1    0   96    0
    datetime ((2008, 4, 0, 16, 0, 32))
    0000   0x60 0x00 0x50 0x00 0x58                   `.P.X
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 3 Base (2004, 4, 13, 10, 13, 40) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x4e                                  .N
    decimal
            219   78
    datetime ((2004, 4, 13, 10, 13, 40))
    0000   0x68 0x0d 0x0a 0x6d 0x54                   h..mT
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 4 Base (2009, 0, 13, 27, 13, 8) head[2], body[0] op[0xd3]

    op hex (2)
    0000   0xd3 0x32                                  .2
    decimal
            211   50
    datetime ((2009, 0, 13, 27, 13, 8))
    0000   0x08 0x0d 0x5b 0x6d 0x59                   ..[mY
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2000, 4, 16, 12, 13, 40) head[2], body[0] op[0xd3]

    op hex (2)
    0000   0xd3 0x12                                  ..
    decimal
            211   18
    datetime ((2000, 4, 16, 12, 13, 40))
    0000   0x68 0x0d 0x0c 0x50 0x00                   h..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 ChangeTimeDisplay 2000-04-16T00:00:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-16T00:00:36)
    0000   0x64 0x00 0x00 0x30 0x00                   d..0.
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-31.data: 7 records`
