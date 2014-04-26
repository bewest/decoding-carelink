
### @erobinson ran several experiments


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

```
05 48 08 0e
0a 48 0b 0e
0a 48 0b 0e
1a 0c 48 0e
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

```
0f 48 08 0e
1a 14 48 0b 0e
3a 14 48 0b 0e
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
