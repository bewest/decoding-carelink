
### @erobinson ran several experiments

We expect to see timestamps on `2014-04-26` between `8am` and `11am.`

```
first consecutive pages were read to get a good baseline
updated the time on the RPi - off by timezone :(
8:10am (ish) turned the sensor off and then back on, after a minute was prompted for a meter reading and entered one
tried unplugging the carelink stick but doing so caused the RPi to fail (not able to issue any bash commands, and errors saying the system is read only.. no idea)
8:19 - download was sucessful
8:20 - stopped the sensor and restarted, did not enter meter bg
8:22 - sucessful download
8:23 - metered 231 and 231 (the first one may have been something else around 230)
8:24 - another download

```

Here are the pages he captured:

```bash
.
├── 01-glucose.diff
├── 02-glucose.diff
├── 03-glucose.diff
├── 04-glucose.diff
├── 05-glucose.diff
├── 06-glucose.diff
├── 07-glucose.diff
├── 20140426_114037-ReadGlucoseHistory-page-0.data
├── 20140426_114037-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_114037-ReadISIGHistory-page-0.data
├── 20140426_114607-ReadGlucoseHistory-page-0.data
├── 20140426_114607-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_114607-ReadISIGHistory-page-0.data
├── 20140426_115239-ReadGlucoseHistory-page-0.data
├── 20140426_115239-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_115239-ReadISIGHistory-page-0.data
├── 20140426_115809-ReadGlucoseHistory-page-0.data
├── 20140426_115809-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_115809-ReadISIGHistory-page-0.data
├── 20140426_120339-ReadGlucoseHistory-page-0.data
├── 20140426_120339-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_120339-ReadISIGHistory-page-0.data
├── 20140426_121924-ReadGlucoseHistory-page-0.data
├── 20140426_121924-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_121924-ReadISIGHistory-page-0.data
├── 20140426_122227-ReadGlucoseHistory-page-0.data
├── 20140426_122227-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_122227-ReadISIGHistory-page-0.data
├── 20140426_122548-ReadGlucoseHistory-page-0.data
├── 20140426_122548-ReadGlucoseHistory-page-0.data.hexdump
├── 20140426_122548-ReadISIGHistory-page-0.data
├── README.markdown
└── readme.txt

0 directories, 33 files
```

We used: `for f in   *ReadGlucose*; do echo $f; xxd -g 1 $f | tee $f.hexdump ; done` to create the hexdumps.

Then this to create the diffs:
```bash
$  diff -u 20140426_114037-ReadGlucoseHistory-page-0.data.hexdump 20140426_114607-ReadGlucoseHistory-page-0.data.hexdump > 01-glucose.diff
$  ls *.hexdump
$  diff -u  20140426_114607-ReadGlucoseHistory-page-0.data.hexdump  20140426_115239-ReadGlucoseHistory-page-0.data.hexdump > 02-glucose.diff 
$  diff -u    20140426_115239-ReadGlucoseHistory-page-0.data.hexdump   20140426_115809-ReadGlucoseHistory-page-0.data.hexdump > 03-glucose.diff
$  diff -u       20140426_115809-ReadGlucoseHistory-page-0.data.hexdump  20140426_120339-ReadGlucoseHistory-page-0.data.hexdump > 04-glucose.diff
$  diff -u  20140426_120339-ReadGlucoseHistory-page-0.data.hexdump 20140426_121924-ReadGlucoseHistory-page-0.data.hexdump > 05-glucose.diff
$  diff -u  20140426_121924-ReadGlucoseHistory-page-0.data.hexdump 20140426_122227-ReadGlucoseHistory-page-0.data.hexdump > 06-glucose.diff
$  diff -u   20140426_122227-ReadGlucoseHistory-page-0.data.hexdump  20140426_122548-ReadGlucoseHistory-page-0.data.hexdump > 07-glucose.diff

```

Here are some interesting results:

###### Individual glucose records recorded
```diff
--- 20140426_114037-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.755432453 -0700
+++ 20140426_114607-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.755432453 -0700
@@ -5,7 +5,7 @@
 0000040: 5e 5a 5d 67 6e 71 72 73 73 74 74 73 74 74 74 74  ^Z]gnqrssttstttt
 0000050: 73 73 73 71 6d 69 66 65 6b 70 72 71 70 70 6f 70  sssqmifekprqppop
 0000060: 71 73 70 6c 68 65 63 62 61 60 5f 61 63 69 6d 6c  qsplhecba`_aciml
