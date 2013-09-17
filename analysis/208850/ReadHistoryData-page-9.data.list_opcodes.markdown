## START logs/ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 260, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0a 0x9e 0x1c 0x35 0x01 0x0c 0x03 0x00    ...5....
    0008   0x03 0x00 0x03 0xa7 0x1c 0x15 0x01 0x0c    ........
    0010   0x26 0x01 0x8d 0x19 0x16 0x01 0x0c 0x27    &......'
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x28 0x00    ......(.
##### DEBUG DECIMAL
             10  158   28   53    1   12    3    0
              3    0    3  167   28   21    1   12
             38    1  141   25   22    1   12   39
              0    0    0    0    0    0   40    0
#### RECORD 0 Prime 2012-08-01T21:28:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0a                   .....
    decimal
              3    0    0    0   10
    datetime (2012-08-01T21:28:30)
    0000   0x9e 0x1c 0x35 0x01 0x0c                   ..5..
    body (0)

#### RECORD 1 Prime 2012-08-01T21:28:39 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2012-08-01T21:28:39)
    0000   0xa7 0x1c 0x15 0x01 0x0c                   .....
    body (0)

#### RECORD 2 EnableDisableRemote 2012-08-01T22:25:13 head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x01                                  &.
    decimal
             38    1
    datetime (2012-08-01T22:25:13)
    0000   0x8d 0x19 0x16 0x01 0x0c                   .....
    body (14)
    hex
    0000   0x27 0x00 0x00 0x00 0x00 0x00 0x00 0x28    '......(
    0008   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
             39    0    0    0    0    0    0   40
              0    0    0    0    0    0

#### RECORD 3 EnableDisableRemote 2012-08-01T22:25:34 head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x01                                  &.
    decimal
             38    1
    datetime (2012-08-01T22:25:34)
    0000   0xa2 0x19 0x16 0x01 0x0c                   .....
    body (14)
    hex
    0000   0x27 0x01 0xe2 0x40 0x00 0x00 0x00 0x28    '..@...(
    0008   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
             39    1  226   64    0    0    0   40
              0    0    0    0    0    0

#### RECORD 4 EnableDisableRemote 2012-08-01T22:31:47 head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x01                                  &.
    decimal
             38    1
    datetime (2012-08-01T22:31:47)
    0000   0xaf 0x1f 0x16 0x01 0x0c                   .....
    body (14)
    hex
    0000   0x27 0x01 0xe2 0x40 0x03 0x42 0x2a 0x28    '..@.B*(
    0008   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
             39    1  226   64    3   66   42   40
              0    0    0    0    0    0

#### RECORD 5 EnableDisableRemote 2012-08-01T22:32:32 head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x01                                  &.
    decimal
             38    1
    datetime (2012-08-01T22:32:32)
    0000   0xa0 0x20 0x16 0x01 0x0c                   . ...
    body (14)
    hex
    0000   0x27 0x01 0xe2 0x40 0x03 0x42 0x2a 0x28    '..@.B*(
    0008   0x0c 0x89 0x92 0x00 0x00 0x00              ......
    decimal
             39    1  226   64    3   66   42   40
             12  137  146    0    0    0
    HOUR BITS: [0, 0, 1]
#### RECORD 6 TempBasal 2012-08-01T22:38:22 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.2}
```
    op hex (2)
    0000   0x33 0x30                                  30
    decimal
             51   48
    datetime (2012-08-01T22:38:22)
    0000   0x96 0x26 0x16 0x01 0x0c                   .&...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 7 TempBasalDuration 2012-08-01T22:38:22 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2012-08-01T22:38:22)
    0000   0x96 0x26 0x16 0x01 0x0c                   .&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 TempBasal 2012-08-01T22:48:39 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.2}
```
    op hex (2)
    0000   0x33 0x30                                  30
    decimal
             51   48
    datetime (2012-08-01T22:48:39)
    0000   0xa7 0x30 0x16 0x01 0x0c                   .0...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 9 TempBasalDuration 2012-08-01T22:48:39 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2012-08-01T22:48:39)
    0000   0xa7 0x30 0x16 0x01 0x0c                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 TempBasal 2012-08-01T22:51:32 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2012-08-01T22:51:32)
    0000   0xa0 0x33 0x16 0x01 0x0c                   .3...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 11 TempBasalDuration 2012-08-01T22:51:32 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2012-08-01T22:51:32)
    0000   0xa0 0x33 0x16 0x01 0x0c                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 12 TempBasal 2012-08-01T22:52:17 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.9}
```
    op hex (2)
    0000   0x33 0x4c                                  3L
    decimal
             51   76
    datetime (2012-08-01T22:52:17)
    0000   0x91 0x34 0x16 0x01 0x0c                   .4...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 13 TempBasalDuration 2012-08-01T22:52:17 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 180}
```
    op hex (2)
    0000   0x16 0x06                                  ..
    decimal
             22    6
    datetime (2012-08-01T22:52:17)
    0000   0x91 0x34 0x16 0x01 0x0c                   .4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 TempBasal 2012-08-01T23:04:54 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.9}
```
    op hex (2)
    0000   0x33 0x4c                                  3L
    decimal
             51   76
    datetime (2012-08-01T23:04:54)
    0000   0xb6 0x04 0x17 0x01 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 15 TempBasalDuration 2012-08-01T23:04:54 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 180}
```
    op hex (2)
    0000   0x16 0x06                                  ..
    decimal
             22    6
    datetime (2012-08-01T23:04:54)
    0000   0xb6 0x04 0x17 0x01 0x0c                   .....
    body (0)

#### RECORD 16 ChangeUtility 2012-08-01T23:35:20 head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x04                                  c.
    decimal
             99    4
    datetime (2012-08-01T23:35:20)
    0000   0x94 0x23 0x17 0x01 0x0c                   .#...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 ChangeUtility 2012-08-01T23:38:57 head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x03                                  c.
    decimal
             99    3
    datetime (2012-08-01T23:38:57)
    0000   0xb9 0x26 0x17 0x01 0x0c                   .&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 ResultTotals 2012-08-01T12:12:01 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x80                   .....
    decimal
              7    0    0    0  128
    datetime (2012-08-01T12:12:01)
    0000   0x81 0x0c 0x6c 0x81 0x0c                   ..l..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x80 0x00 0x80 0x64 0x00 0x00 0x00    ....d...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x5b 0x64 0xa9 0x34 0x06    ...[d.4.
    0028   0x02                                       .
    decimal
              5   12    0  232    0    0    0    0
              0  128    0  128  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   91  100  169   52    6
              2
    DAY BITS: [1, 0, 0]
#### RECORD 19 ClearAlarm 2000-04-04T18:10:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x0a                                  ..
    decimal
             12   10
    datetime (2000-04-04T18:10:16)
    0000   0x50 0x0a 0x32 0x64 0x00                   P.2d.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH (2000, 0, 3, 0, 0, 0) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 0}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime ((2000, 0, 3, 0, 0, 0))
    0000   0x00 0x00 0x00 0x03 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-9.data: 21 records`
