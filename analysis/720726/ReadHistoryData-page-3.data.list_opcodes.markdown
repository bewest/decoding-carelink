## START logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x65 0xf3                                  e.
##### DEBUG DECIMAL
            101  243
#### RECORD 0 Ian0B 2013-09-08T19:34:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x2e                             .f.
    decimal
             11  102   46
    datetime (2013-09-08T19:34:07)
    0000   0x87 0x62 0x53 0xa8 0x0d                   .bS..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 1 PumpSuspend 2013-09-08T19:34:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T19:34:07)
    0000   0x87 0x62 0x13 0x08 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 PumpSuspend 2013-09-08T19:34:11 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T19:34:11)
    0000   0x8b 0x62 0x13 0x08 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 PumpSuspend 2013-09-08T19:36:14 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x44                                  .D
    decimal
             30   68
    datetime (2013-09-08T19:36:14)
    0000   0x8e 0x64 0x13 0x08 0x0d                   .d...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 PumpSuspend 2013-09-08T19:38:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x85                                  ..
    decimal
             30  133
    datetime (2013-09-08T19:38:20)
    0000   0x94 0x66 0x13 0x08 0x0d                   .f...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 PumpSuspend 2013-09-08T19:40:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0xa5                                  ..
    decimal
             30  165
    datetime (2013-09-08T19:40:29)
    0000   0x9d 0x68 0x13 0x08 0x0d                   .h...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 PumpResume 2013-09-08T19:50:52 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xa6                                  ..
    decimal
             31  166
    datetime (2013-09-08T19:50:52)
    0000   0xb4 0x72 0x13 0x08 0x0d                   .r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 BasalProfileStart 2013-09-08T19:50:52 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T19:50:52)
    0000   0xb4 0x72 0x13 0x08 0x0d                   .r...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 1]
#### RECORD 8 PumpResume 2013-09-08T19:50:53 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T19:50:53)
    0000   0xb5 0x72 0x13 0x08 0x0d                   .r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 9 CalBGForPH 2013-09-08T19:51:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-09-08T19:51:45)
    0000   0xad 0x73 0x33 0x68 0x0d                   .s3h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 Ian3F 2013-09-08T19:51:45 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2013-09-08T19:51:45)
    0000   0xad 0x73 0xf3 0x68 0x0d                   .s.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 BolusWizard 2013-09-08T19:52:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 93,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2013-09-08T19:52:00)
    0000   0x80 0x74 0x13 0x08 0x0d                   .t...
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x00 0x00 0x00 0x08 0x00 0x38 0x36         .....86
    decimal
              0  144    0  110   23   54   64    0
              0    0    0    8    0   56   54
    HOUR BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 0.5, 'curve': 4},
 {'age': 98, 'amount': 2.25, 'curve': 20},
 {'age': 108, 'amount': 0.15, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x90 0x04 0x5a 0x62 0x14    \....Zb.
    0008   0x06 0x6c 0x14                             .l.
    decimal
             92   11   20  144    4   90   98   20
              6  108   20
    datetime (unknown)

    body (0)

#### RECORD 13 BolusWizard 2013-09-08T19:52:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 93,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2013-09-08T19:52:02)
    0000   0x82 0x74 0x13 0x08 0x0d                   .t...
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x00 0x00 0x00 0x08 0x00 0x38 0x36         .....86
    decimal
              0  144    0  110   23   54   64    0
              0    0    0    8    0   56   54
    HOUR BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 0.5, 'curve': 4},
 {'age': 98, 'amount': 2.25, 'curve': 20},
 {'age': 108, 'amount': 0.15, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x90 0x04 0x5a 0x62 0x14    \....Zb.
    0008   0x06 0x6c 0x14                             .l.
    decimal
             92   11   20  144    4   90   98   20
              6  108   20
    datetime (unknown)

    body (0)

#### RECORD 15 BolusWizard 2013-09-08T19:52:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 93,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2013-09-08T19:52:11)
    0000   0x8b 0x74 0x13 0x08 0x0d                   .t...
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x4c 0x00 0x00 0x08 0x00 0x84 0x36         L.....6
    decimal
             21  144    0  110   23   54   64    0
             76    0    0    8    0  132   54
    HOUR BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 0.5, 'curve': 4},
 {'age': 98, 'amount': 2.25, 'curve': 20},
 {'age': 108, 'amount': 0.15, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x90 0x04 0x5a 0x62 0x14    \....Zb.
    0008   0x06 0x6c 0x14                             .l.
    decimal
             92   11   20  144    4   90   98   20
              6  108   20
    datetime (unknown)

    body (0)

#### RECORD 17 Ian69 2013-09-08T19:52:11 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-08T19:52:11)
    0000   0x8b 0x74 0x73 0x08 0x0d                   .ts..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 1]