-0000070: 69 68 6c 13 72 74 74 76 01 00 00 00 00 00 00 00  ihl.rttv........
+0000070: 69 68 6c 13 72 74 74 76 77 01 00 00 00 00 00 00  ihl.rttvw.......
 0000080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 0000090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 75 7a  ..............uz
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 cd bc  ................
```
Theory is that these glucose records were added:
* `0x77 * 2` = `238`

```diff
--- 20140426_114607-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.755432453 -0700
+++ 20140426_115239-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.755432453 -0700
@@ -5,7 +5,7 @@
 0000040: 5e 5a 5d 67 6e 71 72 73 73 74 74 73 74 74 74 74  ^Z]gnqrssttstttt
 0000050: 73 73 73 71 6d 69 66 65 6b 70 72 71 70 70 6f 70  sssqmifekprqppop
 0000060: 71 73 70 6c 68 65 63 62 61 60 5f 61 63 69 6d 6c  qsplhecba`_aciml
-0000070: 69 68 6c 13 72 74 74 76 77 01 00 00 00 00 00 00  ihl.rttvw.......
+0000070: 69 68 6c 13 72 74 74 76 77 76 01 00 00 00 00 00  ihl.rttvwv......
 0000080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 0000090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 cd bc  ................
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 7f e2  ................
```
Theory is that these glucose records were added:
* `0x76 * 2` = `236`


```diff
--- 20140426_115239-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.755432453 -0700
+++ 20140426_115809-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.759432453 -0700
@@ -5,7 +5,7 @@
 0000040: 5e 5a 5d 67 6e 71 72 73 73 74 74 73 74 74 74 74  ^Z]gnqrssttstttt
 0000050: 73 73 73 71 6d 69 66 65 6b 70 72 71 70 70 6f 70  sssqmifekprqppop
 0000060: 71 73 70 6c 68 65 63 62 61 60 5f 61 63 69 6d 6c  qsplhecba`_aciml
-0000070: 69 68 6c 13 72 74 74 76 77 76 01 00 00 00 00 00  ihl.rttvwv......
+0000070: 69 68 6c 13 72 74 74 76 77 76 76 01 00 00 00 00  ihl.rttvwvv.....
 0000080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 0000090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 7f e2  ................
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 e8 a3  ................
```
Theory is that these glucose records were added:
* `0x76 * 2` = `236`


None of these look like our four byte dates yet, just individual glucose
records being appended.

```diff
--- 20140426_115809-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.759432453 -0700
+++ 20140426_120339-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.759432453 -0700
@@ -5,7 +5,7 @@
 0000040: 5e 5a 5d 67 6e 71 72 73 73 74 74 73 74 74 74 74  ^Z]gnqrssttstttt
 0000050: 73 73 73 71 6d 69 66 65 6b 70 72 71 70 70 6f 70  sssqmifekprqppop
 0000060: 71 73 70 6c 68 65 63 62 61 60 5f 61 63 69 6d 6c  qsplhecba`_aciml
-0000070: 69 68 6c 13 72 74 74 76 77 76 76 01 00 00 00 00  ihl.rttvwvv.....
+0000070: 69 68 6c 13 72 74 74 76 77 76 76 7a 01 00 00 00  ihl.rttvwvvz....
 0000080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 0000090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 e8 a3  ................
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 15 27  ...............'
```
Theory is that these glucose records were added:
* `0x7A * 2` = `244`

The above records seem to line up with this segment of csv data:
```csv
314,4/26/14,07:45:00,4/26/14 07:45:00,,,,,,,,,,,,,,,,,,,,,,,,,,,238,44.56,,GlucoseSensorData,"AMOUNT=238, ISIG=44.56, VCNTR=null, BACKFILL_INDICATOR=null",12895559834,53172199,260,Paradigm 722
315,4/26/14,07:50:00,4/26/14 07:50:00,,,,,,,,,,,,,,,,,,,,,,,,,,,236,43.31,,GlucoseSensorData,"AMOUNT=236, ISIG=43.31, VCNTR=null, BACKFILL_INDICATOR=null",12895559833,53172199,259,Paradigm 722
316,4/26/14,07:55:00,4/26/14 07:55:00,,,,,,,,,,,,,,,,,,,,,,,,,,,236,44.19,,GlucoseSensorData,"AMOUNT=236, ISIG=44.19, VCNTR=null, BACKFILL_INDICATOR=null",12895559832,53172199,258,Paradigm 722
317,4/26/14,08:00:00,4/26/14 08:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,244,46.72,,GlucoseSensorData,"AMOUNT=244, ISIG=46.72, VCNTR=null, BACKFILL_INDICATOR=null",12895559831,53172199,257,Paradigm 722

```

###### some dates

