## START logs/ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 63, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x90 0x00 0x00 0x00 0x00 0x90 0x36 0x5c    ......6\
    0008   0x1a 0x68 0x38 0x04 0x20 0x92 0x04 0x1a    .h8. ...
    0010   0x9c 0x05 0x2e 0xa6 0x04 0x94 0x28 0x14    ......(.
    0018   0x74 0x5a 0x14 0x68 0x82 0x14 0x7c 0xdc    tZ.h..|.
##### DEBUG DECIMAL
            144    0    0    0    0  144   54   92
             26  104   56    4   32  146    4   26
            156    5   46  166    4  148   40   20
            116   90   20  104  130   20  124  220
#### RECORD 0 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 0.8, 'curve': 4},
 {'age': 104, 'amount': 0.65, 'curve': 5},
 {'age': 114, 'amount': 1.15, 'curve': 4},
 {'age': 244, 'amount': 3.7, 'curve': 4},
 {'age': 38, 'amount': 2.9, 'curve': 20},
 {'age': 78, 'amount': 2.6, 'curve': 20},
 {'age': 168, 'amount': 3.1, 'curve': 20},
 {'age': 188, 'amount': 2.7, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x20 0x5e 0x04 0x1a 0x68 0x05    \. ^..h.
    0008   0x2e 0x72 0x04 0x94 0xf4 0x04 0x74 0x26    .r....t&
    0010   0x14 0x68 0x4e 0x14 0x7c 0xa8 0x14 0x6c    .hN.|..l
    0018   0xbc 0x14                                  ..
    decimal
             92   26   32   94    4   26  104    5
             46  114    4  148  244    4  116   38
             20  104   78   20  124  168   20  108
            188   20
    datetime (unknown)

    body (0)

#### RECORD 1 Base (2012, 8, 19, 17, 48, 48) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2012, 8, 19, 17, 48, 48))
    0000   0xb0 0x30 0x71 0x13 0x0c                   .0q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Base (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0x68 0x00 0x68                   ..h.h
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Base (2003, 2, 17, 16, 48, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xcc                                  ..
    decimal
              0  204
    datetime ((2003, 2, 17, 16, 48, 0))
    0000   0x00 0xb0 0x30 0x51 0x73                   ..0Qs
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 4 ClearAlarm 2003-02-18T08:07:00 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x5b                                  .[
    decimal
             12   91
    datetime (2003-02-18T08:07:00)
    0000   0x00 0x87 0x28 0x12 0x73                   ..(.s
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 5 ClearAlarm 2006-08-23T14:00:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x28                                  .(
    decimal
             12   40
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-18.data: 6 records`
