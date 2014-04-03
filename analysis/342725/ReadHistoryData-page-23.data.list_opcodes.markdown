## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 522, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0e 0x7d 0x5c 0x08 0x3a 0xd3 0x14 0x16    .}\.:...
    0008   0xdd 0x14 0x01 0x0d 0x0d 0x00 0x73 0x15    ......s.
    0010   0x56 0x1b 0x0d 0x0a 0xb9 0x75 0x25 0x36    V....u%6
    0018   0x1b 0x0d 0x0a 0xb9 0x74 0x28 0x36 0x1b    ....t(6.
##### DEBUG DECIMAL
             14  125   92    8   58  211   20   22
            221   20    1   13   13    0  115   21
             86   27   13   10  185  117   37   54
             27   13   10  185  116   40   54   27
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 4.8, 'curve': 20},
 {'age': 204, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x22 0x14 0x30 0xcc 0x14    \..".0..
    decimal
             92    8  192   34   20   48  204   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2015, 0, 8, 31, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x05 0x05 0x00 0x57 0x18 0x4d 0x1a    ....W.M.
    decimal
              1    5    5    0   87   24   77   26
    datetime ((2015, 0, 8, 31, 10, 13))
    0000   0x0d 0x0a 0x5f 0x48 0x2f                   .._H/
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2015, 1, 27, 31, 27, 13) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x1a                                  ..
    decimal
             46   26
    datetime ((2015, 1, 27, 31, 27, 13))
    0000   0x0d 0x5b 0x5f 0x7b 0x2f                   .[_{/
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 3 Base (2013, 0, 13, 16, 36, 13) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x1a                                  ..
    decimal
             14   26
    datetime ((2013, 0, 13, 16, 36, 13))
    0000   0x0d 0x24 0x50 0x0d 0x2d                   .$P.-
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 4 Base (2000, 3, 4, 0, 48, 27) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xfd                                  j.
    decimal
            106  253
    datetime ((2000, 3, 4, 0, 48, 27))
    0000   0x1b 0xf0 0x00 0x04 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 NewTimeSet 2004-04-19T20:08:28 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x7d                                  .}
    decimal
             24  125
    datetime (2004-04-19T20:08:28)
    0000   0x5c 0x08 0x14 0x53 0x04                   \..S.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 0, 24, 24, 1, 20) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x75                                  .u
    decimal
            192  117
    datetime ((2000, 0, 24, 24, 1, 20))
    0000   0x14 0x01 0x18 0x18 0x00                   .....
    body (0)

#### RECORD 7 BasalProfileStart 2000-04-30T13:26:14 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x2f                                  {/
    decimal
            123   47
    datetime (2000-04-30T13:26:14)
    0000   0x4e 0x1a 0x0d 0x1e 0x00                   N....
    body (3)
    hex
    0000   0x50 0x11 0x10                             P..
    decimal
             80   17   16

