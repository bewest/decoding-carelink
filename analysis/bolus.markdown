
# what do bolus records look like?


#### export
```

7/1/06 08:23:47 BolusNormal
  "AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3,
  ACTION_REQUESTOR=pump, ENABLE=false, IS_DUAL_COMPONENT=false,
  UNABSORBED_INSULIN_TOTAL=null"
    0: Timestamp: 7/1/06 08:23:47
    1: Bolus Type: Normal
    2: Bolus Volume Selected (U): 0.3
    3: Bolus Volume Delivered (U): 0.3
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
    15: Raw-Type: BolusNormal
    16: Raw-Values: "AMOUNT=0.3 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.3 && ACTION_REQUESTOR=pump && ENABLE=false && IS_DUAL_COMPONENT=false && UNABSORBED_INSULIN_TOTAL=null"

7/1/06 08:23:47 BolusWizardBolusEstimate
  "BG_INPUT=100, BG_UNITS=mg dl, CARB_INPUT=3, CARB_UNITS=grams,
  CARB_RATIO=10, INSULIN_SENSITIVITY=50, BG_TARGET_LOW=100,
  BG_TARGET_HIGH=100, BOLUS_ESTIMATE=0.3, CORRECTION_ESTIMATE=0,
  FOOD_ESTIMATE=0.3, UNABSORBED_INSULIN_TOTAL=0, UNABSORBED_INSULIN_COUNT=0,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/1/06 08:23:47
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U): 0.3
    6: BWZ Target High BG (mg/dL): 100
    7: BWZ Target Low BG (mg/dL): 100
    8: BWZ Carb Ratio (grams): 10
    9: BWZ Insulin Sensitivity (mg/dL): 50
    10: BWZ Carb Input (grams): 3
    11: BWZ BG Input (mg/dL): 100
    12: BWZ Correction Estimate (U): 0
    13: BWZ Food Estimate (U): 0.3
    14: BWZ Active Insulin (U): 0.0
    15: Raw-Type: BolusWizardBolusEstimate
    16: Raw-Values: "BG_INPUT=100 && BG_UNITS=mg dl && CARB_INPUT=3 && CARB_UNITS=grams && CARB_RATIO=10 && INSULIN_SENSITIVITY=50 && BG_TARGET_LOW=100 && BG_TARGET_HIGH=100 && BOLUS_ESTIMATE=0.3 && CORRECTION_ESTIMATE=0 && FOOD_ESTIMATE=0.3 && UNABSORBED_INSULIN_TOTAL=0 && UNABSORBED_INSULIN_COUNT=0 && ACTION_REQUESTOR=pump"

```

#### decoded
```
RECORD 0: 2006-07-01T08:23:47 0x5b
  hex (2)
0000   0x5b 0x64                                  [d
  decimal
         91  100
  datetime
0000   0x6f 0xd7 0x08 0x01 0x06                   o....
  extra(22) 
0000   0x03 0x50 0x0a 0x32 0x64 0x00 0x03 0x00    .P.2d...
0008   0x00 0x00 0x00 0x03 0x64 0x01 0x03 0x03    ....d...
0010   0x00 0x6f 0xd7 0x28 0x01 0x06              .o.(..
          3   80   10   50  100    0    3    0
          0    0    0    3  100    1    3    3
          0  111  215   40    1    6
```