#### RECORD 18 Ian0B 2013-09-08T19:53:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x34                             .f4
    decimal
             11  102   52
    datetime (2013-09-08T19:53:03)
    0000   0x83 0x75 0x53 0xa8 0x0d                   .uS..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 19 Bolus 2013-09-08T19:52:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x08 0x00    ........
    decimal
              1    0  132    0  132    0    8    0
    datetime (2013-09-08T19:52:11)
    0000   0x8b 0x74 0x53 0x08 0x0d                   .tS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 20 Ian0B 2013-09-08T20:03:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2013-09-08T20:03:00)
    0000   0x80 0x43 0x54 0xa8 0x0d                   .CT..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 21 Ian0B 2013-09-08T20:03:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2013-09-08T20:03:00)
    0000   0x80 0x43 0x54 0xa8 0x0d                   .CT..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2013-09-08T20:07:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-09-08T20:07:20)
    0000   0x94 0x47 0x54 0x08 0x0d                   .GT..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 23 BolusWizard 2013-09-08T20:37:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-08T20:37:29)
    0000   0x9d 0x65 0x14 0x68 0x0d                   .e.h.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 3.3, 'curve': 4},
 {'age': 189, 'amount': 0.5, 'curve': 4},
 {'age': 143, 'amount': 2.25, 'curve': 20},
 {'age': 153, 'amount': 0.15, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x31 0x04 0x14 0xbd 0x04    \..1....
    0008   0x5a 0x8f 0x14 0x06 0x99 0x14              Z.....
    decimal
             92   14  132   49    4   20  189    4
             90  143   20    6  153   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-09-08T20:37:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x78 0x00    ..H.H.x.
    decimal
              1    0   72    0   72    0  120    0
    datetime (2013-09-08T20:37:29)
    0000   0x9d 0x65 0x54 0x68 0x0d                   .eTh.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2013-09-08T20:50:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-08T20:50:13)
    0000   0x8d 0x72 0x14 0x68 0x0d                   .r.h.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 1.05, 'curve': 4},
 {'age': 22, 'amount': 0.75, 'curve': 4},
 {'age': 62, 'amount': 3.3, 'curve': 4},
 {'age': 202, 'amount': 0.5, 'curve': 4},
 {'age': 156, 'amount': 2.25, 'curve': 20},
 {'age': 166, 'amount': 0.15, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x2a 0x0c 0x04 0x1e 0x16 0x04    \.*.....
    0008   0x84 0x3e 0x04 0x14 0xca 0x04 0x5a 0x9c    .>....Z.
    0010   0x14 0x06 0xa6 0x14                        ....
    decimal
             92   20   42   12    4   30   22    4
            132   62    4   20  202    4   90  156
             20    6  166   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-09-08T20:50:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0xb4 0x00    ..H.H...
    decimal
              1    0   72    0   72    0  180    0
    datetime (2013-09-08T20:50:13)
    0000   0x8d 0x72 0x54 0x68 0x0d                   .rTh.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 29 Ian0B 2013-09-08T20:57:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2013-09-08T20:57:22)
    0000   0x96 0x79 0x54 0xa8 0x0d                   .yT..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 30 NoDelivery 2013-09-08T21:13:03 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T21:13:03)
    0000   0x83 0x4d 0xb5 0x88 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0]