```diff
--- 20140426_120339-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.759432453 -0700
+++ 20140426_121924-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.759432453 -0700
@@ -5,9 +5,9 @@
 0000040: 5e 5a 5d 67 6e 71 72 73 73 74 74 73 74 74 74 74  ^Z]gnqrssttstttt
 0000050: 73 73 73 71 6d 69 66 65 6b 70 72 71 70 70 6f 70  sssqmifekprqppop
 0000060: 71 73 70 6c 68 65 63 62 61 60 5f 61 63 69 6d 6c  qsplhecba`_aciml
-0000070: 69 68 6c 13 72 74 74 76 77 76 76 7a 01 00 00 00  ihl.rttvwvvz....
-0000080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-0000090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
+0000070: 69 68 6c 13 72 74 74 76 77 76 76 7a 7e 0e 5a 05  ihl.rttvwvvz~.Z.
+0000080: 48 08 0e 1a 0a 48 0b 0e 3a 0a 48 0b 0e 3a 0b 48  H....H..:.H..:.H
+0000090: 0d 00 03 e7 0e 1a 0c 48 0e 13 02 01 00 00 00 00  .......H........
 00000a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 15 27  ...............'
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 f8 8f  ................
```
This chunk was added:
```diff
+0000070: 69 68 6c 13 72 74 74 76 77 76 76 7a
+...                                          7e 0e 5a 05  ihl.rttvwvvz~.Z.
+0000080: 48 08 0e 1a 0a 48 0b 0e 3a 0a 48 0b 0e 3a 0b 48  H....H..:.H..:.H
+0000090: 0d 00 03 e7 0e 1a 0c 48 0e 13 02 01 00 00 00 00  .......H........
```
Theory is that these glucose records were added:
* `0x7E * 2` = `252`

```csv
318,4/26/14,08:05:00,4/26/14 08:05:00,,,,,,,,,,,,,,,,,,,,,,,,,,,252,48.55,,GlucoseSensorData,"AMOUNT=252, ISIG=48.55, VCNTR=null, BACKFILL_INDICATOR=null",12895559830,53172199,256,Paradigm 722
319,4/26/14,08:05:00,4/26/14 08:05:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorTimestamp,TIMESTAMP_TYPE=gap,12895559829,53172199,255,Paradigm 722
320,4/26/14,08:10:00,4/26/14 08:10:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorStatus,STATUS_TYPE=off,12895559828,53172199,254,Paradigm 722
321,4/26/14,08:10:00,4/26/14 08:10:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCal,"CAL_TYPE=meter_bg_now, ISIG=49.52, VCNTR=null, BACKFILL_INDICATOR=null",12895559825,53172199,251,Paradigm 722
322,4/26/14,08:10:00,4/26/14 08:10:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorStatus,STATUS_TYPE=on,12895559827,53172199,253,Paradigm 722
329,4/26/14,08:11:00,4/26/14 08:11:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorSync,SYNC_TYPE=new,12895559826,53172199,252,Paradigm 722
```

Theory is that records with the following timestamps were recorded:

###### probably `2014-04-26 08:05:00`

###### probably `2014-04-26 08:10:00`
```
0e 5a
05 48 08 0e [1a]
0a 48 0b 0e [3a]
0a 48 0b 0e [3a 0b 48 0d 00 03 e7 0e]
1a 0c 48 0e [13 02 01]
```
```csv
333,4/26/14,08:15:00,4/26/14 08:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorTimestamp,TIMESTAMP_TYPE=gap,12895559822,53172199,248,Paradigm 722
```


```diff
--- 20140426_121924-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.759432453 -0700
+++ 20140426_122227-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.763432454 -0700
@@ -7,9 +7,9 @@
 0000060: 71 73 70 6c 68 65 63 62 61 60 5f 61 63 69 6d 6c  qsplhecba`_aciml
 0000070: 69 68 6c 13 72 74 74 76 77 76 76 7a 7e 0e 5a 05  ihl.rttvwvvz~.Z.
 0000080: 48 08 0e 1a 0a 48 0b 0e 3a 0a 48 0b 0e 3a 0b 48  H....H..:.H..:.H
-0000090: 0d 00 03 e7 0e 1a 0c 48 0e 13 02 01 00 00 00 00  .......H........
-00000a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00000b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
+0000090: 0d 00 03 e7 0e 1a 0c 48 0e 13 02 0e 5a 0f 48 08  .......H....Z.H.
+00000a0: 0e 1a 14 48 0b 0e 3a 14 48 0b 0e 3a 14 48 0d 01  ...H..:.H..:.H..
+00000b0: 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 f8 8f  ................
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 63 0c  ..............c.
```
new data
```
                                           0e 5a 0f 48 08  .......H....Z.H.
00000a0: 0e 1a 14 48 0b 0e 3a 14 48 0b 0e 3a 14 48 0d 01  ...H..:.H..:.H..
00000b0: 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
```
```csv
334,4/26/14,08:15:00,4/26/14 08:15:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorWeakSignal,,12895559823,53172199,249,Paradigm 722
335,4/26/14,08:20:00,4/26/14 08:20:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCal,"CAL_TYPE=waiting, ISIG=50.36, VCNTR=null, BACKFILL_INDICATOR=null",12895559818,53172199,244,Paradigm 722
```