### RECORD 1: 2006-07-01T08:24:43 0x5b
#### export
```
7/1/06 08:24:43 BolusWizardBolusEstimate
  "BG_INPUT=103, BG_UNITS=mg dl, CARB_INPUT=7, CARB_UNITS=grams,
  CARB_RATIO=10, INSULIN_SENSITIVITY=50, BG_TARGET_LOW=100,
  BG_TARGET_HIGH=100, BOLUS_ESTIMATE=0.7, CORRECTION_ESTIMATE=0,
  FOOD_ESTIMATE=0.7, UNABSORBED_INSULIN_TOTAL=0.3,
  UNABSORBED_INSULIN_COUNT=1, ACTION_REQUESTOR=pump"
    0: Timestamp: 7/1/06 08:24:43
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U): 0.7
    6: BWZ Target High BG (mg/dL): 100
    7: BWZ Target Low BG (mg/dL): 100
    8: BWZ Carb Ratio (grams): 10
    9: BWZ Insulin Sensitivity (mg/dL): 50
    10: BWZ Carb Input (grams): 7
    11: BWZ BG Input (mg/dL): 103
    12: BWZ Correction Estimate (U): 0
    13: BWZ Food Estimate (U): 0.7
    14: BWZ Active Insulin (U): 0.3
    15: Raw-Type: BolusWizardBolusEstimate
    16: Raw-Values: "BG_INPUT=103 && BG_UNITS=mg dl && CARB_INPUT=7 && CARB_UNITS=grams && CARB_RATIO=10 && INSULIN_SENSITIVITY=50 && BG_TARGET_LOW=100 && BG_TARGET_HIGH=100 && BOLUS_ESTIMATE=0.7 && CORRECTION_ESTIMATE=0 && FOOD_ESTIMATE=0.7 && UNABSORBED_INSULIN_TOTAL=0.3 && UNABSORBED_INSULIN_COUNT=1 && ACTION_REQUESTOR=pump"

7/1/06 08:24:43 UnabsorbedInsulin
  "BOLUS_ESTIMATE_DATUM=9773719100, INDEX=0, AMOUNT=0.3, RECORD_AGE=1,
  INSULIN_TYPE=null, INSULIN_ACTION_CURVE=300"
    0: Timestamp: 7/1/06 08:24:43
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
    15: Raw-Type: UnabsorbedInsulin
    16: Raw-Values: "BOLUS_ESTIMATE_DATUM=9773719100 && INDEX=0 && AMOUNT=0.3 && RECORD_AGE=1 && INSULIN_TYPE=null && INSULIN_ACTION_CURVE=300"

7/1/06 08:24:43 BolusNormal
  "AMOUNT=0.7, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.7,
  ACTION_REQUESTOR=pump, ENABLE=false, IS_DUAL_COMPONENT=false,
  UNABSORBED_INSULIN_TOTAL=null"
    0: Timestamp: 7/1/06 08:24:43
    1: Bolus Type: Normal
    2: Bolus Volume Selected (U): 0.7
    3: Bolus Volume Delivered (U): 0.7
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
    15: Raw-Type: BolusNormal
    16: Raw-Values: "AMOUNT=0.7 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.7 && ACTION_REQUESTOR=pump && ENABLE=false && IS_DUAL_COMPONENT=false && UNABSORBED_INSULIN_TOTAL=null"
```

#### decoded
```
RECORD 1: 2006-07-01T08:24:43 0x5b
  hex (2)
0000   0x5b 0x67                                  [g
  decimal
         91  103
  datetime
0000   0x6b 0xd8 0x08 0x01 0x06                   k....
  extra(22) 
0000   0x07 0x50 0x0a 0x32 0x64 0x00 0x07 0x00    .P.2d...
0008   0x00 0x03 0x00 0x07 0x64 0x5c 0x05 0x0c    ....d\..
0010   0x01 0x44 0x01 0x07 0x07 0x00              .D....
          7   80   10   50  100    0    7    0
          0    3    0    7  100   92    5   12
          1   68    1    7    7    0
```

### another record
#### export
```
7/1/06 08:26:55 BolusWizardBolusEstimate
  "BG_INPUT=599, BG_UNITS=mg dl, CARB_INPUT=1, CARB_UNITS=grams,
  CARB_RATIO=10, INSULIN_SENSITIVITY=50, BG_TARGET_LOW=100,
  BG_TARGET_HIGH=100, BOLUS_ESTIMATE=9, CORRECTION_ESTIMATE=9.9,
  FOOD_ESTIMATE=0.1, UNABSORBED_INSULIN_TOTAL=1, UNABSORBED_INSULIN_COUNT=1,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/1/06 08:26:55
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U): 9.0
    6: BWZ Target High BG (mg/dL): 100
    7: BWZ Target Low BG (mg/dL): 100
    8: BWZ Carb Ratio (grams): 10
    9: BWZ Insulin Sensitivity (mg/dL): 50
    10: BWZ Carb Input (grams): 1
    11: BWZ BG Input (mg/dL): 599
    12: BWZ Correction Estimate (U): 9.9
    13: BWZ Food Estimate (U): 0.1
    14: BWZ Active Insulin (U): 1.0
    15: Raw-Type: BolusWizardBolusEstimate
    16: Raw-Values: "BG_INPUT=599 && BG_UNITS=mg dl && CARB_INPUT=1 && CARB_UNITS=grams && CARB_RATIO=10 && INSULIN_SENSITIVITY=50 && BG_TARGET_LOW=100 && BG_TARGET_HIGH=100 && BOLUS_ESTIMATE=9 && CORRECTION_ESTIMATE=9.9 && FOOD_ESTIMATE=0.1 && UNABSORBED_INSULIN_TOTAL=1 && UNABSORBED_INSULIN_COUNT=1 && ACTION_REQUESTOR=pump"

7/1/06 08:26:55 BolusNormal
  "AMOUNT=9, CONCENTRATION=null, PROGRAMMED_AMOUNT=9, ACTION_REQUESTOR=pump,
  ENABLE=false, IS_DUAL_COMPONENT=false, UNABSORBED_INSULIN_TOTAL=null"
    0: Timestamp: 7/1/06 08:26:55
    1: Bolus Type: Normal
    2: Bolus Volume Selected (U): 9.0
    3: Bolus Volume Delivered (U): 9.0
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
    15: Raw-Type: BolusNormal
    16: Raw-Values: "AMOUNT=9 && CONCENTRATION=null && PROGRAMMED_AMOUNT=9 && ACTION_REQUESTOR=pump && ENABLE=false && IS_DUAL_COMPONENT=false && UNABSORBED_INSULIN_TOTAL=null"

7/1/06 08:26:55 UnabsorbedInsulin
  "BOLUS_ESTIMATE_DATUM=9773719097, INDEX=0, AMOUNT=1, RECORD_AGE=3,
  INSULIN_TYPE=null, INSULIN_ACTION_CURVE=300"
    0: Timestamp: 7/1/06 08:26:55
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
    15: Raw-Type: UnabsorbedInsulin
    16: Raw-Values: "BOLUS_ESTIMATE_DATUM=9773719097 && INDEX=0 && AMOUNT=1 && RECORD_AGE=3 && INSULIN_TYPE=null && INSULIN_ACTION_CURVE=300"

```

