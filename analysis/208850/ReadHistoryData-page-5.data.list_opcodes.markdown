## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 127, found 16 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x07 0x00 0x00 0x03 0x36 0xad 0x86 0x6c    ....6..l
    0008   0xad 0x86 0x05 0x0c 0x00 0xe8 0x00 0x00    ........
    0010   0x00 0x00 0x03 0x36 0x03 0x36 0x64 0x00    ...6.6d.
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              7    0    0    3   54  173  134  108
            173  134    5   12    0  232    0    0
              0    0    3   54    3   54  100    0
              0    0    0    0    0    0    0    0
#### RECORD 0 LowReservoir 2006-11-12T07:48:20 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.0}
```
    op hex (2)
    0000   0x34 0x00                                  4.
    decimal
             52    0
    datetime (2006-11-12T07:48:20)
    0000   0x94 0xf0 0x07 0x0c 0x06                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 Rewind 2006-11-12T07:48:27 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2006-11-12T07:48:27)
    0000   0x9b 0xf0 0x07 0x0c 0x06                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 Prime 2006-11-12T14:30:26 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0e                   .....
    decimal
              3    0    0    0   14
    datetime (2006-11-12T14:30:26)
    0000   0x9a 0xde 0x2e 0x0c 0x06                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Prime 2006-11-12T14:30:36 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2006-11-12T14:30:36)
    0000   0xa4 0xde 0x0e 0x0c 0x06                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 ResultTotals 2006-10-12T12:06:44 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x01 0xae                   .....
    decimal
              7    0    0    1  174
    datetime (2006-10-12T12:06:44)
    0000   0xac 0x86 0x6c 0xac 0x86                   ..l..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x01 0xae 0x01 0xae 0x64 0x00 0x00 0x00    ....d...
    0010   0x00 0x00 0x00 0x00 0x34 0x00 0x94 0xf0    ....4...
    0018   0x07 0x0c 0x06 0x21 0x00 0x9b 0xf0 0x07    ...!....
    0020   0x0c 0x06 0x03 0x00 0x00 0x00 0x0e 0x9a    ........
    0028   0xde                                       .
    decimal
              5   12    0  232    0    0    0    0
              1  174    1  174  100    0    0    0
              0    0    0    0   52    0  148  240
              7   12    6   33    0  155  240    7
             12    6    3    0    0    0   14  154
            222
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 Base (2000, 0, 3, 0, 3, 6) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x0c                                  ..
    decimal
             46   12
    datetime ((2000, 0, 3, 0, 3, 6))
    0000   0x06 0x03 0x00 0x03 0x00                   .....
    body (0)

#### RECORD 6 Prime (2001, 0, 0, 0, 7, 6) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.2, 'fixed': 22.2, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0xa4 0xde 0x0e 0x0c                   .....
    decimal
              3  164  222   14   12
    datetime ((2001, 0, 0, 0, 7, 6))
    0000   0x06 0x07 0x00 0x00 0x01                   .....
    body (0)

#### RECORD 7 Base (2005, 9, 6, 12, 44, 6) head[2], body[0] op[0xae]

    op hex (2)
    0000   0xae 0xac                                  ..
    decimal
            174  172
    datetime ((2005, 9, 6, 12, 44, 6))
    0000   0x86 0x6c 0xac 0x86 0x05                   .l...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 8 ClearAlarm (2000, 12, 0, 0, 0, 40) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x00                                  ..
    decimal
             12    0
    datetime ((2000, 12, 0, 0, 0, 40))
    0000   0xe8 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 9 Bolus (2000, 4, 0, 0, 0, 36) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 17.4, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0xae 0x01 0xae                        ....
    decimal
              1  174    1  174
    datetime ((2000, 4, 0, 0, 0, 36))
    0000   0x64 0x00 0x00 0x00 0x00                   d....
    body (0)

`end logs/ReadHistoryData-page-5.data: 10 records`