#### RECORD 31 PumpSuspend 2013-09-08T21:13:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T21:13:03)
    0000   0x83 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 PumpSuspend 2013-09-08T21:13:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T21:13:09)
    0000   0x89 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 ClearAlarm 2013-09-08T21:13:13 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x67                                  .g
    decimal
             12  103
    datetime (2013-09-08T21:13:13)
    0000   0x8d 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 34 PumpSuspend 2013-09-08T21:13:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x43                                  .C
    decimal
             30   67
    datetime (2013-09-08T21:13:16)
    0000   0x90 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 35 PumpSuspend 2013-09-08T21:13:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x65                                  .e
    decimal
             30  101
    datetime (2013-09-08T21:13:18)
    0000   0x92 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 PumpResume 2013-09-08T21:13:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xa6                                  ..
    decimal
             31  166
    datetime (2013-09-08T21:13:20)
    0000   0x94 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 BasalProfileStart 2013-09-08T21:13:20 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T21:13:20)
    0000   0x94 0x4d 0x15 0x08 0x0d                   .M...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 38 PumpResume 2013-09-08T21:13:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T21:13:22)
    0000   0x96 0x4d 0x15 0x08 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 Ian0B 2013-09-08T21:19:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x33                             .f3
    decimal
             11  102   51
    datetime (2013-09-08T21:19:07)
    0000   0x87 0x53 0x55 0xa8 0x0d                   .SU..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 40 CalBGForPH 2013-09-08T21:26:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 63}