#### decoded
pretty sure this one is wrong/ has too much data.
```
RECORD 2: 2006-07-01T08:26:55 0x6b
  hex (7)
0000   0x6b 0xd8 0x28 0x01 0x06 0x5b 0x57         k.(..[W
  decimal
        107  216   40    1    6   91   87
  datetime
0000   0x77 0xda 0x08 0x01 0x06                   w....
  extra(27) 
0000   0x01 0x52 0x0a 0x32 0x64 0x63 0x01 0x00    .R.2dc..
0008   0x00 0x0a 0x00 0x5a 0x64 0x5c 0x05 0x28    ...Zd\.(
0010   0x03 0x44 0x01 0x5a 0x5a 0x00 0x77 0xda    .D.ZZ.w.
0018   0x28 0x01 0x06                             (..
          1   82   10   50  100   99    1    0
          0   10    0   90  100   92    5   40
          3   68    1   90   90    0  119  218
         40    1    6

```


### RECORD 16: 2006-07-07T15:05:03 0x5b
#### export
```
7/7/06 15:05:03 BolusWizardBolusEstimate
  "BG_INPUT=117, BG_UNITS=mg dl, CARB_INPUT=3, CARB_UNITS=grams,
  CARB_RATIO=10, INSULIN_SENSITIVITY=50, BG_TARGET_LOW=100,
  BG_TARGET_HIGH=100, BOLUS_ESTIMATE=0.6, CORRECTION_ESTIMATE=0.3,
  FOOD_ESTIMATE=0.3, UNABSORBED_INSULIN_TOTAL=0, UNABSORBED_INSULIN_COUNT=0,
  ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 15:05:03
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U): 0.6
    6: BWZ Target High BG (mg/dL): 100
    7: BWZ Target Low BG (mg/dL): 100
    8: BWZ Carb Ratio (grams): 10
    9: BWZ Insulin Sensitivity (mg/dL): 50
    10: BWZ Carb Input (grams): 3
    11: BWZ BG Input (mg/dL): 117
    12: BWZ Correction Estimate (U): 0.3
    13: BWZ Food Estimate (U): 0.3
    14: BWZ Active Insulin (U): 0.0
    15: Raw-Type: BolusWizardBolusEstimate
    16: Raw-Values: "BG_INPUT=117 && BG_UNITS=mg dl && CARB_INPUT=3 && CARB_UNITS=grams && CARB_RATIO=10 && INSULIN_SENSITIVITY=50 && BG_TARGET_LOW=100 && BG_TARGET_HIGH=100 && BOLUS_ESTIMATE=0.6 && CORRECTION_ESTIMATE=0.3 && FOOD_ESTIMATE=0.3 && UNABSORBED_INSULIN_TOTAL=0 && UNABSORBED_INSULIN_COUNT=0 && ACTION_REQUESTOR=pump"

7/7/06 15:05:03 BolusNormal
  "AMOUNT=0.6, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.6,
  ACTION_REQUESTOR=pump, ENABLE=false, IS_DUAL_COMPONENT=false,
  UNABSORBED_INSULIN_TOTAL=null"
    0: Timestamp: 7/7/06 15:05:03
    1: Bolus Type: Normal
    2: Bolus Volume Selected (U): 0.6
    3: Bolus Volume Delivered (U): 0.6
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
    15: Raw-Type: BolusNormal
    16: Raw-Values: "AMOUNT=0.6 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.6 && ACTION_REQUESTOR=pump && ENABLE=false && IS_DUAL_COMPONENT=false && UNABSORBED_INSULIN_TOTAL=null"

```

