
# what do priming/bolus records look like

There is a better analysis in `history` or `rosetta` or something.
This one is done using `list_dates.py`


### another record
#### export
```
7/7/06 16:47:57 Rewind
  ACTION_REQUESTOR=pump
    0: Timestamp: 7/7/06 16:47:57
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Rewind
    16: Raw-Values: ACTION_REQUESTOR=pump

```

#### decoded
```
RECORD 18: 2006-07-07T16:47:57 0x45
  hex (7)
0000   0x45 0xce 0x30 0x07 0x06 0x21 0x00         E.0..!.
  decimal
         69  206   48    7    6   33    0
  datetime
0000   0x79 0xef 0x10 0x07 0x06                   y....
  extra(6) 
0000   0x03 0x00 0x00 0x00 0x13 0x74              .....t
          3    0    0    0   19  116

RECORD 19: 2006-07-07T16:49:12 0xf0
  hex (9)
0000   0xf0 0x30 0x07 0x06 0x03 0x00 0x03 0x00    .0......
0008   0x03                                       .
  decimal
        240   48    7    6    3    0    3    0
          3
  datetime
0000   0x4c 0xf1 0x10 0x07 0x06                   L....
  extra(0) None

```

### another record
#### export
```
7/7/06 16:48:52 Prime
  "AMOUNT=1.9, CONCENTRATION=null, PROGRAMMED_AMOUNT=0, PRIME_TYPE=manual,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 16:48:52
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=1.9 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0 && PRIME_TYPE=manual && ACTION_REQUESTOR=pump"

```

#### decoded
```
```
eaten by above


### another record
#### export
```
7/7/06 16:49:12 Prime
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 16:49:12
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && PRIME_TYPE=fixed && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 19: 2006-07-07T16:49:12 0xf0
  hex (9)
0000   0xf0 0x30 0x07 0x06 0x03 0x00 0x03 0x00    .0......
0008   0x03                                       .
  decimal
        240   48    7    6    3    0    3    0
          3
  datetime
0000   0x4c 0xf1 0x10 0x07 0x06                   L....
  extra(0) None

```


### another record
#### export
```
7/7/06 17:10:38 Prime
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 17:10:38
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && PRIME_TYPE=fixed && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 20: 2006-07-07T17:10:38 0x03
  hex (5)
0000   0x03 0x00 0x03 0x00 0x03                   .....
  decimal
          3    0    3    0    3
  datetime
0000   0x66 0xca 0x11 0x07 0x06                   f....
  extra(4) 
0000   0x03 0x00 0x03 0x00                        ....
          3    0    3    0

```


### another record
#### export
```
7/7/06 17:28:51 Prime
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 17:28:51
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && PRIME_TYPE=fixed && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 21: 2006-07-07T17:28:51 0x03
  hex (1)
0000   0x03                                       .
  decimal
          3
  datetime
0000   0x73 0xdc 0x11 0x07 0x06                   s....
  extra(4) 
0000   0x03 0x00 0x03 0x00                        ....
          3    0    3    0

```


### another record
#### export
```
7/7/06 17:41:14 Prime
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 17:41:14
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && PRIME_TYPE=fixed && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 22: 2006-07-07T17:41:14 0x03
  hex (1)
0000   0x03                                       .
  decimal
          3
  datetime
0000   0x4e 0xe9 0x11 0x07 0x06                   N....
  extra(4) 
0000   0x03 0x00 0x03 0x00                        ....
          3    0    3    0

```


### another record
#### export
```
7/7/06 17:57:02 Prime
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 17:57:02
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && PRIME_TYPE=fixed && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 23: 2006-07-07T17:57:02 0x03
  hex (1)
0000   0x03                                       .
  decimal
          3
  datetime
0000   0x42 0xf9 0x11 0x07 0x06                   B....
  extra(4) 
0000   0x03 0x00 0x03 0x00                        ....
          3    0    3    0

```


### another record
#### export
```
7/7/06 18:02:05 Prime
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 18:02:05
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: Prime
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && PRIME_TYPE=fixed && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 24: 2006-07-07T18:02:05 0x03
  hex (1)
0000   0x03                                       .
  decimal
          3
  datetime
0000   0x45 0xc2 0x12 0x07 0x06                   E....
  extra(4) 
0000   0x1e 0x00 0x60 0xd6                        ..`.
         30    0   96  214

```

### another record
#### export
```
7/7/06 18:22:32 ChangeSuspendEnable
  "ENABLE=user_suspend, ACTION_REQUESTOR=rf_diagnostic, PRE_ENABLE=null"
    0: Timestamp: 7/7/06 18:22:32
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U):
    6: BWZ Target High BG (mg/dL):
    7: BWZ Target Low BG (mg/dL):
    8: BWZ Carb Ratio (grams):
    9: BWZ Insulin Sensitivity (mg/dL):
    10: BWZ Carb Input (grams):
    11: BWZ BG Input (mg/dL):
    12: BWZ Correction Estimate (U):
    13: BWZ Food Estimate (U):
    14: BWZ Active Insulin (U):
    15: Raw-Type: ChangeSuspendEnable
    16: Raw-Values: "ENABLE=user_suspend && ACTION_REQUESTOR=rf_diagnostic && PRE_ENABLE=null"

7/7/06 18:22:51 ChangeSuspendEnable
```

hrm... not sure what happened here!?

#### decoded
```
RECORD 25: 2006-07-07T18:22:51 0x12
  hex (5)
0000   0x12 0x47 0x06 0x1f 0x00                   .G...
  decimal
         18   71    6   31    0
  datetime
0000   0x73 0xd6 0x12 0x47 0x06                   s..G.
  extra(0) None

```


### another record
#### export
```
```

#### decoded
```
```








### another record
#### export
```
```

#### decoded
```
```

