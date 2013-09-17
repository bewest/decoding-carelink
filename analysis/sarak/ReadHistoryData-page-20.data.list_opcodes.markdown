## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 185, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x61 0x24 0x00 0x00 0x00 0x00 0x00 0x00    a$......
    0008   0x00 0x00 0x34 0xc8 0x67 0xf1 0x00 0x18    ..4.g...
    0010   0x0d 0x7b 0x01 0x40 0xc0 0x04 0x18 0x0d    .{.@....
    0018   0x08 0x21 0x00 0x7b 0x02 0x40 0xc0 0x08    .!.{.@..
##### DEBUG DECIMAL
             97   36    0    0    0    0    0    0
              0    0   52  200  103  241    0   24
             13  123    1   64  192    4   24   13
              8   33    0  123    2   64  192    8
#### RECORD 0 BolusWizard 2013-07-23T20:06:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-07-23T20:06:36)
    0000   0x64 0xc6 0x14 0x77 0x0d                   d..w.
    body (13)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x10 0x00                   P....
    decimal
             20   80    0  100   60  100    0    0
             80    0    0   16    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2000, 4, 27, 20, 20, 28) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x78                                  Px
    decimal
             80  120
    datetime ((2000, 4, 27, 20, 20, 28))
    0000   0x5c 0x14 0x34 0x7b 0xc0                   \.4{.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 Base (2014, 12, 0, 11, 38, 0) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x8f                                  ..
    decimal
             28  143
    datetime ((2014, 12, 0, 11, 38, 0))
    0000   0xc0 0x26 0xcb 0xc0 0x0e                   .&...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0]
#### RECORD 3 Base (2009, 4, 4, 16, 37, 4) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0xc0                                  ..
    decimal
            213  192
    datetime ((2009, 4, 4, 16, 37, 4))
    0000   0x44 0x25 0xd0 0x44 0x89                   D%.D.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 Base (2000, 1, 16, 0, 16, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 1, 16, 0, 16, 0))
    0000   0x00 0x50 0x00 0x50 0x00                   .P.P.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 5 Base (2013, 7, 23, 20, 6, 36) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2013, 7, 23, 20, 6, 36))
    0000   0x64 0xc6 0x54 0x77 0x0d                   d.Tw.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-07-23T20:37:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2013-07-23T20:37:46)
    0000   0x6e 0xe5 0x34 0x17 0x0d                   n.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 CalBGForPH 2013-07-23T21:41:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 292}
```
    op hex (2)
    0000   0x0a 0x24                                  .$
    decimal
             10   36
    datetime (2013-07-23T21:41:53)
    0000   0x75 0xe9 0x35 0x17 0x8d                   u.5..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2013-07-23T21:41:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 292,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x24                                  [$
    decimal
             91   36
    datetime (2013-07-23T21:41:56)
    0000   0x78 0xe9 0x15 0x17 0x0d                   x....
    body (13)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x70 0x00    .Q.d<dp.
    0008   0x00 0x00 0x00 0x20 0x00                   ... .
    decimal
              0   81    0  100   60  100  112    0
              0    0    0   32    0
    HOUR BITS: [1, 1, 1]
#### RECORD 9 Base (2000, 4, 2, 16, 20, 28) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x78                                  Px
    decimal
             80  120
    datetime ((2000, 4, 2, 16, 20, 28))
    0000   0x5c 0x14 0x50 0x62 0xc0                   \.Pb.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 10 LowReservoir (2006, 12, 0, 14, 28, 0) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 21.8}
```
    op hex (2)
    0000   0x34 0xda                                  4.
    decimal
             52  218
    datetime ((2006, 12, 0, 14, 28, 0))
    0000   0xc0 0x1c 0xee 0xc0 0x26                   ....&
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 11 Base (2004, 0, 4, 16, 52, 14) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0xd0                                  *.
    decimal
             42  208
    datetime ((2004, 0, 4, 16, 52, 14))
    0000   0x0e 0x34 0xd0 0x44 0x84                   .4.D.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Base (2000, 1, 16, 0, 16, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 1, 16, 0, 16, 0))
    0000   0x00 0x50 0x00 0x50 0x00                   .P.P.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 13 Base (2013, 7, 23, 21, 41, 56) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2013, 7, 23, 21, 41, 56))
    0000   0x78 0xe9 0x55 0x17 0x0d                   x.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 Base (2013, 7, 24, 0, 0, 0) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime ((2013, 7, 24, 0, 0, 0))
    0000   0x40 0xc0 0x00 0x18 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 Base (2005, 0, 0, 0, 7, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1d                                  ..
    decimal
              0   29
    datetime ((2005, 0, 0, 0, 7, 0))
    0000   0x00 0x07 0x00 0x00 0x05                   .....
    body (0)

#### RECORD 16 Base (2014, 8, 0, 0, 0, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x77                                  .w
    decimal
              0  119
    datetime ((2014, 8, 0, 0, 0, 13))
    0000   0x8d 0x00 0x00 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 17 Base (2000, 0, 0, 13, 0, 5) head[2], body[0] op[0x77]

    op hex (2)
    0000   0x77 0x8d                                  w.
    decimal
            119  141
    datetime ((2000, 0, 0, 13, 0, 5))
    0000   0x05 0x00 0xcd 0x00 0x00                   .....
    body (0)

#### RECORD 18 CalBGForPH (2012, 0, 2, 0, 5, 0) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime ((2012, 0, 2, 0, 5, 0))
    0000   0x00 0x05 0x00 0x02 0xdc                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 19 Base (2000, 0, 4, 0, 43, 36) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0x02                                  9.
    decimal
             57    2
    datetime ((2000, 0, 4, 0, 43, 36))
    0000   0x24 0x2b 0x00 0x44 0x00                   $+.D.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 20 Base (2000, 0, 0, 4, 0, 16) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 0, 0, 4, 0, 16))
    0000   0x10 0x00 0x44 0x00 0x00                   ..D..
    body (0)

#### RECORD 21 Prime (2000, 0, 0, 0, 0, 0) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.1, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x05 0x01 0x00 0x04                   .....
    decimal
              3    5    1    0    4
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-20.data: 22 records`
