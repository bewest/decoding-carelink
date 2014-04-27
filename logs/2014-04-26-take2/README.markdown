
## manually dissecting glucose pages

#### start

```diff
********** 20140426_203842-ReadGlucoseHistory-page-0.data.hex[1-1] compared to 20140426_203842-ReadGlucoseHistory-page-0.data.hex[1] *********
21,22c21,23
< 00000140  79 79 7a 7e 82 85 87 86  01 00 00 00 00 00 00 00  |yyz~............|
< 00000150  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
---
> 00000140  79 79 7a 7e 82 85 87 86  04 0e 3a 27 50 0e 04 0e  |yyz~......:'P...|
> 00000150  3a 28 50 0e 85 04 0e 3a  29 50 0e 01 00 00 00 00  |:(P....:)P......|
> 00000160  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
24c25
```
Looks like some glucose data at the top.

> `00000140  79 79 7a 7e 82 85 87 86`

* `0x79` `*2` == `242` `2014-04-26T16:00:00 GlucoseSensorData`
* `0x79` `*2` == `242` `2014-04-26T16:05:00 GlucoseSensorData`
* `0x7a` `*2` == `244` `2014-04-26T16:10:00 GlucoseSensorData`
* `0x7e` `*2` == `252` `2014-04-26T16:15:00 GlucoseSensorData`
* `0x82` `*2` == `260` `2014-04-26T16:20:00 GlucoseSensorData`
* `0x85` `*2` == `266` `2014-04-26T16:25:00 GlucoseSensorData`
* `0x87` `*2` == `270` `2014-04-26T16:30:00 GlucoseSensorData`
* `0x86` `*2` == `268` `2014-04-26T16:35:00 GlucoseSensorData`

#### analysis
```
04 0e 3a 27 50 0e
04 0e 3a 28 50 0e
85                    GlucoseSensorData 0x85 * 2 == 266
04 0e 3a 29 50 0e
01 00 00 00 00
```

```csv
510,4/26/14,15:55:00,4/26/14 15:55:00,,,,,,,,,,,,,,,,,,,,,,,,,,,242,53.44,,GlucoseSensorData,"AMOUNT=242, ISIG=53.44, VCNTR=null, BACKFILL_INDICATOR=null",12895952933,53172285,135,Paradigm 722
511,4/26/14,16:00:00,4/26/14 16:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,242,52.62,,GlucoseSensorData,"AMOUNT=242, ISIG=52.62, VCNTR=null, BACKFILL_INDICATOR=null",12895952932,53172285,134,Paradigm 722
512,4/26/14,16:05:00,4/26/14 16:05:00,,,,,,,,,,,,,,,,,,,,,,,,,,,242,52.78,,GlucoseSensorData,"AMOUNT=242, ISIG=52.78, VCNTR=null, BACKFILL_INDICATOR=null",12895952931,53172285,133,Paradigm 722
513,4/26/14,16:10:00,4/26/14 16:10:00,,,,,,,,,,,,,,,,,,,,,,,,,,,244,54.21,,GlucoseSensorData,"AMOUNT=244, ISIG=54.21, VCNTR=null, BACKFILL_INDICATOR=null",12895952930,53172285,132,Paradigm 722
514,4/26/14,16:15:00,4/26/14 16:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,252,56.68,,GlucoseSensorData,"AMOUNT=252, ISIG=56.68, VCNTR=null, BACKFILL_INDICATOR=null",12895952929,53172285,131,Paradigm 722
515,4/26/14,16:20:00,4/26/14 16:20:00,,,,,,,,,,,,,,,,,,,,,,,,,,,260,58.91,,GlucoseSensorData,"AMOUNT=260, ISIG=58.91, VCNTR=null, BACKFILL_INDICATOR=null",12895952928,53172285,130,Paradigm 722
516,4/26/14,16:25:00,4/26/14 16:25:00,,,,,,,,,,,,,,,,,,,,,,,,,,,266,59.61,,GlucoseSensorData,"AMOUNT=266, ISIG=59.61, VCNTR=null, BACKFILL_INDICATOR=null",12895952927,53172285,129,Paradigm 722
517,4/26/14,16:30:00,4/26/14 16:30:00,,,,,,,,,,,,,,,,,,,,,,,,,,,270,59.16,,GlucoseSensorData,"AMOUNT=270, ISIG=59.16, VCNTR=null, BACKFILL_INDICATOR=null",12895952926,53172285,128,Paradigm 722
518,4/26/14,16:35:00,4/26/14 16:35:00,,,,,,,,,,,,,,,,,,,,,,,,,,,268,58.47,,GlucoseSensorData,"AMOUNT=268, ISIG=58.47, VCNTR=null, BACKFILL_INDICATOR=null",12895952925,53172285,127,Paradigm 722

522,4/26/14,16:40:00,4/26/14 16:40:00,,,,,,,,,,,,,,,,,,,,,,,,,,,266,57.41,,GlucoseSensorData,"AMOUNT=266, ISIG=57.41, VCNTR=null, BACKFILL_INDICATOR=null",12895952922,53172285,124,Paradigm 722
```