#### decoded
```
RECORD 16: 2006-07-07T15:05:03 0x5b
  hex (2)
0000   0x5b 0x75                                  [u
  decimal
         91  117
  datetime
0000   0x43 0xc5 0x0f 0x07 0x06                   C....
  extra(22) 
0000   0x03 0x50 0x0a 0x32 0x64 0x03 0x03 0x00    .P.2d...
0008   0x00 0x00 0x00 0x06 0x64 0x01 0x06 0x06    ....d...
0010   0x00 0x43 0xc5 0x2f 0x07 0x06              .C./..
          3   80   10   50  100    3    3    0
          0    0    0    6  100    1    6    6
          0   67  197   47    7    6

```

### another record
#### export
```
7/7/06 16:14:05 UnabsorbedInsulin
  "BOLUS_ESTIMATE_DATUM=9799981764, INDEX=0, AMOUNT=0.6, RECORD_AGE=71,
  INSULIN_TYPE=null, INSULIN_ACTION_CURVE=300"
    0: Timestamp: 7/7/06 16:14:05
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
    15: Raw-Type: UnabsorbedInsulin
    16: Raw-Values: "BOLUS_ESTIMATE_DATUM=9799981764 && INDEX=0 && AMOUNT=0.6 && RECORD_AGE=71 && INSULIN_TYPE=null && INSULIN_ACTION_CURVE=300"

7/7/06 16:14:05 BolusWizardBolusEstimate
  "BG_INPUT=117, BG_UNITS=mg dl, CARB_INPUT=6, CARB_UNITS=grams,
  CARB_RATIO=10, INSULIN_SENSITIVITY=50, BG_TARGET_LOW=100,
  BG_TARGET_HIGH=100, BOLUS_ESTIMATE=0.6, CORRECTION_ESTIMATE=0.3,
  FOOD_ESTIMATE=0.6, UNABSORBED_INSULIN_TOTAL=0.5,
  UNABSORBED_INSULIN_COUNT=1, ACTION_REQUESTOR=pump"
    0: Timestamp: 7/7/06 16:14:05
    1: Bolus Type:
    2: Bolus Volume Selected (U):
    3: Bolus Volume Delivered (U):
    4: Programmed Bolus Duration (hh:mm:ss):
    5: BWZ Estimate (U): 0.6
    6: BWZ Target High BG (mg/dL): 100
    7: BWZ Target Low BG (mg/dL): 100
    8: BWZ Carb Ratio (grams): 10
    9: BWZ Insulin Sensitivity (mg/dL): 50
    10: BWZ Carb Input (grams): 6
    11: BWZ BG Input (mg/dL): 117
    12: BWZ Correction Estimate (U): 0.3
    13: BWZ Food Estimate (U): 0.6
    14: BWZ Active Insulin (U): 0.5
    15: Raw-Type: BolusWizardBolusEstimate
    16: Raw-Values: "BG_INPUT=117 && BG_UNITS=mg dl && CARB_INPUT=6 && CARB_UNITS=grams && CARB_RATIO=10 && INSULIN_SENSITIVITY=50 && BG_TARGET_LOW=100 && BG_TARGET_HIGH=100 && BOLUS_ESTIMATE=0.6 && CORRECTION_ESTIMATE=0.3 && FOOD_ESTIMATE=0.6 && UNABSORBED_INSULIN_TOTAL=0.5 && UNABSORBED_INSULIN_COUNT=1 && ACTION_REQUESTOR=pump"

7/7/06 16:14:05 BolusNormal
  "AMOUNT=0.6, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.6,
  ACTION_REQUESTOR=pump, ENABLE=false, IS_DUAL_COMPONENT=false,
  UNABSORBED_INSULIN_TOTAL=null"
    0: Timestamp: 7/7/06 16:14:05
    1: Bolus Type: Normal
    2: Bolus Volume Selected (U): 0.6
    3: Bolus Volume Delivered (U): 0.6
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
    15: Raw-Type: BolusNormal
    16: Raw-Values: "AMOUNT=0.6 && CONCENTRATION=null && PROGRAMMED_AMOUNT=0.6 && ACTION_REQUESTOR=pump && ENABLE=false && IS_DUAL_COMPONENT=false && UNABSORBED_INSULIN_TOTAL=null"

7/7/06 16:47:57 Rewind
[...]

```

#### decoded
```
RECORD 17: 2006-07-07T16:14:05 0x5b
  hex (2)
0000   0x5b 0x75                                  [u
  decimal
         91  117
  datetime
0000   0x45 0xce 0x10 0x07 0x06                   E....
  extra(22) 
0000   0x06 0x50 0x0a 0x32 0x64 0x03 0x06 0x00    .P.2d...
0008   0x00 0x05 0x00 0x06 0x64 0x5c 0x05 0x18    ....d\..
0010   0x47 0x44 0x01 0x06 0x06 0x00              GD....
          6   80   10   50  100    3    6    0
          0    5    0    6  100   92    5   24
         71   68    1    6    6    0

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

```





### another record
#### export
```
```

#### decoded
```
```