```
    op hex (2)
    0000   0x0a 0x3f                                  .?
    decimal
             10   63
    datetime (2013-09-08T21:26:47)
    0000   0xaf 0x5a 0x35 0x68 0x0d                   .Z5h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2013-09-08T21:26:47 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2013-09-08T21:26:47)
    0000   0xaf 0x5a 0xf5 0x68 0x0d                   .Z.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 TempBasal 2013-09-08T21:32:06 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.625}
```
    op hex (2)
    0000   0x33 0x19                                  3.
    decimal
             51   25
    datetime (2013-09-08T21:32:06)
    0000   0x86 0x60 0x15 0x08 0x0d                   .`...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [0, 1, 1]
#### RECORD 43 TempBasalDuration 2013-09-08T21:32:06 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 600}
```
    op hex (2)
    0000   0x16 0x14                                  ..
    decimal
             22   20
    datetime (2013-09-08T21:32:06)
    0000   0x86 0x60 0x15 0x08 0x0d                   .`...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 44 NoDelivery 2013-09-08T21:34:07 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T21:34:07)
    0000   0x87 0x62 0xb5 0x88 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 45 PumpSuspend 2013-09-08T21:34:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T21:34:07)
    0000   0x87 0x62 0x15 0x08 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 ClearAlarm 2013-09-08T21:34:14 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x67                                  .g
    decimal
             12  103
    datetime (2013-09-08T21:34:14)
    0000   0x8e 0x62 0x15 0x08 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 47 PumpSuspend 2013-09-08T21:34:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x43                                  .C
    decimal
             30   67
    datetime (2013-09-08T21:34:18)
    0000   0x92 0x62 0x15 0x08 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 48 Ian0B 2013-09-08T21:37:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x2e                             .f.
    decimal
             11  102   46
    datetime (2013-09-08T21:37:22)
    0000   0x96 0x65 0x55 0xa8 0x0d                   .eU..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 49 Ian0B 2013-09-08T21:59:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x36                             .f6
    decimal
             11  102   54
    datetime (2013-09-08T21:59:07)
    0000   0x87 0x7b 0x55 0xa8 0x0d                   .{U..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 50 Ian0B 2013-09-08T22:17:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2013-09-08T22:17:22)
    0000   0x96 0x51 0x56 0xa8 0x0d                   .QV..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 51 PumpSuspend 2013-09-08T22:40:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x64                                  .d
    decimal
             30  100
    datetime (2013-09-08T22:40:17)
    0000   0x91 0x68 0x16 0x08 0x0d                   .h...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 52 PumpSuspend 2013-09-08T22:40:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x85                                  ..
    decimal
             30  133
    datetime (2013-09-08T22:40:40)
    0000   0xa8 0x68 0x16 0x08 0x0d                   .h...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 53 PumpResume 2013-09-08T22:40:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xa6                                  ..
    decimal
             31  166
    datetime (2013-09-08T22:40:50)
    0000   0xb2 0x68 0x16 0x08 0x0d                   .h...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 54 PumpResume 2013-09-08T22:40:51 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T22:40:51)
    0000   0xb3 0x68 0x16 0x08 0x0d                   .h...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 Ian54 2013-09-08T22:45:21 head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0xf0                                  T.
    decimal
             84  240
    datetime (2013-09-08T22:45:21)
    0000   0x95 0x6d 0x56 0x08 0x0d                   .mV..
    body (57)
    hex
    0000   0xff 0xf0 0xff 0x00 0x55 0x28 0x0e 0x64    ....U(.d
    0008   0x28 0x00 0xff 0xff 0x00 0xff 0xff 0x00    (.......
    0010   0xff 0xff 0x00 0xff 0xff 0x00 0xff 0xff    ........
    0018   0x00 0xff 0xff 0xf0 0xff 0xf0 0xff 0x00    ........
    0020   0x00 0x00 0x0e 0x00 0x00 0x00 0xff 0xff    ........
    0028   0x00 0xff 0xff 0x00 0xff 0xff 0x00 0xff    ........
    0030   0xff 0x00 0xff 0xff 0x00 0xff 0xff 0x8b    ........
    0038   0x02                                       .
    decimal
            255  240  255    0   85   40   14  100
             40    0  255  255    0  255  255    0
            255  255    0  255  255    0  255  255
              0  255  255  240  255  240  255    0
              0    0   14    0    0    0  255  255
              0  255  255    0  255  255    0  255
            255    0  255  255    0  255  255  139
              2
    HOUR BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2013-09-08T22:52:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2013-09-08T22:52:41)
    0000   0xa9 0x74 0x36 0x68 0x0d                   .t6h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 Ian3F 2013-09-08T22:52:41 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2013-09-08T22:52:41)
    0000   0xa9 0x74 0x76 0x68 0x0d                   .tvh.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2013-09-08T22:52:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 8.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 13.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-09-08T22:52:57)
    0000   0xb9 0x74 0x16 0x68 0x0d                   .t.h.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x84 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x50 0x00 0x34 0x36         ...P.46
    decimal
              0  144    0  110   23   54  132    0
              0    0    0   80    0   52   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 1.8, 'curve': 4},
 {'age': 134, 'amount': 1.05, 'curve': 4},
 {'age': 144, 'amount': 0.75, 'curve': 4},
 {'age': 184, 'amount': 3.3, 'curve': 4},
 {'age': 68, 'amount': 0.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x7c 0x04 0x2a 0x86 0x04    \.H|.*..
    0008   0x1e 0x90 0x04 0x84 0xb8 0x04 0x14 0x44    .......D
    0010   0x14                                       .
    decimal
             92   17   72  124    4   42  134    4
             30  144    4  132  184    4   20   68
             20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-09-08T22:52:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x50 0x00    ..L.L.P.
    decimal
              1    0   76    0   76    0   80    0
    datetime (2013-09-08T22:52:57)
    0000   0xb9 0x74 0x56 0x68 0x0d                   .tVh.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 ResultTotals (2000, 10, 0, 0, 13, 8) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xf4                   .....
    decimal
              7    0    0    5  244
    datetime ((2000, 10, 0, 0, 13, 8))
    0000   0x88 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x88 0x8d 0x06 0x00 0x7b 0x35 0xeb    n....{5.
    0008   0x0f 0x00 0x00 0x05 0xf4 0x03 0x10 0x33    .......3
    0010   0x02 0xe4 0x31 0x00 0x72 0x01 0x08 0x00    ..1.r...
    0018   0xf8 0x00 0xe4 0x00 0x00 0x04 0x03 0x02    ........
    0020   0x00 0x00 0x49 0x00 0x36 0x2e 0xa2 0x12    ..I.6...
    0028   0x00 0x00 0xa8 0xa8 0x14 0x00 0x00         .......
    decimal
            110  136  141    6    0  123   53  235
             15    0    0    5  244    3   16   51
              2  228   49    0  114    1    8    0
            248    0  228    0    0    4    3    2
              0    0   73    0   54   46  162   18
              0    0  168  168   20    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 63 CalBGForPH 2013-09-09T03:57:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 27}
```
    op hex (2)
    0000   0x0a 0x1b                                  ..
    decimal
             10   27
    datetime (2013-09-09T03:57:41)
    0000   0xa9 0x79 0xa3 0x69 0x0d                   .y.i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 Ian3F 2013-09-09T03:57:41 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x43                                  ?C
    decimal
             63   67
    datetime (2013-09-09T03:57:41)
    0000   0xa9 0x79 0x63 0x69 0x0d                   .yci.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 BolusWizard 2013-09-09T03:57:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 299,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 16.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2b                                  [+
    decimal
             91   43
    datetime (2013-09-09T03:57:54)
    0000   0xb6 0x79 0x03 0x69 0x0d                   .y.i.
    body (15)
    hex
    0000   0x00 0x91 0x00 0x6e 0x17 0x36 0xa8 0x00    ...n.6..
    0008   0x00 0x08 0x00 0x00 0x01 0xa8 0x36         ......6
    decimal
              0  145    0  110   23   54  168    0
              0    8    0    0    1  168   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.9, 'curve': 20},
 {'age': 173, 'amount': 1.8, 'curve': 20},
 {'age': 183, 'amount': 1.05, 'curve': 20},
 {'age': 193, 'amount': 0.75, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x4c 0x35 0x14 0x48 0xad 0x14    \.L5.H..
    0008   0x2a 0xb7 0x14 0x1e 0xc1 0x14              *.....
    decimal
             92   14   76   53   20   72  173   20
             42  183   20   30  193   20
    datetime (unknown)

    body (0)

#### RECORD 67 LowReservoir 2013-09-09T03:57:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 12.8}
```
    op hex (2)
    0000   0x34 0x80                                  4.
    decimal
             52  128
    datetime (2013-09-09T03:57:54)
    0000   0xb6 0x79 0x03 0x09 0x8d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 Bolus 2013-09-09T03:57:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x78 0x01 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    1  120    1  120    0    0    0
    datetime (2013-09-09T03:57:54)
    0000   0xb6 0x79 0x43 0x69 0x0d                   .yCi.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 Ian0B 2013-09-09T07:07:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2013-09-09T07:07:00)
    0000   0x80 0x47 0x47 0xa9 0x0d                   .GG..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 70 BasalProfileStart 2013-09-09T07:32:06 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-09T07:32:06)
    0000   0x86 0x60 0x07 0x09 0x0d                   .`...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 1]
