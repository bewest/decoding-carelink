## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 64, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0x36 0x5c 0x0e 0x84 0x41 0x04 0xe4    l6\..A..
    0008   0x9b 0x04 0x1c 0xa5 0x04 0x64 0x8b 0x14    .....d..
    0010   0x01 0x00 0x6c 0x00 0x6c 0x00 0xb0 0x00    ..l.l...
    0018   0x93 0x32 0x54 0x65 0x0d 0x0a 0x89 0xa6    .2Te....
##### DEBUG DECIMAL
            108   54   92   14  132   65    4  228
            155    4   28  165    4  100  139   20
              1    0  108    0  108    0  176    0
            147   50   84  101   13   10  137  166
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 5.7, 'curve': 4},
 {'age': 107, 'amount': 0.7, 'curve': 4},
 {'age': 81, 'amount': 2.5, 'curve': 20},
 {'age': 181, 'amount': 3.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xe4 0x61 0x04 0x1c 0x6b 0x04    \..a..k.
    0008   0x64 0x51 0x14 0x9c 0xb5 0x14              dQ....
    decimal
             92   14  228   97    4   28  107    4
            100   81   20  156  181   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-08-05T19:52:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x9c 0x00    ........
    decimal
              1    0  132    0  132    0  156    0
    datetime (2013-08-05T19:52:24)
    0000   0x98 0x34 0x53 0x65 0x0d                   .4Se.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-08-05T20:09:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-08-05T20:09:49)
    0000   0xb1 0x09 0x34 0x65 0x0d                   ..4e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 3 Base (2013, 8, 5, 20, 9, 49) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime ((2013, 8, 5, 20, 9, 49))
    0000   0xb1 0x09 0x14 0x65 0x0d                   ...e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 4 Base (2002, 9, 19, 0, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2002, 9, 19, 0, 27, 22))
    0000   0x96 0x5b 0x00 0x93 0x32                   .[..2
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 5 SelectBasalProfile (2014, 0, 0, 16, 30, 13) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x65                                  .e
    decimal
             20  101
    datetime ((2014, 0, 0, 16, 30, 13))
    0000   0x0d 0x1e 0x90 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 ChangeTime (2000, 0, 0, 12, 0, 0) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x36                                  .6
    decimal
             23   54
    datetime ((2000, 0, 0, 12, 0, 0))
    0000   0x00 0x00 0x6c 0x00 0x00                   ..l..
    body (0)

`end logs/ReadHistoryData-page-27.data: 7 records`