#### second run
```diff
********** 20140426_203842-ReadGlucoseHistory-page-0.data.hex[2-1] compared to 20140426_203842-ReadGlucoseHistory-page-0.data.hex[2] *********
22,23c22,24
< 00000150  3a 28 50 0e 85 04 0e 3a  29 50 0e 01 00 00 00 00  |:(P....:)P......|
< 00000160  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
---
> 00000150  3a 28 50 0e 85 04 0e 3a  29 50 0e 04 0e 3a 2d 50  |:(P....:)P...:-P|
> 00000160  0e 13 02 01 00 00 00 00  00 00 00 00 00 00 00 00  |................|
25c26
```

##### analysis

```
04 0e 3a 2d 50
0e 13 02
[01]

```

```csv

527,4/26/14,16:45:00,4/26/14 16:45:00,,,,,,,,,,,,,,,,,,,,,,,,,,,262,56.61,,GlucoseSensorData,"AMOUNT=262, ISIG=56.61, VCNTR=null, BACKFILL_INDICATOR=null",12895952919,53172285,121,Paradigm 722
530,4/26/14,16:50:00,4/26/14 16:50:00,,,,,,,,,,,,,,,,,,,,,,,,,,,262,57.45,,GlucoseSensorData,"AMOUNT=262, ISIG=57.45, VCNTR=null, BACKFILL_INDICATOR=null",12895952917,53172285,119,Paradigm 722
536,4/26/14,16:55:00,4/26/14 16:55:00,,,,,,,,,,,,,,,,,,,,,,,,,,,264,58.14,,GlucoseSensorData,"AMOUNT=264, ISIG=58.14, VCNTR=null, BACKFILL_INDICATOR=null",12895952914,53172285,116,Paradigm 722
537,4/26/14,17:00:00,4/26/14 17:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,268,59.26,,GlucoseSensorData,"AMOUNT=268, ISIG=59.26, VCNTR=null, BACKFILL_INDICATOR=null",12895952913,53172285,115,Paradigm 722
542,4/26/14,17:05:00,4/26/14 17:05:00,,,,,,,,,,,,,,,,,,,,,,,,,,,270,59.81,,GlucoseSensorData,"AMOUNT=270, ISIG=59.81, VCNTR=null, BACKFILL_INDICATOR=null",12895952910,53172285,112,Paradigm 722
543,4/26/14,17:10:00,4/26/14 17:10:00,,,,,,,,,,,,,,,,,,,,,,,,,,,272,59.28,,GlucoseSensorData,"AMOUNT=272, ISIG=59.28, VCNTR=null, BACKFILL_INDICATOR=null",12895952909,53172285,111,Paradigm 722
544,4/26/14,17:15:00,4/26/14 17:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCalFactor,CAL_FACTOR=4.359,12895952907,53172285,109,Paradigm 722
```

#### third run

```diff
********** 20140426_203842-ReadGlucoseHistory-page-0.data.hex[3-1] compared to 20140426_203842-ReadGlucoseHistory-page-0.data.hex[3] *********
23c23
< 00000160  0e 13 02 01 00 00 00 00  00 00 00 00 00 00 00 00  |................|
---
> 00000160  0e 13 02 04 0e 3a 32 50  0e 01 00 00 00 00 00 00  |.....:2P........|
```
##### data
```
04 0e 3a 32 50
0e
[01]
```

#### fourth run
```diff
********** 20140426_203842-ReadGlucoseHistory-page-0.data.hex[4-1] compared to 20140426_203842-ReadGlucoseHistory-page-0.data.hex[4] *********
23,24c23,25
< 00000160  0e 13 02 04 0e 3a 32 50  0e 01 00 00 00 00 00 00  |.....:2P........|
< 00000170  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
---
> 00000160  0e 13 83 04 0e 3a 32 50  0e 83 04 0e 3a 33 50 0e  |.....:2P....:3P.|
> 00000170  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
> 00000180  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
```
##### data

```
83                 0x83 * 2 == 262
04 0e 3a 33 50
0e
[01]
```

#### fifth run

