## START logs/ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 202, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x44 0x00 0x00 0x00 0x00 0x44 0x36 0x5c    D....D6\
    0008   0x14 0x7c 0x6e 0x04 0x90 0xc8 0x04 0x68    .|n....h
    0010   0xfa 0x04 0x20 0x54 0x14 0x1a 0x5e 0x15    .. T..^.
    0018   0x2e 0x68 0x14 0x01 0x00 0x44 0x00 0x44    .h...D.D
##### DEBUG DECIMAL
             68    0    0    0    0   68   54   92
             20  124  110    4  144  200    4  104
            250    4   32   84   20   26   94   21
             46  104   20    1    0   68    0   68
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

#### RECORD 1 Ian69 2012-08-19T17:48:48 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-19T17:48:48)
    0000   0xb0 0x30 0x71 0x13 0x0c                   .0q..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0x68 0x00 0x68 0x00    ....h.h.
    decimal
             21   30    1    0  104    0  104    0
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Base (2012, 8, 19, 17, 48, 48) head[2], body[0] op[0xcc]

    op hex (2)
    0000   0xcc 0x00                                  ..
    decimal
            204    0
    datetime ((2012, 8, 19, 17, 48, 48))
    0000   0xb0 0x30 0x51 0x73 0x0c                   .0Qs.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2012-08-19T18:40:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-19T18:40:07)
    0000   0x87 0x28 0x12 0x73 0x0c                   .(.s.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 2.6, 'curve': 4},
 {'age': 146, 'amount': 0.8, 'curve': 4},
 {'age': 156, 'amount': 0.65, 'curve': 5},
 {'age': 166, 'amount': 1.15, 'curve': 4},
 {'age': 40, 'amount': 3.7, 'curve': 20},
 {'age': 90, 'amount': 2.9, 'curve': 20},
 {'age': 130, 'amount': 2.6, 'curve': 20},
 {'age': 220, 'amount': 3.1, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x68 0x38 0x04 0x20 0x92 0x04    \.h8. ..
    0008   0x1a 0x9c 0x05 0x2e 0xa6 0x04 0x94 0x28    .......(
    0010   0x14 0x74 0x5a 0x14 0x68 0x82 0x14 0x7c    .tZ.h..|
    0018   0xdc 0x14                                  ..
    decimal
             92   26  104   56    4   32  146    4
             26  156    5   46  166    4  148   40
             20  116   90   20  104  130   20  124
            220   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-08-19T18:40:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xb8 0x00    ........
    decimal
              1    0  144    0  144    0  184    0
    datetime (2012-08-19T18:40:07)
    0000   0x87 0x28 0x52 0x73 0x0c                   .(Rs.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2012-08-19T20:07:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-19T20:07:02)
    0000   0x82 0x07 0x14 0x73 0x0c                   ...s.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 3.6, 'curve': 4},
 {'age': 143, 'amount': 2.6, 'curve': 4},
 {'age': 233, 'amount': 0.8, 'curve': 4},
 {'age': 243, 'amount': 0.65, 'curve': 5},
 {'age': 253, 'amount': 1.15, 'curve': 4},
 {'age': 127, 'amount': 3.7, 'curve': 20},
 {'age': 177, 'amount': 2.9, 'curve': 20},
 {'age': 217, 'amount': 2.6, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x90 0x5d 0x04 0x68 0x8f 0x04    \..].h..
    0008   0x20 0xe9 0x04 0x1a 0xf3 0x05 0x2e 0xfd     .......
    0010   0x04 0x94 0x7f 0x14 0x74 0xb1 0x14 0x68    ....t..h
    0018   0xd9 0x14                                  ..
    decimal
             92   26  144   93    4  104  143    4
             32  233    4   26  243    5   46  253
              4  148  127   20  116  177   20  104
            217   20
    datetime (unknown)

    body (0)

#### RECORD 8 CalBGForPH 2012-08-19T20:08:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2012-08-19T20:08:36)
    0000   0xa4 0x08 0x34 0x73 0x0c                   ..4s.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 Base (2012, 8, 19, 20, 8, 36) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime ((2012, 8, 19, 20, 8, 36))
    0000   0xa4 0x08 0xd4 0x73 0x0c                   ...s.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 10 Ian69 2000-08-28T00:01:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2000-08-28T00:01:22)
    0000   0x96 0x01 0x00 0x7c 0x00                   ...|.
    body (8)
    hex
    0000   0x7c 0x00 0x80 0x00 0x83 0x07 0x54 0x73    |.....Ts
    decimal
            124    0  128    0  131    7   84  115
    DAY BITS: [0, 1, 1]
#### RECORD 11 ClearAlarm 2003-02-21T22:57:00 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x5b                                  .[
    decimal
             12   91
    datetime (2003-02-21T22:57:00)
    0000   0x00 0xb9 0x36 0x15 0x73                   ..6.s
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 12 ClearAlarm 2006-08-23T14:00:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x13                                  ..
    decimal
             12   19
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-18.data: 13 records`
