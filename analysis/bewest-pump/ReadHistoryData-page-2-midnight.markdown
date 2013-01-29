### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-2.data.list_opcodes.markdown: 0
## START logs/ReadHistoryData-page-2.data
#### RECORD 0 BolusWizard 2013-01-14T05:44:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 372,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.6}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-01-14T05:44:31)
    0000   0x1f 0x6c 0x05 0x0e 0x0d                   .l...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x36 0x00 0x00    .Q.-j6..
    0008   0x00 0x1a 0x00 0x1c 0x7d                   ....}
    decimal
              0   81   13   45  106   54    0    0
              0   26    0   28  125
    HOUR BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 3.6, 'curve': 4},
 {'age': 200, 'amount': 0.3, 'curve': 4},
 {'age': 210, 'amount': 0.3, 'curve': 5},
 {'age': 204, 'amount': 1.9, 'curve': 20},
 {'age': 214, 'amount': 2.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x90 0x6e 0x04 0x0c 0xc8 0x04    \..n....
    0008   0x0c 0xd2 0x05 0x4c 0xcc 0x14 0x54 0xd6    ...L..T.
    0010   0x14                                       .
--
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2013-01-14T21:17:41)
    0000   0x29 0x51 0x35 0x0e 0x0d                   )Q5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xf4                                  ..
    decimal
              0  244
    datetime (unknown)
    0000   0x59                                       Y
    body (0)

`end logs/ReadHistoryData-page-2.data: 81 records`