```diff
********** 20140426_203842-ReadGlucoseHistory-page-0.data.hex[5-1] compared to 20140426_203842-ReadGlucoseHistory-page-0.data.hex[5] *********
24c24
< 00000170  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
---
> 00000170  04 0e 3a 35 50 0e 01 00  00 00 00 00 00 00 00 00  |..:5P...........|
27c27
```

```
04 0e 3a 35 50
0e
[01]
```


```csv
545,4/26/14,17:15:00,4/26/14 17:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,258,58.76,,GlucoseSensorData,"AMOUNT=258, ISIG=58.76, VCNTR=null, BACKFILL_INDICATOR=null",12895952908,53172285,110,Paradigm 722
546,4/26/14,17:20:00,4/26/14 17:20:00,,,,,,,,,,,,,,,,,,,,,,,,,,,256,58.89,,GlucoseSensorData,"AMOUNT=256, ISIG=58.89, VCNTR=null, BACKFILL_INDICATOR=null",12895952906,53172285,108,Paradigm 722
547,4/26/14,17:25:00,4/26/14 17:25:00,,,,,,,,,,,,,,,,,,,,,,,,,,,254,58.15,,GlucoseSensorData,"AMOUNT=254, ISIG=58.15, VCNTR=null, BACKFILL_INDICATOR=null",12895952905,53172285,107,Paradigm 722
548,4/26/14,17:30:00,4/26/14 17:30:00,,,,,,,,,,,,,,,,,,,,,,,,,,,250,56.14,,GlucoseSensorData,"AMOUNT=250, ISIG=56.14, VCNTR=null, BACKFILL_INDICATOR=null",12895952904,53172285,106,Paradigm 722
549,4/26/14,17:35:00,4/26/14 17:35:00,,,,,,,,,,,,,,,,,,,,,,,,,,,244,55.13,,GlucoseSensorData,"AMOUNT=244, ISIG=55.13, VCNTR=null, BACKFILL_INDICATOR=null",12895952903,53172285,105,Paradigm 722
550,4/26/14,17:40:00,4/26/14 17:40:00,,,,,,,,,,,,,,,,,,,,,,,,,,,240,54.1,,GlucoseSensorData,"AMOUNT=240, ISIG=54.1, VCNTR=null, BACKFILL_INDICATOR=null",12895952902,53172285,104,Paradigm 722
551,4/26/14,17:45:00,4/26/14 17:45:00,,,,,,,,,,,,,,,,,,,,,,,,,,,236,52.98,,GlucoseSensorData,"AMOUNT=236, ISIG=52.98, VCNTR=null, BACKFILL_INDICATOR=null",12895952901,53172285,103,Paradigm 722
552,4/26/14,17:50:00,4/26/14 17:50:00,,,,,,,,,,,,,,,,,,,,,,,,,,,230,52.03,,GlucoseSensorData,"AMOUNT=230, ISIG=52.03, VCNTR=null, BACKFILL_INDICATOR=null",12895952900,53172285,102,Paradigm 722
554,4/26/14,17:55:00,4/26/14 17:55:00,,,,,,,,,,,,,,,,,,,,,,,,,,,226,51.19,,GlucoseSensorData,"AMOUNT=226, ISIG=51.19, VCNTR=null, BACKFILL_INDICATOR=null",12895952899,53172285,101,Paradigm 722
555,4/26/14,18:00:00,4/26/14 18:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,224,50.88,,GlucoseSensorData,"AMOUNT=224, ISIG=50.88, VCNTR=null, BACKFILL_INDICATOR=null",12895952898,53172285,100,Paradigm 722
556,4/26/14,18:05:00,4/26/14 18:05:00,,,,,,,,,,,,,,,,,,,,,,,,,,,226,52.54,,GlucoseSensorData,"AMOUNT=226, ISIG=52.54, VCNTR=null, BACKFILL_INDICATOR=null",12895952897,53172285,99,Paradigm 722
557,4/26/14,18:10:00,4/26/14 18:10:00,,,,,,,,,,,,,,,,,,,,,,,,,,,234,55.8,,GlucoseSensorData,"AMOUNT=234, ISIG=55.8, VCNTR=null, BACKFILL_INDICATOR=null",12895952896,53172285,98,Paradigm 722
558,4/26/14,18:15:00,4/26/14 18:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorTimestamp,TIMESTAMP_TYPE=last_rf,12895952894,53172285,96,Paradigm 722
559,4/26/14,18:15:00,4/26/14 18:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,238,55.85,,GlucoseSensorData,"AMOUNT=238, ISIG=55.85, VCNTR=null, BACKFILL_INDICATOR=null",12895952895,53172285,97,Paradigm 722
```
