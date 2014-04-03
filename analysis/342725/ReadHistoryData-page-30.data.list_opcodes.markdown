## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 78, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x21 0x7d 0x5c 0x0e 0x80 0xf7 0x04 0x30    !}\....0
    0008   0x6f 0x14 0x08 0x79 0x14 0x28 0xbf 0x14    o..y.(..
    0010   0x01 0x21 0x21 0x00 0x5d 0x15 0x57 0x02    .!!.].W.
    0018   0x0d 0x07 0x00 0x00 0x05 0x80 0x42 0x0d    ......B.
##### DEBUG DECIMAL
             33  125   92   14  128  247    4   48
            111   20    8  121   20   40  191   20
              1   33   33    0   93   21   87    2
             13    7    0    0    5  128   66   13
#### RECORD 0 BolusWizard 2013-04-02T19:19:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-04-02T19:19:28)
    0000   0x5c 0x13 0x13 0x02 0x0d                   \....
    body (15)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x07 0x00 0x20 0x7d 0x5c 0x1a         ... }\.
    decimal
             42   80   13   45  106    0   32    0
              0    7    0   32  125   92   26

#### RECORD 1 Base (2008, 0, 4, 7, 8, 4) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x7d                                  0}
    decimal
             48  125
    datetime ((2008, 0, 4, 7, 8, 4))
    0000   0x04 0x08 0x87 0x04 0x28                   ....(
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2009, 3, 0, 4, 63, 40) head[2], body[0] op[0xcd]

    op hex (2)
    0000   0xcd 0x04                                  ..
    decimal
            205    4
    datetime ((2009, 3, 0, 4, 63, 40))
    0000   0x28 0xff 0x04 0x80 0x09                   (....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 3 SelectBasalProfile (2004, 0, 29, 6, 20, 19) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x06                                  ..
    decimal
             20    6
    datetime ((2004, 0, 29, 6, 20, 19))
    0000   0x13 0x14 0x06 0x1d 0x14                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 4 Base (2000, 0, 0, 0, 1, 20) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x4f                                  .O
    decimal
            144   79
    datetime ((2000, 0, 0, 0, 1, 20))
    0000   0x14 0x01 0x20 0x20 0x00                   ..  .
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[19], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 2.075, 'curve': 13},
 {'age': 20, 'amount': 0.25, 'curve': 91},
 {'age': 55, 'amount': 0.525, 'curve': 2},
 {'age': 91, 'amount': 3.525, 'curve': 20},
 {'age': 21, 'amount': 2.325, 'curve': 23}]
```
    op hex (19)
    0000   0x5c 0x13 0x53 0x02 0x0d 0x0a 0x14 0x5b    \.S....[
    0008   0x15 0x37 0x02 0x8d 0x5b 0x14 0x5d 0x15    .7..[.].
    0010   0x17 0x02 0x0d                             ...
    decimal
             92   19   83    2   13   10   20   91
             21   55    2  141   91   20   93   21
             23    2   13
    datetime (unknown)

    body (0)

#### RECORD 6 Base (2000, 0, 1, 10, 45, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x51                                  .Q
    decimal
              0   81
    datetime ((2000, 0, 1, 10, 45, 13))
    0000   0x0d 0x2d 0x6a 0x21 0x00                   .-j!.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-30.data: 7 records`
