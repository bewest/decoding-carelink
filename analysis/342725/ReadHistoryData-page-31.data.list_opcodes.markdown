## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 83, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x01 0x00 0x00 0x01 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x34 0x64 0x03 0xe9 0x06    ...4d...
    0010   0x1f 0x0d 0x0a 0x06 0x37 0xf2 0x27 0x1f    ....7.'.
    0018   0x8d 0x5b 0x06 0x04 0xf3 0x07 0x1f 0x0d    .[......
##### DEBUG DECIMAL
              1    0    0    1    0   12    0  232
              0    0    0   52  100    3  233    6
             31   13   10    6   55  242   39   31
            141   91    6    4  243    7   31   13
#### RECORD 0 BolusWizard 2013-03-30T22:31:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-03-30T22:31:44)
    0000   0x2c 0xdf 0x16 0x1e 0x0d                   ,....
    body (15)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x0f 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x2f 0x7d 0x34 0xc8         .../}4.
    decimal
             42   80   13   45  106   15   32    0
              0    0    0   47  125   52  200
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Base (2015, 0, 1, 13, 30, 22) head[2], body[0] op[0x29]

    op hex (2)
    0000   0x29 0xe0                                  ).
    decimal
             41  224
    datetime ((2015, 0, 1, 13, 30, 22))
    0000   0x16 0x1e 0x0d 0x01 0x2f                   ..../
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2013, 3, 30, 22, 31, 44) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0x00                                  /.
    decimal
             47    0
    datetime ((2013, 3, 30, 22, 31, 44))
    0000   0x2c 0xdf 0x56 0x1e 0x0d                   ,.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-30T23:59:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-03-30T23:59:41)
    0000   0x29 0xfb 0x37 0x1e 0x0d                   ).7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 MResultTotals 2013-03-31T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x32                   ....2
    decimal
              7    0    0    4   50
    datetime (2013-03-31T00:00:00)
    0000   0x3e 0x8d                                  >.
    body (3)
    hex
    0000   0x6d 0x3e 0x8d                             m>.
    decimal
            109   62  141
    HOUR BITS: [1, 0, 0]
#### RECORD 5 Base (2000, 9, 2, 1, 45, 23) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 9, 2, 1, 45, 23))
    0000   0x97 0x6d 0xc1 0x02 0x00                   .m...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 Base (2000, 0, 18, 22, 3, 50) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2000, 0, 18, 22, 3, 50))
    0000   0x32 0x03 0x76 0x52 0x00                   2.vR.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2002, 0, 28, 0, 42, 0) head[2], body[0] op[0xbc]

    op hex (2)
    0000   0xbc 0x12                                  ..
    decimal
            188   18
    datetime ((2002, 0, 28, 0, 42, 0))
    0000   0x00 0x2a 0x00 0xbc 0x12                   .*...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2000, 4, 0, 28, 0, 4) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x80                                  ..
    decimal
              0  128
    datetime ((2000, 4, 0, 28, 0, 4))
    0000   0x44 0x00 0x3c 0x20 0x00                   D.< .
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-31.data: 9 records`