#### RECORD 8 Battery (2001, 0, 13, 26, 0, 31) head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x0d                                  ..
    decimal
             26   13
    datetime ((2001, 0, 13, 26, 0, 31))
    0000   0x1f 0x00 0x7a 0x2d 0x11                   ..z-.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Battery 2004-03-12T07:46:10 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x0d                                  ..
    decimal
             26   13
    datetime (2004-03-12T07:46:10)
    0000   0x0a 0xee 0x47 0x0c 0x34                   ..G.4
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 10 Battery 2004-07-12T20:46:27 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x0d                                  ..
    decimal
             26   13
    datetime (2004-07-12T20:46:27)
    0000   0x5b 0xee 0x74 0x0c 0x14                   [.t..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 11 Battery 2010-01-13T13:16:38 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x0d                                  ..
    decimal
             26   13
    datetime (2010-01-13T13:16:38)
    0000   0x26 0x50 0x0d 0x2d 0x6a                   &P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 LowBattery (2006, 0, 0, 0, 0, 0) head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x1d                                  ..
    decimal
             25   29
    datetime ((2006, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x36                   ....6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 13 Base (2004, 1, 20, 8, 32, 8) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2004, 1, 20, 8, 32, 8))
    0000   0x08 0x60 0x48 0x14 0x14                   .`H..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2004, 0, 0, 22, 54, 1) head[2], body[0] op[0x98]

    op hex (2)
    0000   0x98 0x14                                  ..
    decimal
            152   20
    datetime ((2004, 0, 0, 22, 54, 1))
    0000   0x01 0x36 0x36 0x00 0x74                   .66.t
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 15 ClearAlarm (2015, 0, 5, 10, 13, 26) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x54                                  .T
    decimal
             12   84
    datetime ((2015, 0, 5, 10, 13, 26))
    0000   0x1a 0x0d 0x0a 0x45 0x4f                   ...EO
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 16 Rewind (2000, 0, 0, 7, 13, 26) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x36                                  !6
    decimal
             33   54
    datetime ((2000, 0, 0, 7, 13, 26))
    0000   0x1a 0x0d 0x07 0x00 0x00                   .....
    body (0)

#### RECORD 17 Base (2013, 4, 26, 13, 13, 26) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x88                                  ..
    decimal
              5  136
    datetime ((2013, 4, 26, 13, 13, 26))
    0000   0x5a 0x0d 0x6d 0x5a 0x0d                   Z.mZ.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 18 Base (2000, 9, 10, 14, 5, 7) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 9, 10, 14, 5, 7))
    0000   0x87 0x45 0xee 0x0a 0x00                   .E...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 Base (2002, 8, 28, 12, 3, 8) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2002, 8, 28, 12, 3, 8))
    0000   0x88 0x03 0x4c 0x3c 0x02                   ..L<.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 20 Base (2008, 2, 28, 2, 6, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x28                                  <(
    decimal
             60   40
    datetime ((2008, 2, 28, 2, 6, 0))
    0000   0x00 0x86 0x02 0x3c 0x28                   ...<(
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 21 Bolus (2002, 0, 2, 1, 5, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 14.0, 'dual_component': '??', 'programmed': 6.9, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x8c 0x45 0x00 0xb0 0x1f 0x00 0x00    ..E.....
    decimal
              1  140   69    0  176   31    0    0
    datetime ((2002, 0, 2, 1, 5, 0))
    0000   0x00 0x05 0x01 0x02 0x02                   .....
    body (0)

#### RECORD 22 Base (2000, 3, 0, 0, 40, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2000, 3, 0, 0, 40, 0))
    0000   0x00 0xe8 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 CalBGForPH 2013-04-27T00:28:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-04-27T00:28:56)
    0000   0x78 0x1c 0x20 0x1b 0x0d                   x. ..
    body (0)

#### RECORD 24 CalBGForPH 2013-04-27T07:23:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-04-27T07:23:12)
    0000   0x4c 0x17 0x27 0x1b 0x0d                   L.'..
    body (0)

#### RECORD 25 BolusWizard 2013-04-27T07:23:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 200,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc8                                  [.
    decimal
             91  200
    datetime (2013-04-27T07:23:14)
    0000   0x4e 0x17 0x07 0x1b 0x0d                   N....
    body (15)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d 0x01 0x10         ....}..
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125    1   16

#### RECORD 26 Base (2013, 4, 27, 7, 23, 14) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2013, 4, 27, 7, 23, 14))
    0000   0x4e 0x17 0x47 0x1b 0x0d                   N.G..
    body (0)

#### RECORD 27 PumpSuspend 2013-04-27T07:36:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-27T07:36:33)
    0000   0x61 0x24 0x07 0x1b 0x0d                   a$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 PumpResume 2013-04-27T07:43:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-27T07:43:05)
    0000   0x45 0x2b 0x07 0x1b 0x0d                   E+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 CalBGForPH 2013-04-27T08:54:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-04-27T08:54:20)
    0000   0x54 0x36 0x28 0x1b 0x0d                   T6(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 CalBGForPH 2013-04-27T08:55:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-04-27T08:55:39)
    0000   0x67 0x37 0x28 0x1b 0x0d                   g7(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BolusWizard 2013-04-27T08:55:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-04-27T08:55:57)
    0000   0x79 0x37 0x08 0x1b 0x0d                   y7...
    body (15)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x01 0x1b 0x00    $P.-j...
    0008   0x00 0x0a 0x00 0x1b 0x7d 0x5c 0x08         ....}\.
    decimal
             36   80   13   45  106    1   27    0
              0   10    0   27  125   92    8
    HOUR BITS: [0, 0, 1]
#### RECORD 32 Base (2001, 0, 4, 5, 46, 4) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x5b                                  .[
    decimal
             18   91
    datetime ((2001, 0, 4, 5, 46, 4))
    0000   0x04 0x2e 0x65 0x04 0x01                   ..e..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 Base (2011, 1, 8, 23, 57, 0) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x1b                                  ..
    decimal
             27   27
    datetime ((2011, 1, 8, 23, 57, 0))
    0000   0x00 0x79 0x37 0x48 0x1b                   .y7H.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 34 Base (2011, 9, 9, 16, 42, 6) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2011, 9, 9, 16, 42, 6))
    0000   0x86 0x6a 0x10 0x29 0x1b                   .j.).
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 35 Base (2011, 9, 9, 18, 15, 6) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2011, 9, 9, 18, 15, 6))
    0000   0x86 0x4f 0x12 0x09 0x1b                   .O...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 36 Base (2002, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2c                                  .,
    decimal
             13   44
    datetime ((2002, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x02                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 37 Rewind (2013, 0, 1, 0, 34, 0) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime ((2013, 0, 1, 0, 34, 0))
    0000   0x00 0x22 0x00 0x21 0x7d                   .".!}
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.7, 'curve': 4},
 {'age': 114, 'amount': 0.45, 'curve': 4},
 {'age': 124, 'amount': 1.15, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x18 0x04 0x12 0x72 0x04    \.l...r.
    0008   0x2e 0x7c 0x04                             .|.
    decimal
             92   11  108   24    4   18  114    4
             46  124    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus (2007, 0, 17, 14, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x21 0x21 0x00 0x50 0x12 0x49 0x1b    .!!.P.I.
    decimal
              1   33   33    0   80   18   73   27
    datetime ((2007, 0, 17, 14, 10, 13))
    0000   0x0d 0x0a 0x6e 0x51 0x37                   ..nQ7
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 40 Base (2000, 0, 15, 10, 10, 13) head[2], body[0] op[0x29]

    op hex (2)
    0000   0x29 0x1b                                  ).
    decimal
             41   27
    datetime ((2000, 0, 15, 10, 10, 13))
    0000   0x0d 0x0a 0x6a 0x6f 0x00                   ..jo.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 41 Base (2007, 0, 24, 8, 10, 13) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x1b                                  *.
    decimal
             42   27
    datetime ((2007, 0, 24, 8, 10, 13))
    0000   0x0d 0x0a 0x68 0x78 0x17                   ..hx.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 42 Base (2013, 0, 10, 30, 51, 13) head[2], body[0] op[0x2b]

    op hex (2)
    0000   0x2b 0x1b                                  +.
    decimal
             43   27
    datetime ((2013, 0, 10, 30, 51, 13))
    0000   0x0d 0x33 0x1e 0x4a 0x2d                   .3.J-
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 43 Ian0B (2013, 0, 10, 5, 22, 0) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x1b 0x0d                             ...
    decimal
             11   27   13
    datetime ((2013, 0, 10, 5, 22, 0))
    0000   0x00 0x16 0x05 0x4a 0x2d                   ...J-
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 44 Ian0B (2011, 0, 20, 23, 54, 10) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x1b 0x0d                             ...
    decimal
             11   27   13
    datetime ((2011, 0, 20, 23, 54, 10))
    0000   0x0a 0x36 0x57 0x34 0x2b                   .6W4+
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 45 Base (2012, 0, 13, 23, 24, 51) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x0d                                  ..
    decimal
             27   13
    datetime ((2012, 0, 13, 23, 24, 51))
    0000   0x33 0x18 0x57 0x0d 0x0c                   3.W..
    body (0)

#### RECORD 46 Base (2013, 0, 23, 4, 22, 0) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x0d                                  ..
    decimal
             27   13
    datetime ((2013, 0, 23, 4, 22, 0))
    0000   0x00 0x16 0x04 0x57 0x0d                   ...W.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 47 ClearAlarm (2013, 0, 2, 18, 51, 13) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x1b                                  ..
    decimal
             12   27
    datetime ((2013, 0, 2, 18, 51, 13))
    0000   0x0d 0x33 0x12 0x62 0x0d                   .3.b.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 ClearAlarm (2002, 0, 4, 22, 0, 13) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x1b                                  ..
    decimal
             12   27
    datetime ((2002, 0, 4, 22, 0, 13))
    0000   0x0d 0x00 0x16 0x04 0x62                   ....b
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 49 Base (2007, 0, 28, 10, 13, 27) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0c                                  ..
    decimal
             13   12
    datetime ((2007, 0, 28, 10, 13, 27))
    0000   0x1b 0x0d 0x0a 0x5c 0x57                   ...\W
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 50 Base (2003, 0, 9, 10, 13, 27) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x2c                                  .,
    decimal
             17   44
    datetime ((2003, 0, 9, 10, 13, 27))
    0000   0x1b 0x0d 0x0a 0x69 0x53                   ...iS
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 51 Base (2001, 0, 23, 10, 13, 27) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x2c                                  *,
    decimal
             42   44
    datetime ((2001, 0, 23, 10, 13, 27))
    0000   0x1b 0x0d 0x0a 0xd7 0x61                   ....a
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 52 Rewind (2006, 0, 23, 27, 13, 27) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x2e                                  !.
    decimal
             33   46
    datetime ((2006, 0, 23, 27, 13, 27))
    0000   0x1b 0x0d 0x5b 0xd7 0x66                   ..[.f
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 53 Rewind (2013, 0, 16, 0, 13, 27) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x0e                                  !.
    decimal
             33   14
    datetime ((2013, 0, 16, 0, 13, 27))
    0000   0x1b 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 54 Base (2000, 0, 0, 0, 0, 20) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 20))
    0000   0x14 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 55 Base (2015, 5, 4, 14, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x14                                  ..
    decimal
              0   20
    datetime ((2015, 5, 4, 14, 28, 61))
    0000   0x7d 0x5c 0x0e 0x84 0x3f                   }\..?
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 56 SelectBasalProfile 2004-04-13T18:20:19 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x6c                                  .l
    decimal
             20  108
    datetime (2004-04-13T18:20:19)
    0000   0x53 0x14 0x12 0xad 0x14                   S....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 57 Base (2000, 0, 20, 20, 1, 20) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0xb7                                  ..
    decimal
             46  183
    datetime ((2000, 0, 20, 20, 1, 20))
    0000   0x14 0x01 0x14 0x14 0x00                   .....
    body (0)

#### RECORD 58 Base (2011, 4, 10, 13, 27, 14) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x21                                  f!
    decimal
            102   33
    datetime ((2011, 4, 10, 13, 27, 14))
    0000   0x4e 0x1b 0x0d 0x0a 0x7b                   N...{
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 59 Base (2000, 0, 10, 13, 27, 47) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x05                                  V.
    decimal
             86    5
    datetime ((2000, 0, 10, 13, 27, 47))
    0000   0x2f 0x1b 0x0d 0x0a 0x80                   /....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 Base (2000, 0, 30, 13, 27, 48) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x02                                  C.
    decimal
             67    2
    datetime ((2000, 0, 30, 13, 27, 48))
    0000   0x30 0x1b 0x0d 0x1e 0x00                   0....
    body (0)

#### RECORD 61 Base (2000, 0, 31, 13, 27, 17) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x30                                  V0
    decimal
             86   48
    datetime ((2000, 0, 31, 13, 27, 17))
    0000   0x11 0x1b 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 62 Base (2007, 0, 10, 13, 27, 18) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x29                                  S)
    decimal
             83   41
    datetime ((2007, 0, 10, 13, 27, 18))
    0000   0x12 0x1b 0x0d 0x0a 0xa7                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 63 Base (2007, 0, 27, 13, 27, 54) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x15                                  U.
    decimal
             85   21
    datetime ((2007, 0, 27, 13, 27, 54))
    0000   0x36 0x1b 0x0d 0x5b 0xa7                   6..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 64 Base (2000, 0, 7, 13, 27, 22) head[2], body[0] op[0x73]

    op hex (2)
    0000   0x73 0x15                                  s.
    decimal
            115   21
    datetime ((2000, 0, 7, 13, 27, 22))
    0000   0x16 0x1b 0x0d 0x07 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 65 Base (2000, 4, 0, 5, 9, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 5, 9, 42))
    0000   0x6a 0x09 0x05 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-23.data: 66 records`
