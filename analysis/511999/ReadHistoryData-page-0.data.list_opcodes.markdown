## START analysis/sarak/raw//ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 98, found 924 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x74 0x42                                  tB
##### DEBUG DECIMAL
            116   66
#### RECORD 0 BolusWizard 2013-09-04T14:17:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-09-04T14:17:33)
    0000   0xa1 0x51 0x0e 0x04 0x0d                   .Q...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x14 0x00 0x28 0x78         (....(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   20    0   40  120
    HOUR BITS: [0, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.7, 'curve': 192},
 {'age': 75, 'amount': 1.5, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x79 0xc0 0x3c 0x4b 0xd0    \.Dy.<K.
    decimal
             92    8   68  121  192   60   75  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-09-04T14:17:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x14 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   20    0
    datetime (2013-09-04T14:17:33)
    0000   0xa1 0x51 0x4e 0x04 0x0d                   .QN..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 CalBGForPH 2013-09-04T15:20:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 252}
```
    op hex (2)
    0000   0x0a 0xfc                                  ..
    decimal
             10  252
    datetime (2013-09-04T15:20:52)
    0000   0xb4 0x54 0x2f 0x04 0x0d                   .T/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 BolusWizard 2013-09-04T15:20:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 252,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfc                                  [.
    decimal
             91  252
    datetime (2013-09-04T15:20:55)
    0000   0xb7 0x54 0x0f 0x04 0x0d                   .T...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x58 0x00    .P.x<dX.
    0008   0x00 0x00 0x00 0x1c 0x00 0x3c 0x78         .....<x
    decimal
              0   80    0  120   60  100   88    0
              0    0    0   28    0   60  120
    HOUR BITS: [0, 1, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 1.0, 'curve': 192},
 {'age': 184, 'amount': 1.7, 'curve': 192},
 {'age': 138, 'amount': 1.5, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x40 0xc0 0x44 0xb8 0xc0    \.(@.D..
    0008   0x3c 0x8a 0xd0                             <..
    decimal
             92   11   40   64  192   68  184  192
             60  138  208
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-09-04T15:20:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x1c 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   28    0
    datetime (2013-09-04T15:20:55)
    0000   0xb7 0x54 0x4f 0x04 0x0d                   .TO..
    body (0)
    HOUR BITS: [0, 1, 0]
`end analysis/sarak/raw//ReadHistoryData-page-0.data: 7 records`