###### probably `2014-04-26T08:20:00`

```
0f 48 08 0e
[1a] 14 48 0b 0e
[3a] 14 48 0b 0e
```

```csv
336,4/26/14,08:20:00,4/26/14 08:20:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorSync,SYNC_TYPE=new,12895559819,53172199,245,Paradigm 722
337,4/26/14,08:20:00,4/26/14 08:20:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorStatus,STATUS_TYPE=on,12895559820,53172199,246,Paradigm 722
338,4/26/14,08:20:00,4/26/14 08:20:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorStatus,STATUS_TYPE=off,12895559821,53172199,247,Paradigm 722
```

###### two dates
```diff
--- 20140426_122227-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.763432454 -0700
+++ 20140426_122548-ReadGlucoseHistory-page-0.data.hexdump	2014-04-26 12:56:12.763432454 -0700
@@ -9,7 +9,7 @@
 0000080: 48 08 0e 1a 0a 48 0b 0e 3a 0a 48 0b 0e 3a 0b 48  H....H..:.H..:.H
 0000090: 0d 00 03 e7 0e 1a 0c 48 0e 13 02 0e 5a 0f 48 08  .......H....Z.H.
 00000a0: 0e 1a 14 48 0b 0e 3a 14 48 0b 0e 3a 14 48 0d 01  ...H..:.H..:.H..
-00000b0: 03 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
+00000b0: 03 e6 0e 1a 17 48 0e e7 0e 1a 19 48 0e 01 03 01  .....H.....H....
 00000c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00000e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
@@ -61,4 +61,4 @@
 00003c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
 00003e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
-00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 63 0c  ..............c.
+00003f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 95 cd  ................
```


```
+00000b0: 03 e6 0e 1a 17 48 0e e7 0e 1a 19 48 0e 01 03 01  .....H.....H....
[01] 03 e6 0e

1a 17 48 0e
e7 0e
1a 19 48 0e
01 03 01
```

```csv
341,4/26/14,08:25:00,4/26/14 08:25:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCal,"CAL_TYPE=waiting, ISIG=50.54, VCNTR=null, BACKFILL_INDICATOR=null",12895559815,53172199,241,Paradigm 722

344,4/26/14,08:30:00,4/26/14 08:30:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCal,"CAL_TYPE=waiting, ISIG=50.64, VCNTR=null, BACKFILL_INDICATOR=null",12895559814,53172199,240,Paradigm 722
```




```csv

345,4/26/14,08:35:00,4/26/14 08:35:00,,,,,,,,,,,,,,,,,,,,,,,,,,,230,49.99,,GlucoseSensorData,"AMOUNT=230, ISIG=49.99, VCNTR=null, BACKFILL_INDICATOR=null",12895559813,53172199,239,Paradigm 722
346,4/26/14,08:35:00,4/26/14 08:35:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCalFactor,CAL_FACTOR=4.591,12895559812,53172199,238,Paradigm 722
349,4/26/14,08:40:00,4/26/14 08:40:00,,,,,,,,,,,,,,,,,,,,,,,,,,,224,47.12,,GlucoseSensorData,"AMOUNT=224, ISIG=47.12, VCNTR=null, BACKFILL_INDICATOR=null",12895559810,53172199,236,Paradigm 722
350,4/26/14,08:45:00,4/26/14 08:45:00,,,,,,,,,,,,,,,,,,,,,,,,,,,216,45.26,,GlucoseSensorData,"AMOUNT=216, ISIG=45.26, VCNTR=null, BACKFILL_INDICATOR=null",12895559809,53172199,235,Paradigm 722
351,4/26/14,08:50:00,4/26/14 08:50:00,,,,,,,,,,,,,,,,,,,,,,,,,,,216,44.45,,GlucoseSensorData,"AMOUNT=216, ISIG=44.45, VCNTR=null, BACKFILL_INDICATOR=null",12895559808,53172199,234,Paradigm 722
352,4/26/14,08:51:00,4/26/14 08:51:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SensorCalFactor,CAL_FACTOR=4.755,12895559807,53172199,233,Paradigm 722
353,4/26/14,08:55:00,4/26/14 08:55:00,,,,,,,,,,,,,,,,,,,,,,,,,,,210,43.15,,GlucoseSensorData,"AMOUNT=210, ISIG=43.15, VCNTR=null, BACKFILL_INDICATOR=null",12895559806,53172199,232,Paradigm 722
```
