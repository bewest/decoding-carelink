### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-8.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-8.data
#### RECORD 0 hack1 2012-12-25T01:33:45 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xd8 0x0c 0x05 0x00 0x5e 0x3d 0xa3    m....^=.
    0008   0x06 0x00 0x00 0x05 0x82 0x03 0x7a 0x3f    ......z?
    0010   0x02 0x08 0x25 0x00 0xaa 0x02 0x08 0x25    ..%....%
    0018   0x01 0xf0 0x5f 0x00 0x18 0x05 0x00 0x00    .._.....
    0020   0x00 0x04 0x03 0x00 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x34 0xc8              ....4.
    decimal
            109  216   12    5    0   94   61  163
              6    0    0    5  130    3  122   63
              2    8   37    0  170    2    8   37
              1  240   95    0   24    5    0    0
              0    4    3    0    1    0   12    0
            232    0    0    0   52  200
    datetime (2012-12-25T01:33:45)
    0000   0xed 0x21 0x01 0x19 0x0c                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Rewind 2012-12-25T09:30:48 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-25T09:30:48)
    0000   0xf0 0x1e 0x09 0x19 0x0c                   .....
    body (0)

#### RECORD 2 Prime 2012-12-25T09:31:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2012-12-25T09:31:18)
--
             92   17   80   86    4   84  176    4
             80  206    4  104   30   20  140  180
             20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-12-25T22:20:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-25T22:20:36)
    0000   0xe4 0x14 0x56 0x19 0x0c                   ..V..
    body (0)

#### RECORD 38 ResultTotals 2012-12-25T13:12:25 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x6c                   ....l
    decimal
              7    0    0    6  108
    datetime (2012-12-25T13:12:25)
    0000   0xd9 0x0c 0x6d 0xd9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa5 0x46 0x32 0x0a 0x00 0x00    ...F2...
    0008   0x06 0x6c 0x03 0x80 0x37 0x02 0xec 0x2d    .l..7..-
    0010   0x00 0xd0 0x02 0xec 0x2d 0x02 0x34 0x4b    ....-.4K
    0018   0x00 0xb8 0x19 0x00 0x00 0x00 0x07 0x05    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  165   70   50   10    0    0
              6  108    3  128   55    2  236   45
              0  208    2  236   45    2   52   75
              0  184   25    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 39 CalBGForPH 2012-12-26T00:55:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 224}
```
    op hex (2)
    0000   0x0a 0xe0                                  ..
    decimal
             10  224
    datetime (2012-12-26T00:55:44)
    0000   0xec 0x37 0x20 0x1a 0x0c                   .7 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 BolusWizard 2012-12-26T00:55:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
--
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-12-26T19:39:17)
    0000   0xd1 0x27 0x53 0x1a 0x0c                   .'S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 CalBGForPH 2012-12-26T20:57:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-12-26T20:57:27)
    0000   0xdb 0x39 0x34 0x1a 0x0c                   .94..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 ResultTotals 2012-12-26T13:12:26 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x18                   .....
    decimal
              7    0    0    6   24
    datetime (2012-12-26T13:12:26)
    0000   0xda 0x0c 0x6d 0xda 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7e 0x59 0xe0 0x06 0x00 0x00    ..~Y....
    0008   0x06 0x18 0x03 0x68 0x38 0x02 0xb0 0x2c    ...h8..,
    0010   0x00 0xcf 0x02 0xb0 0x2c 0x02 0x60 0x58    ....,.`X
    0018   0x00 0x50 0x0c 0x00 0x00 0x00 0x04 0x02    .P......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  126   89  224    6    0    0
              6   24    3  104   56    2  176   44
              0  207    2  176   44    2   96   88
              0   80   12    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2012-12-27T00:30:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2012-12-27T00:30:38)
    0000   0xe6 0x1e 0x20 0x1b 0x0c                   .. ..
    body (0)

#### RECORD 60 BolusWizard 2012-12-27T00:30:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
--
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-12-27T20:06:35)
    0000   0xe3 0x06 0x54 0x1b 0x0c                   ..T..
    body (0)

#### RECORD 77 CalBGForPH 2012-12-27T22:23:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2012-12-27T22:23:38)
    0000   0xe6 0x17 0x36 0x1b 0x0c                   ..6..
    body (0)

#### RECORD 78 ResultTotals 2012-12-27T13:12:27 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-12-27T13:12:27)
    0000   0xdb 0x0c 0x6d 0xdb 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x78 0x48 0xbc 0x06 0x00 0x00    ..xH....
    0008   0x05 0x0c 0x03 0x7c 0x45 0x01 0x90 0x1f    ...|E...
    0010   0x00 0x7a 0x01 0x90 0x1f 0x01 0x54 0x55    .z....TU
    0018   0x00 0x3c 0x0f 0x00 0x00 0x00 0x04 0x02    .<......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  120   72  188    6    0    0
              5   12    3  124   69    1  144   31
              0  122    1  144   31    1   84   85
              0   60   15    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 79 LowBattery 2012-12-28T01:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-12-28T01:01:00)
    0000   0xc0 0x01 0x01 0x1c 0x0c                   .....
    body (0)

#### RECORD 80 Battery 2012-12-28T07:36:44 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2012-12-28T07:36:44)
--
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2012-12-28T07:47:54)
    0000   0xf6 0x2f 0x27 0x1c 0x0c                   ./'..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 83 Base unknown head[2], body[0] op[0x9d]

    op hex (2)
    0000   0x9d 0x8a                                  ..
    decimal
            157  138
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-8.data: 84 records`
