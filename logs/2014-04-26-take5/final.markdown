
### dissect a hexdump of final page

```bash
$ xxd -p -a -g 1 -c 8 logs/2014-04-26-take5/20140427_030926-ReadGlucoseHistory-page-0.data  | cut -c 1-2,3-4,5-6,7-8,9-10,11-12,13-14,15-16,17-18,19-20 --output-delimiter=' ' | tee -a logs/2014-04-26-take5/final.markdown
```

These records line up very well with [the day's csv data](./day.csv).

And reformatted manually:

```
40 40 41 13
42 13
46
4a 13
4c 13
4e 13
4f 13
50 13
51 13
52
   0e 5a 05 40    2014-05-26T00:05:00 SensorTimestamp type=gap
08
13 53
54 13
55 13
55
53
53
52
52
51
51
51
51
54
5e
65
6a
6c
6e
6e
6f
70
71
71
72
73
73
75
76
72
6e
6a
69
68
66
64
60
5e 5a 5d 67 6e 71 72
73 73 74 74 73 74 74
74 74 73 73 73 71 6d 69 66 65
6b 70 72 71 70 70 6f 70
71 73 70 6c 68 65 63 62
61 60 5f 61 63 69 6d 6c
69 68 6c 13 72 74 74 76
77 76 76 7a
7e

   0e 5a 05 48     2014-05-26T08:05:00 SensorTimestamp type=gap
08

   0e 1a 0a 48     2014-04-26T08:10:00
0b

   0e 3a 0a 48     2014-04-26T08:10:00
0b

   0e 3a 0b 48     2014-04-26T08:11:00 SensorSync type=new
0d
00 03

e7
   0e 1a 0c 48     2014-04-26T08:12:00 CalBGForGH amount=231, origin=manual
0e

13 02
   0e 5a 0f 48     2014-05-26T08:15:00 SensorTimestamp type=gap
08

   0e 1a 14 48     2014-04-26T08:20:00 SensorStatus type=off
0b

   0e 3a 14 48     2014-04-26T08:20:00 SensorStatus type=on
0b

   0e 3a 14 48     2014-04-26T08:20:00 SensorSync type=new
0d
01 03

e6 0e 1a 17 48     2014-04-26T08:23:00 CalBGForGH amount=230
0e

e7 0e 1a 19 48     2014-04-26T08:25:00 CalBGForGH amount=231
0e
01 03 01 03
73

ef 11
   0e 1a 23 48     2014-04-26T08:35:00 SensorCalFactor factor=4.591
0f

e2
   0e 1a 25 48     2014-04-26T08:37:00 CalBGForGH amount=226, origin=manual
0e

70
6c 6c
93 12
   0e 1a 33 48    2014-04-26T08:51:00 SensorCalFactor factor=4.755
0f
69 65 61 5c 59 59 59
57 51 4b 47 43 42 42 43
44 44 44 44 44 43 42 3f
40 42 44 45 45 46 47 48
4a 4c

a2
   0e 1a 26 4b    2014-04-26T11:38:00 CalBGForGH amount=162, origin=manual
0e

4f 55 57

e5 11
   0e 1a 32 4b    2014-04-26T11:50:00 SensorCalFactor factor=4.581
0f

5b 5c 5b 59 57 57
59 5c 5b 58 54 52 51 50
4f 4f 50 50 51 52 53 56
59 5a 5a 59 58 57 56 58
59 5b 5e 61 64 66 68 69
6b 6a 6a 6b 6d 6e 70
73

   0e 1a 28 4f    2014-04-26T15:40:00 SensorTimestamp type=last_rf
08

75 77 79
79 79 7a 7e 82 85 87 86

04
   0e 3a 27 50    2014-04-26T16:39:00 CalBGForGH amount=260, origin=manual
0e

04
   0e 3a 28 50    2014-04-26T16:40:00 CalBGForGH amount=260, origin=manual
0e

85

04
   0e 3a 29 50    2014-04-26T16:41:00 CalBGForGH amount=260, origin=manual
0e

04
   0e 3a 2d 50    2014-04-26T16:45:00 CalBGForGH amount=260, origin=manual
0e

13 83

04
   0e 3a 32 50    2014-04-26T16:50:00 CalBGForGH amount=260, origin=manual
0e

83

04
   0e 3a 33 50    2014-04-26T16:51:00 CalBGForGH amount=260, origin=manual
0e

04
   0e 3a 35 50    2014-04-26T16:53:00 CalBGForGH amount=260, origin=manual
0e
84 86

fa
   0e 1a 04 51    2014-04-26T17:04:00 CalBGForGH amount=250, origin=manual
0e

fa
   0e 1a 05 51    2014-04-26T17:05:00 CalBGForGH amount=250, origin=manual
0e

87
88
81

07 11
   0e 1a 0f 51    2014-04-26T17:15:00 SensorCalFactor factor=4.359
0f

80 13
7f 13
7d 13
7a 13 78 13
76 13
73 71 70 71 75
77                2014-04-26T18:15:00 Glucose 238
   0e 1a 0f 52    2014-04-26T18:15:00 SensorTimestamp type=last_rf
08
78
77
76
74
72
70

07
   0e 3a 30 52    2014-04-26T18:48:00 CalBGForGH amount=263
0e

6c                2014-04-26T18:50:00 Glucose 216
65                2014-04-26T18:55:00 Glucose 202
6b                2014-04-26T19:00:00 Glucose 214

24 13
   0e 1a 00 53    2014-04-26T19:00:00 SensorCalFactor factor=4.901
0f

65                2014-04-26T19:10:00 Glucose 202
60                2014-04-26T19:10:00 Glucose 192
5a                2014-04-26T19:15:00 Glucose 180
55                2014-04-26T19:20:00 Glucose 170
51                2014-04-26T19:25:00 Glucose 162
4e                2014-04-26T19:30:00 Glucose 156
4b                2014-04-26T19:35:00 Glucose 150
49                2014-04-26T19:40:00 Glucose 146
48                2014-04-26T19:45:00 Glucose 144
47                2014-04-26T19:50:00 Glucose 142
48                2014-04-26T19:55:00 Glucose 144
47                2014-04-26T20:00:00 Glucose 142
46                2014-04-26T20:05:00 Glucose 140
46                2014-04-26T20:10:00 Glucose 140
47                2014-04-26T20:15:00 Glucose 142
49                2014-04-26T20:20:00 Glucose 146
4c                2014-04-26T20:25:00 Glucose 152
4e                2014-04-26T20:30:00 Glucose 156
4f                2014-04-26T20:35:00 Glucose 158
4f                2014-04-26T20:40:00 Glucose 158
50                2014-04-26T20:45:00 Glucose 160
51                2014-04-26T20:50:00 Glucose 162
51                2014-04-26T20:55:00 Glucose 162
4f                2014-04-26T21:00:00 Glucose 158
4c                2014-04-26T21:05:00 Glucose 152

89
   0e 1a 09 55    2014-04-26T21:09:00 CalBGForGH amount=137
0e

4a                2014-04-26T21:10:00 Glucose 148
47                2014-04-26T21:15:00 Glucose 142
44                2014-04-26T21:20:00 Glucose 136

25 13
   0e 1a 14 55    2014-04-26T21:20:00 SensorCalFactor factor=4.901
0f

41                2014-04-26T21:25:00 Glucose 130
3d                2014-04-26T21:30:00 Glucose 122
3a                2014-04-26T21:35:00 Glucose 116
37                2014-04-26T21:40:00 Glucose 110
36                2014-04-26T21:45:00 Glucose 108
36                2014-04-26T21:50:00 Glucose 108
37                2014-04-26T21:55:00 Glucose 110
38                2014-04-26T22:00:00 Glucose 112
38                2014-04-26T22:05:00 Glucose 112
38                2014-04-26T22:10:00 Glucose 112
39                2014-04-26T22:15:00 Glucose 114
39                2014-04-26T22:20:00 Glucose 114
39                2014-04-26T22:25:00 Glucose 114
39                2014-04-26T22:30:00 Glucose 114
39                2014-04-26T22:35:00 Glucose 114
38                2014-04-26T22:40:00 Glucose 112
36                2014-04-26T22:45:00 Glucose 108
35                2014-04-26T22:50:00 Glucose 106

   0e 1a 32 56    2014-04-26T22:50:00 SensorTimestamp type=last_rf
08

   0e 1a 32 56    2014-04-26T22:50:00 SensorTimestamp type=last_rf
08
33                2014-04-26T22:55:00 Glucose 102

32                2014-04-26T23:00:00 Glucose 100
   0e 1a 00 57    2014-04-26T23:00:00 SensorTimestamp type=last_rf
08

   0e 1a 00 57    2014-04-26T23:00:00 SensorTimestamp type=last_rf
08
31                2014-04-26T23:05:00 Glucose 98

   0e 1a 05 57    2014-04-26T23:05:00 SensorTimestamp type=last_rf
08

   0e 1a 05 57    2014-04-26T23:05:00 SensorTimestamp type=last_rf
08

   0e 1a 05 57    2014-04-26T23:05:00 SensorTimestamp type=last_rf
08

   0e 1a 05 57    2014-04-26T23:05:00 SensorTimestamp type=last_rf
08
01
```