#### RECORD 71 CalBGForPH 2013-09-09T07:45:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 294}
```
    op hex (2)
    0000   0x0a 0x26                                  .&
    decimal
             10   38
    datetime (2013-09-09T07:45:43)
    0000   0xab 0x6d 0x27 0x69 0x8d                   .m'i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 72 Ian3F 2013-09-09T07:45:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x24                                  ?$
    decimal
             63   36
    datetime (2013-09-09T07:45:43)
    0000   0xab 0x6d 0xc7 0x69 0x0d                   .m.i.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 BolusWizard 2013-09-09T07:45:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 18.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-09-09T07:45:59)
    0000   0xbb 0x6d 0x07 0x69 0x0d                   .m.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xbc 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x1c 0x00 0xa0 0x36         ......6
    decimal
              0  144    0  110   23   54  188    0
              0    0    0   28    0  160   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 227, 'amount': 2.7, 'curve': 5},
 {'age': 237, 'amount': 0.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0xe3 0x05 0x0c 0xed 0x04    \.l.....
    decimal
             92    8  108  227    5   12  237    4
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-09-09T07:45:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x1c 0x00    ........
    decimal
              1    0  160    0  160    0   28    0
    datetime (2013-09-09T07:45:59)
    0000   0xbb 0x6d 0x47 0x69 0x0d                   .mGi.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 Ian0B 2013-09-09T08:03:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2013-09-09T08:03:00)
    0000   0x80 0x43 0x48 0xa9 0x0d                   .CH..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 77 Ian0B 2013-09-09T08:03:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2013-09-09T08:03:00)
    0000   0x80 0x43 0x48 0xa9 0x0d                   .CH..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 78 CalBGForPH 2013-09-09T08:04:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-09-09T08:04:11)
    0000   0x8b 0x44 0x48 0x09 0x0d                   .DH..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 79 Rewind 2013-09-09T08:43:36 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-09-09T08:43:36)
    0000   0xa4 0x6b 0x08 0x09 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 80 Prime 2013-09-09T08:44:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2013-09-09T08:44:17)
    0000   0x91 0x6c 0x28 0x09 0x0d                   .l(..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 81 BasalProfileStart 2013-09-09T08:44:25 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-09T08:44:25)
    0000   0x99 0x6c 0x08 0x09 0x0d                   .l...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 1]
#### RECORD 82 PumpSuspend 2013-09-09T09:01:36 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-09-09T09:01:36)
    0000   0xa4 0x41 0x09 0x09 0x0d                   .A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 83 BasalProfileStart 2013-09-09T10:06:29 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-09T10:06:29)
    0000   0x9d 0x46 0x0a 0x09 0x0d                   .F...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 84 PumpResume 2013-09-09T10:06:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-09-09T10:06:29)
    0000   0x9d 0x46 0x0a 0x09 0x0d                   .F...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 85 Ian69 2013-09-09T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-09T10:30:00)
    0000   0x80 0x5e 0x0a 0x09 0x0d                   .^...
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30
    HOUR BITS: [0, 1, 0]
#### RECORD 86 CalBGForPH 2013-09-09T11:01:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2013-09-09T11:01:59)
    0000   0xbb 0x41 0x2b 0x69 0x0d                   .A+i.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 87 Ian3F 2013-09-09T11:01:59 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2013-09-09T11:01:59)
    0000   0xbb 0x41 0xeb 0x69 0x0d                   .A.i.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 88 BolusWizard 2013-09-09T11:10:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-09-09T11:10:57)
    0000   0xb9 0x4a 0x0b 0x69 0x0d                   .J.i.
    body (15)
    hex
    0000   0x10 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    ...n.6$.
    0008   0x38 0x00 0x00 0x10 0x00 0x4c 0x36         8....L6
    decimal
             16  144    0  110   23   54   36    0
             56    0    0   16    0   76   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 89 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 202, 'amount': 1.0, 'curve': 4},
 {'age': 212, 'amount': 3.0, 'curve': 4},
 {'age': 176, 'amount': 2.7, 'curve': 21},
 {'age': 186, 'amount': 0.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0xca 0x04 0x78 0xd4 0x04    \.(..x..
    0008   0x6c 0xb0 0x15 0x0c 0xba 0x14              l.....
    decimal
             92   14   40  202    4  120  212    4
            108  176   21   12  186   20
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-3.data: 90 records`
